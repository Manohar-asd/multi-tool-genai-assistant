# Multi-Tool GenAI Chat Assistant

**Agent-Based Orchestration using Azure AI Foundry**

A multi-tool Generative AI chatbot built with Azure AI Foundry and Azure OpenAI, demonstrating agent-based orchestration and LLM function/tool calling. The assistant intelligently selects and invokes tools to search documents, answer questions, summarize text, and generate emails through a single chat interface.

## Key Capabilities

- One unified chatbot interface
- Document search using vector embeddings (RAG)
- Document-based question answering
- Text summarization
- Professional email generation
- LLM-driven function / tool calling
- Agent-based orchestration
- Web API + Chat UI

## Concepts Demonstrated

### Agent Orchestration
A central GenAI agent interprets user intent and dynamically coordinates multiple tools.

### Function / Tool Calling
Tools are registered with structured schemas, and the LLM autonomously decides which tool to invoke.

### Retrieval-Augmented Generation (RAG)
Documents are embedded, stored in a vector database, retrieved via similarity search, and used as grounded context for answers.

## System Architecture

```
User
  ↓
Streamlit UI / REST API
  ↓
Agent (Azure OpenAI)
  ↓
Function / Tool Selection
  ├── Summarization Tool
  ├── Email Generation Tool
  └── Document Search & Q&A Tool (RAG)
      ↓
Azure AI Foundry (LLM + Embeddings)
```

## Tech Stack

- Python 3.10+
- Azure AI Foundry
- Azure OpenAI
- FastAPI (Backend API)
- Streamlit (Chat UI)
- FAISS (Vector database)
- PyPDF (Document loading)
- dotenv

## Project Structure

```
multi_tool_chatbot/
├── app.py                  # FastAPI application
├── agent.py                # Agent orchestration & tool calling
├── azure_client.py         # Azure OpenAI client configuration
├── document_index.py       # Document indexing (FAISS)
├── ui.py                   # Streamlit chat interface
│
├── tools/
│   ├── summarize.py        # Text summarization tool
│   ├── email.py            # Email generation tool
│   └── document_qa.py      # Document search & Q&A tool
│
├── data/
│   └── docs/               # Input documents (PDF/TXT)
│
├── requirements.txt
├── .env.example
└── README.md
```

## Setup & Installation

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Environment Variables

Create a `.env` file using `.env.example`:

```env
AZURE_OPENAI_API_KEY=your_api_key_here
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT=your-deployment-name
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=your-embedding-deployment-name
AZURE_OPENAI_API_VERSION=2024-02-15-preview
```

⚠️ `.env` is intentionally excluded from the repository for security reasons.

## Document Indexing (One-Time Step)

Add PDF or TXT files to:

```
data/docs/
```

Then run:

```bash
python document_index.py
```

This creates the FAISS vector index used for document search and Q&A.

## Running the Application

### Start Backend API

```bash
uvicorn app:app --reload
```

Open API docs:
```
http://127.0.0.1:8000/docs
```

### Start Chat UI (Optional)

```bash
streamlit run ui.py
```

## Example Queries

### Document Search / Q&A
> "What does the document say about system architecture?"

### Summarization
> "Summarize: Artificial intelligence is transforming industries..."

### Email Generation
> "Write an email requesting an internship opportunity."

### General Question
> "Explain agent-based orchestration in GenAI systems."

## 🎓 Academic Alignment

This project fulfills the following requirements:

**Multi-Tool Chat Assistant**
- Search documents
- Summarize text
- Answer questions
- Generate emails

**Concepts**
- Function / tool calling
- Agent orchestration

## Security Note

Sensitive credentials are managed via environment variables and are not included in the repository. A sample configuration file (`.env.example`) is provided for reproducibility.

## 📌 Author

**Manohara Sai Ch**  
Multi-Tool GenAI Assistant using Azure AI Foundry
