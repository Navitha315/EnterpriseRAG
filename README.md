# 🚀 Enterprise RAG System with Automated Google Drive Integration

An end-to-end **Enterprise Retrieval-Augmented Generation (RAG)** application that automatically ingests enterprise documents from Google Drive, indexes them into a vector database, and enables intelligent question answering through a FastAPI API, Telegram Bot, and Streamlit UI.

---

## 📌 Features

- 📄 Supports multiple document formats
  - PDF
  - DOCX
  - TXT
  - Excel
  - PowerPoint (extensible)

- 🧠 Semantic Retrieval using ChromaDB

- 🤖 LLM-powered Question Answering using Groq

- 📚 Source Document Citation

- 🔍 Semantic Chunking & Embeddings

- ☁ Automated Google Drive Synchronization

- ⚡ n8n Workflow Automation

- 📱 Telegram Bot Integration

- 💻 Streamlit Web Interface

- 🚫 Duplicate Document Detection

---

# 🏗 System Architecture

```
                Google Drive
                     │
                     ▼
          n8n Google Drive Trigger
                     │
                     ▼
            Download New Document
                     │
                     ▼
       FastAPI (/upload-ingest API)
                     │
                     ▼
         Document Parsing & Chunking
                     │
                     ▼
        HuggingFace Sentence Embeddings
                     │
                     ▼
               ChromaDB Vector Store
                     │
                     ▼
              FastAPI (/query API)
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
    Telegram Bot          Streamlit UI
          │                     │
          └──────────┬──────────┘
                     ▼
                    User
```

---

# 📂 Project Structure

```
EnterpriseRAG/
│
├── app.py
├── streamlit_app.py
├── requirements.txt
│
├── db/
├── llm/
├── loaders/
├── services/
├── utils/
├── telegram_bot/
│
├── documents/
├── chroma_db/
```

---

# 🛠 Technologies Used

### Backend
- FastAPI
- Python

### Vector Database
- ChromaDB

### Embedding Model
- HuggingFace Sentence Transformers

### Large Language Model
- Groq Llama

### Automation
- n8n

### Cloud Storage
- Google Drive API

### Frontend
- Streamlit

### Messaging Platform
- Telegram Bot API

### Libraries
- LangChain
- PyMuPDF
- python-docx
- openpyxl
- python-pptx
- pytesseract
- Pillow

---

# ⚙ Workflow

### Document Ingestion

1. Upload enterprise documents to Google Drive.
2. n8n detects newly uploaded files.
3. Documents are downloaded automatically.
4. FastAPI parses the documents.
5. Text is chunked.
6. Embeddings are generated.
7. Chunks are stored inside ChromaDB.

---

### Question Answering

1. User submits a question.
2. ChromaDB retrieves the most relevant chunks.
3. Context is passed to Groq LLM.
4. AI generates an answer.
5. Source documents are returned with the response.

---

# 🚀 APIs

## Upload & Ingest

```
POST /upload-ingest
```

Uploads a document and indexes it into the vector database.

---

## Query

```
POST /query
```

Example Request

```json
{
  "question": "What is the leave policy?"
}
```

Example Response

```json
{
  "answer": "...",
  "documents": [
    {
      "source": "employee_handbook.docx"
    }
  ]
}
```

---

# 🤖 Telegram Bot

Users can interact with the Enterprise Knowledge Base directly through Telegram.

Example:

```
User:
What is the travel reimbursement policy?

Bot:
Employees receive a daily meal allowance of $35...

Source:
travel_policy.docx
```

---

# 💻 Streamlit UI

The project includes a simple chat interface built with Streamlit that communicates with the FastAPI backend for real-time enterprise document question answering.

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/EnterpriseRAG.git
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run FastAPI

```bash
uvicorn app:app --reload
```

Run Streamlit

```bash
streamlit run streamlit_app.py
```

---

# Future Enhancements

- Cloud Deployment
- Authentication
- OCR Support
- Chat History
- Multi-user Access
- Advanced Source Ranking
- Teams/Slack Integration
- Persistent Cloud Vector Database

---

# 👨‍💻 Author

**Navitha Elango**

Integrated M.Tech (CSE with Business Analytics)

VIT Chennai

---

# ⭐ Project Highlights

- End-to-End Enterprise RAG System
- Automated Google Drive Synchronization
- Semantic Search using ChromaDB
- Groq LLM Integration
- FastAPI REST APIs
- n8n Workflow Automation
- Telegram Chatbot
- Streamlit Web Application
- Multi-format Enterprise Document Support
- Source-aware AI Responses
