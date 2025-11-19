# Local RAG Research Analyst

A fully local research assistant that performs document retrieval and generates research-backed answers without requiring the internet or API keys.

This system collects information from Wikipedia and ArXiv, stores it in a FAISS vector database, and uses a local FLAN-T5 model to generate grounded research responses. It also includes a Streamlit frontend for a clean UI experience.

---

## 🚀 Features

* **Fully Offline Option Available**
* **No API Keys Required**
* **Retrieves Real Research Data**

  * Wikipedia summaries
  * ArXiv paper abstracts
* **FAISS Vector Database**

  * Stores embeddings
  * Enables semantic retrieval
* **Local LLM**

  * Uses FLAN-T5 Base for generation
  * No external model calls
* **Streamlit Frontend**

  * Simple UI
  * Input → Research → Final Answer displayed

---

## 🧩 Tech Stack

| Component        | Technology                         |
| ---------------- | ---------------------------------- |
| Language         | Python                             |
| Embeddings       | SentenceTransformer (MiniLM-L6-v2) |
| Vector DB        | FAISS                              |
| LLM              | FLAN-T5                            |
| Research Sources | Wikipedia + ArXiv                  |
| Frontend         | Streamlit                          |

## 🧠 How It Works

1. **User enters a research query**
2. System searches:

   * Wikipedia (summary)
   * ArXiv (latest relevant paper)
3. Retrieved text is:

   * Embedded using MiniLM
   * Stored into FAISS
4. For each new question:

   * FAISS returns the most relevant documents
5. Local FLAN-T5 generates the final answer using:

   ```
   "Answer using only the research provided"
   ```

Everything can run offline if online search is disabled.

---

## 🧪 Sample Prompts

Try:

* Impact of AI in finance
* Role of blockchain in supply chain
* Applications of quantum computing in drug discovery
* Latest research on cybersecurity attacks
* Machine learning in space exploration

---

## 📌 Model Replacement (Optional)

You can switch FLAN-T5 to any local model supported by `transformers`, including:

* DistilGPT2
* GPT-J
* Dolly
* Mistral (via local pipeline)


