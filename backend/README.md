# RAGOps — Evidence-Driven Multi-Agent Research Assistant

> An AI-powered research assistant that combines **multi-agent workflows, web search, RAG, evidence verification, and source-grounded report generation**.

RAGOps is a full-stack AI research system designed to answer complex research questions by breaking them into smaller tasks, gathering information from multiple sources, retrieving relevant user-provided documents, verifying evidence, and synthesizing the findings into a structured research report.

---

## 🚀 Overview

Traditional AI assistants can generate fluent answers but may provide unsupported claims or fail to clearly show where their information came from.

**RAGOps** addresses this problem by introducing an evidence-driven research workflow.

Instead of directly asking an LLM to answer a question:

```text
User Question
     ↓
     LLM
     ↓
  Answer
```

RAGOps follows a structured research pipeline:

```text
                         ┌─────────────────┐
                         │      User       │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │ React Research  │
                         │     Portal      │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │    FastAPI      │
                         │     Backend     │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │    LangGraph    │
                         │ Research        │
                         │    Workflow     │
                         └────────┬────────┘
                                  │
                ┌─────────────────┼─────────────────┐
                │                 │                 │
                ▼                 ▼                 ▼
           ┌─────────┐      ┌───────────┐    ┌───────────┐
           │ Planner │      │ Researcher│    │    RAG    │
           └─────────┘      └─────┬─────┘    └─────┬─────┘
                                  │                 │
                                  ▼                 ▼
                            ┌───────────┐      ┌──────────┐
                            │   Tavily  │      │ ChromaDB │
                            │ Web Search│      │ Documents│
                            └───────────┘      └──────────┘
                                  │                 │
                                  └────────┬────────┘
                                           ▼
                                  ┌─────────────────┐
                                  │     Verifier    │
                                  └────────┬────────┘
                                           │
                                           ▼
                                  ┌─────────────────┐
                                  │   Synthesizer   │
                                  └────────┬────────┘
                                           │
                                           ▼
                                  ┌─────────────────┐
                                  │ Evidence-Based  │
                                  │ Research Report │
                                  └─────────────────┘
```

---

# ✨ Key Features

### 🤖 Multi-Agent Research

The research process is divided among specialized agents:

* **Planner Agent** — breaks a research question into smaller tasks
* **Researcher Agent** — gathers information from web and local documents
* **Evidence Verification Agent** — evaluates collected evidence
* **Synthesizer Agent** — produces the final research report

---

### 🌐 Web Research

RAGOps uses **Tavily Search API** to retrieve relevant information from the web.

```text
Research Task
      ↓
Tavily Search
      ↓
Web Sources
      ↓
Research Results
```

---

### 📚 Retrieval-Augmented Generation

Users can provide their own documents.

Supported formats:

* PDF
* DOCX
* TXT
* CSV

The document pipeline is:

```text
Document
   ↓
Document Loader
   ↓
Text Chunks
   ↓
Embeddings
   ↓
ChromaDB
   ↓
Semantic Retrieval
```

When a research task is generated, RAGOps retrieves the most relevant document chunks and combines them with web research.

---

### 🔎 Evidence Verification

Instead of treating every retrieved piece of information as automatically correct, RAGOps represents evidence using a structured model:

```text
Claim
  ↓
Evidence
  ↓
Source
  ↓
Verification
  ↓
Confidence
```

Each evidence item contains:

```text
task
claim
evidence
source
verification
confidence
```

Supported verification states:

* `supported`
* `partially_supported`
* `conflicting`
* `unsupported`

---

### 📊 Structured Research Reports

The final synthesis is organized into:

1. Executive Summary
2. Key Findings
3. Evidence
4. Sources
5. Limitations

This makes the output more useful for research, technical analysis, and decision-support workflows.

---

# 🏗️ Architecture

## Backend Architecture

```text
FastAPI
   │
   ▼
LangGraph
   │
   ├── Planner Agent
   │
   ├── Researcher Agent
   │      │
   │      ├── Tavily Search
   │      │
   │      └── RAG Retriever
   │               │
   │               ▼
   │            ChromaDB
   │
   ├── Evidence Verifier
   │
   └── Synthesizer
```

---

# 🧠 LangGraph Workflow

The current research graph follows:

```text
START
  ↓
Planner
  ↓
Researcher
  ↓
Verifier
  ↓
Synthesizer
  ↓
END
```

### State

The agents communicate through a shared research state:

```python
{
    "question": "...",
    "research_tasks": [...],
    "research_results": [...],
    "verified_evidence": [...],
    "final_report": "..."
}
```

