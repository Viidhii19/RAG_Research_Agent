import os
import wikipedia
import arxiv
import faiss
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from sentence_transformers import SentenceTransformer

DB_PATH = "vector.index"
DOCS_PATH = "doc.txt"

# --------------------------------
# Load Embedding & LLM
# --------------------------------
print("🔧 Loading Embedding Model…")
embedder = SentenceTransformer("all-MiniLM-L6-v2")

print("🧠 Loading Local FLAN-T5 Model…")
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

# --------------------------------
# Load or create FAISS index
# --------------------------------
if os.path.exists(DB_PATH):
    print("📁 Loading existing vector DB")
    index = faiss.read_index(DB_PATH)
    with open(DOCS_PATH, "r", encoding="utf8") as f:
        docs = f.read().split("\n\n")
else:
    print("📁 Creating new vector DB")
    index = faiss.IndexFlatL2(384)
    docs = []

# --------------------------------
# Add text to FAISS
# --------------------------------
def add_to_db(text, source="Unknown"):
    global docs
    docs.append(text)
    
    emb = embedder.encode([text])
    index.add(emb)

    faiss.write_index(index, DB_PATH)
    
    with open(DOCS_PATH, "w", encoding="utf8") as f:
        f.write("\n\n".join(docs))

    print(f"➕ Added info from -> {source}")

# --------------------------------
# FIXED ArXiv Search
# --------------------------------
def search_arxiv(query):
    try:
        print("📄 Searching ArXiv…")
        client = arxiv.Client()
        results = client.results(arxiv.Search(query=query, max_results=1))

        for r in results:
            text = f"{r.title}\n{r.summary}"
            add_to_db(text, "ArXiv Paper")
            break

    except Exception as e:
        print("⚠ ArXiv error:", e)

# --------------------------------
# Wikipedia Search
# --------------------------------
def search_wikipedia(query):
    try:
        print("📘 Searching Wikipedia…")
        text = wikipedia.summary(query, sentences=5)
        add_to_db(text, "Wikipedia")

    except Exception as e:
        print("⚠ Wikipedia error:", e)

# --------------------------------
# Token-Safe Local Generator
# --------------------------------
def generate_answer(prompt):
    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=400    # fits inside model limit
    )
    
    outputs = model.generate(
        inputs["input_ids"],
        max_length=300,
        do_sample=False
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# --------------------------------
# Research Query (RAG)
# --------------------------------
def research_query(query):
    print(f"\n🔎 Researching: {query}")
    search_wikipedia(query)
    search_arxiv(query)

    # Retrieve results
    emb = embedder.encode([query])
    distances, ids = index.search(emb, k=4)

    # Safe retrieval handling in case index is empty or low
    retrieved_docs = [docs[i] for i in ids[0] if i < len(docs)]
    context = "\n\n".join(retrieved_docs)

    prompt = (
        f"Answer using only the following research:\n\n"
        f"{context}\n\nQuestion: {query}\nAnswer:"
    )

    answer = generate_answer(prompt)
    print("\n🧠 Final Answer:\n", answer)
    return answer

# --------------------------------
# CLI Runner
# --------------------------------
if __name__ == "__main__":
    print("\n🚀 Local RAG Research Analyst Ready!")

    while True:
        q = input("\nAsk a research question (or type exit): ")
        if q.lower().strip() == "exit":
            break
        
        research_query(q)