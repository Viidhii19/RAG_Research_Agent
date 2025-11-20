# Local RAG Research Analyst

A privacy-first **Retrieval-Augmented Generation (RAG)** system that autonomously conducts research using academic sources and generates answers locally.

Unlike standard API-wrappers, this project runs the **Embedding Model** and **LLM** entirely on your local CPU, ensuring zero data privacy risks and no API costs.

---

## 🚀 Key Features

* **Hybrid Architecture:** Fetches real-time data from the web (ArXiv/Wikipedia) but performs all processing and text generation locally.
* **Zero-Cost Inference:** Uses `google/flan-t5-base` for generation, removing the need for OpenAI/Anthropic API keys.
* **Vector Search:** Implements **FAISS** and **SentenceTransformers** (`all-MiniLM-L6-v2`) for semantic similarity search.
* **Self-Building Knowledge Base:** Every query automatically updates the local vector index, making the agent smarter over time.
* **Interactive UI:** Built with **Streamlit** for an easy-to-use research dashboard.

---

## 🛠️ Tech Stack

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Language** | Python | Core Logic |
| **LLM** | Google FLAN-T5 | Local Text Generation |
| **Embeddings** | SentenceTransformer | `all-MiniLM-L6-v2` (384 dim) |
| **Vector DB** | FAISS | High-performance similarity search |
| **Data Sources** | `arxiv` + `wikipedia` | Real-time academic retrieval |
| **Frontend** | Streamlit | User Interface |

---

## 🧠 How It Works

1.  **User Input:** You ask a question (e.g., *"Role of blockchain in supply chain"*).
2.  **Data Aggregation:** The agent searches **Wikipedia** (general context) and **ArXiv** (technical papers).
3.  **Vectorization:** Text chunks are converted into embeddings using `SentenceTransformer`.
4.  **Indexing:** Embeddings are stored in a local **FAISS** index (`vector.index`).
5.  **Retrieval:** The system searches the vector DB for the top 4 chunks relevant to the query.
6.  **Generation:** The retrieved context is fed into **FLAN-T5**, which synthesizes a final answer strictly based on the research.

---

## 💻 Installation & Run

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/yourusername/local-rag-agent.git](https://github.com/yourusername/local-rag-agent.git)
    cd local-rag-agent
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the App**
    ```bash
    streamlit run app.py
    ```

---

## 🧪 Sample Research Queries
Try these to test the RAG capabilities:
* *"Zero-day vulnerability detection mechanisms"*
* *"Impact of Quantum Computing on Cryptography"*
* *"Recent advancements in Transformer architectures"*
* *"Role of AI in early cancer detection"*

---

## 🔮 Future Improvements
* [ ] Add support for **Llama-3-8B** (quantized) for better reasoning.
* [ ] Implement **PDF Upload** 
* [ ] Add citation sources (links to papers) in the final response.


## Output

https://drive.google.com/file/d/1PFOTmRx_fBX7G01T1f7659sXgE4ekXZ8/view?usp=sharing