This allows each agent to contribute information to the same research workflow.

---

# 🛠️ Technology Stack

| Layer               | Technology                   |
| ------------------- | ---------------------------- |
| Frontend            | React                        |
| Backend             | FastAPI                      |
| Agent Workflow      | LangGraph                    |
| LLM Framework       | LangChain                    |
| LLM                 | Google Gemini                |
| Embeddings          | Gemini Embeddings            |
| Vector Database     | ChromaDB                     |
| Web Search          | Tavily                       |
| Document Processing | PyMuPDF, python-docx         |
| Data Validation     | Pydantic                     |
| Main Database       | PostgreSQL *(planned)*       |
| Frontend Deployment | Vercel *(planned)*           |
| Backend Deployment  | Render / Railway *(planned)* |

---

# 📁 Project Structure

```text
RAGOps/
│
├── backend/
│   │
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── config.py
│   │   │
│   │   ├── agents/
│   │   │   ├── planner.py
│   │   │   ├── researcher.py
│   │   │   ├── verifier.py
│   │   │   └── synthesizer.py
│   │   │
│   │   ├── graph/
│   │   │   ├── state.py
│   │   │   └── workflow.py
│   │   │
│   │   ├── models/
│   │   │   └── evidence.py
│   │   │
│   │   ├── services/
│   │   │   ├── llm.py
│   │   │   └── mock_llm.py
│   │   │
│   │   ├── tools/
│   │   │   └── web_search.py
│   │   │
│   │   ├── utils/
│   │   │   └── llm_utils.py
│   │   │
│   │   └── rag/
│   │       ├── __init__.py
│   │       ├── loader.py
│   │       ├── chunker.py
│   │       ├── embeddings.py
│   │       ├── vector_store.py
│   │       ├── ingest.py
│   │       └── retriever.py
│   │
│   ├── data/
│   │   ├── documents/
│   │   └── chroma_db/
│   │
│   ├── .env
│   ├── .gitignore
│   ├── requirements.txt
│   └── venv/
│
└── frontend/                 # Planned
```

---

# ⚙️ Backend Setup

## 1. Clone the Repository

```bash
git clone <your-repository-url>
cd RAGOps
```

---

## 2. Create Virtual Environment

Navigate to the backend:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file inside `backend/`:

```env
GEMINI_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
GEMINI_MODEL=gemini-3.8-flash
```

Do **not** commit `.env` to GitHub.

---

# ▶️ Running the Backend

From the `backend` directory:

```bash
uvicorn app.main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 🔌 API Endpoints

## Health Check

### `GET /health`

Checks whether the backend is running.

Example response:

```json
{
  "status": "ok",
  "service": "RAGOps API"
}
```

---

## Upload Document

### `POST /documents/upload`

Uploads and indexes a document.

Supported formats:

```text
PDF
DOCX
TXT
CSV
```

Pipeline:

```text
Upload
  ↓
Loader
  ↓
Chunking
  ↓
Embeddings
  ↓
ChromaDB
```

---

## Research

### `POST /research`

Starts the LangGraph research workflow.

Example request:

```json
{
  "question": "Compare RAG and fine-tuning for reducing hallucinations in AI systems."
}
```

The workflow:

```text
Question
   ↓
Planner
   ↓
Research Tasks
   ↓
Web + Document Retrieval
   ↓
Evidence Verification
   ↓
Synthesis
   ↓
Research Report
```

---

# 🧩 RAG Pipeline

RAGOps uses a standard retrieval-augmented generation pipeline.

### 1. Load

Documents are converted into LangChain `Document` objects.

### 2. Chunk

Large documents are split into smaller pieces.

Current configuration:

```text
Chunk size: 1000
Overlap: 150
```

### 3. Embed

Each chunk is converted into an embedding vector.

### 4. Store

Embeddings and document content are stored in ChromaDB.

### 5. Retrieve

When a research task is generated, the retriever searches for the most relevant chunks.

Current retrieval:

```text
Top K = 5
```

### 6. Generate

Retrieved information is supplied to downstream agents for verification and synthesis.

---

# 🧪 Development Mode

RAGOps includes a **Mock LLM** for development.

```text
use_mock_llm = True
```

This allows the LangGraph workflow to be developed and tested without repeatedly consuming Gemini API quota.

The mock service simulates responses from:

* Planner
* Verifier
* Synthesizer

The real Gemini model can be enabled later.

---

# 🔐 Security Considerations

The project is designed with the following security considerations:

* API keys stored in environment variables
* `.env` excluded from Git
* CORS configured for approved frontend origins
* Uploaded files restricted to supported extensions
* Pydantic validation for structured data
* Evidence schema validation

Additional production security will be added before deployment.

---

# 📈 Planned Improvements

The project is currently under active development.

### Frontend

* [ ] React research dashboard
* [ ] Document upload interface
* [ ] Research question interface
* [ ] Research progress indicator
* [ ] Evidence cards
* [ ] Source explorer
* [ ] Report viewer
* [ ] Research history

### Backend

* [ ] PostgreSQL integration
* [ ] Research history
* [ ] Better error handling
* [ ] Background research jobs
* [ ] Research status tracking
* [ ] Improved citation handling
* [ ] Duplicate document detection
* [ ] Secure file handling
* [ ] Production CORS configuration

### AI / RAG

* [ ] Improved evidence extraction
* [ ] Better source ranking
* [ ] Hybrid web + document retrieval
* [ ] Retrieval evaluation
* [ ] Citation accuracy evaluation
* [ ] Hallucination evaluation
* [ ] Agent performance evaluation

### Deployment

* [ ] Production backend deployment
* [ ] Frontend deployment
* [ ] Environment configuration
* [ ] Production database
* [ ] End-to-end deployment testing

---

# 📊 Evaluation

The system will eventually be evaluated using metrics such as:

### Retrieval Quality

Measures whether the retrieved documents contain relevant information.

### Answer Correctness

Measures whether the generated report accurately answers the research question.

### Citation Accuracy

Measures whether claims are properly connected to supporting sources.

### Hallucination Rate

Measures unsupported claims generated by the system.

### Response Time

Measures the time required to complete a research workflow.

### Agent Performance

Evaluates individual stages such as:

```text
Planner
Researcher
Verifier
Synthesizer
```

---

# 🎯 Example Use Cases

RAGOps can be used for research tasks such as:

* Comparing AI techniques
* Technical literature research
* Product/technology comparison
* Research-paper analysis
* Document-based question answering
* Web + document research
* Evidence collection
* Technical report generation

---

# 💡 Why RAGOps?

RAGOps combines several modern AI engineering concepts into a single system:

```text
LLMs
 +
RAG
 +
Vector Search
 +
Web Search
 +
Multi-Agent Systems
 +
LangGraph
 +
Evidence Verification
 +
FastAPI
 +
React
```

Rather than building only a chatbot, RAGOps focuses on creating a **structured research workflow where information is gathered, retrieved, verified, and synthesized**.

---

# 🗺️ Development Roadmap

```text
Phase 1 — Core Backend
        │
        ├── FastAPI
        ├── LangGraph
        ├── Agents
        ├── Tavily
        └── RAG
              ↓
Phase 2 — API Layer
        │
        ├── Upload API
        ├── Research API
        └── CORS
              ↓
Phase 3 — Frontend
        │
        ├── React
        ├── Research Dashboard
        ├── Upload UI
        └── Report UI
              ↓
Phase 4 — Database
        │
        └── PostgreSQL
              ↓
Phase 5 — Evaluation
        │
        ├── Retrieval
        ├── Citations
        ├── Hallucination
        └── Agent Performance
              ↓
Phase 6 — Production
        │
        ├── Backend Deployment
        ├── Frontend Deployment
        └── Production Testing
```

---

# 👩‍💻 Project Status

**Current status: Active Development**

### Completed

* [x] FastAPI backend
* [x] Environment configuration
* [x] Gemini LLM service
* [x] Development Mock LLM
* [x] LangGraph workflow
* [x] Planner Agent
* [x] Researcher Agent
* [x] Evidence Verification Agent
* [x] Synthesizer Agent
* [x] Tavily web search integration
* [x] PDF/DOCX/TXT/CSV loaders
* [x] Document chunking
* [x] Gemini embeddings
* [x] ChromaDB vector store
* [x] RAG retrieval
* [x] Document ingestion
* [x] Document upload API
* [x] Research API
* [x] Health API
* [x] CORS configuration

### In Progress

* [ ] React frontend
* [ ] PostgreSQL
* [ ] Research history
* [ ] Evaluation system
* [ ] Production security
* [ ] Deployment

---

# 📜 License

This project is currently being developed as an academic and portfolio project.

License information will be added before public production release.

---

# 👤 Author

**Poornima P**

Computer Science and Engineering

RAGOps — Evidence-Driven Multi-Agent Research Assistant

---

> **RAGOps is being developed as a practical exploration of modern AI engineering, combining RAG, multi-agent workflows, web search, evidence verification, and full-stack application development.**
