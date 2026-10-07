RAGOps — Evidence-Driven AI Research Assistant

RAGOps is a research assistant I built to make research questions easier to explore using web search, document retrieval, and a multi-agent workflow.

Instead of asking an LLM to directly answer a question, RAGOps breaks the question into smaller research tasks, collects relevant information, checks the evidence, and then generates a structured report with sources and confidence scores.

What it does

Accepts a research question through a web interface

Supports PDF, DOCX, TXT and CSV uploads

Retrieves relevant content from uploaded documents

Searches the web for additional information

Breaks complex questions into smaller research tasks

Verifies collected evidence

Generates a structured research report

Shows claims, evidence, sources, verification status and confidence

Allows the final report to be downloaded

How it works

User
  ↓
React Frontend
  ↓
FastAPI Backend
  ↓
LangGraph Workflow
  ↓
Planner Agent
  ↓
Researcher Agent
  ├── Web Search (Tavily)
  └── Document Retrieval (RAG)
  ↓
Verifier Agent
  ↓
Evidence
  ↓
Synthesizer Agent
  ↓
Research Report

The main idea is to separate the research process into stages instead of relying on one large LLM prompt.

Agents

Planner Agent

Breaks the user's research question into smaller research tasks so the research process is organized.

Researcher Agent

Collects information for each task using web search and relevant chunks from uploaded documents.

Verifier Agent

Reviews collected information and converts useful findings into structured evidence.

Each evidence item contains:

Claim
Evidence
Source
Verification
Confidence

Verification values are:

supported

partially_supported

conflicting

unsupported

Synthesizer Agent

Uses verified evidence to create the final report with sections such as Executive Summary, Key Findings, Evidence, Sources and Limitations.

RAG Pipeline

Upload Document
      ↓
Document Loader
      ↓
Text Extraction
      ↓
Chunking
      ↓
Embeddings
      ↓
ChromaDB
      ↓
Retriever
      ↓
Relevant Document Chunks
      ↓
Research Workflow

Supported formats:

PDF

DOCX

TXT

CSV

Evidence-Driven Research

One of the main ideas behind RAGOps is that the final answer should not be treated as the only output.

Claim
  ↓
Evidence
  ↓
Source
  ↓
Verification
  ↓
Confidence

This makes the result easier to inspect instead of simply returning an unexplained AI-generated answer.

Tech Stack

Frontend

React

Vite

JavaScript

CSS

Backend

Python

FastAPI

Uvicorn

AI / Agent Workflow

LangChain

LangGraph

Groq API

RAG

LangChain document loaders

RecursiveCharacterTextSplitter

Embeddings

ChromaDB

Web Research

Tavily Search API

Document Processing

PyMuPDF

python-docx

docx2txt

CSVLoader

Deployment

Vercel — frontend

Render — backend

Project Structure

RAGOps/
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   │   ├── planner.py
│   │   │   ├── researcher.py
│   │   │   ├── verifier.py
│   │   │   └── synthesizer.py
│   │   ├── graph/
│   │   │   ├── state.py
│   │   │   └── workflow.py
│   │   ├── models/
│   │   │   └── evidence.py
│   │   ├── rag/
│   │   │   ├── loader.py
│   │   │   ├── chunker.py
│   │   │   ├── embeddings.py
│   │   │   ├── vector_store.py
│   │   │   ├── ingest.py
│   │   │   └── retriever.py
│   │   ├── services/
│   │   │   └── llm.py
│   │   ├── tools/
│   │   │   └── web_search.py
│   │   ├── utils/
│   │   │   └── llm_utils.py
│   │   ├── config.py
│   │   └── main.py
│   ├── data/
│   │   ├── documents/
│   │   └── chroma_db/
│   └── requirements.txt
│
└── frontend/
    ├── src/
    │   ├── App.jsx
    │   ├── api.js
    │   └── ...
    └── package.json

Running Locally

Backend

cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

Create a .env file:

GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
GROQ_MODEL=openai/gpt-oss-20b
USE_MOCK_LLM=False

Start the backend:

uvicorn app.main:app --reload

Frontend

cd frontend
npm install

Create .env:

VITE_API_URL=http://127.0.0.1:8000

Start it:

npm run dev

API Endpoints

Health Check

GET /health

Upload Document

POST /documents/upload

Research

POST /research

Example:

{
  "question": "What is the main difference between RAG and fine-tuning?"
}

Environment Variables

API keys should never be committed to GitHub.

GROQ_API_KEY=
TAVILY_API_KEY=
VITE_API_URL=

Keep .env in .gitignore and add production values through the hosting platform's environment-variable settings.

Deployment

The deployed architecture is:

Vercel
  ↓
React Frontend
  ↓
Render
  ↓
FastAPI Backend

The frontend uses VITE_API_URL to point to the deployed backend.

Example Research Question

According to the uploaded document, what is the main difference between RAG and fine-tuning?

RAGOps can retrieve the relevant document chunks, verify the evidence, and generate a structured report based on the retrieved information.

Limitations

RAGOps is designed to make research more traceable, but evidence-backed output does not automatically mean every generated statement is correct.

The result still depends on:

quality of retrieved documents

quality of web search results

evidence verification

LLM output

source reliability

For important or high-stakes decisions, the original sources should always be checked.

Why I Built It

I built RAGOps to understand how a real AI research system can be structured beyond a basic chatbot.

The project helped me work with RAG, vector databases, embeddings, LangChain, LangGraph, multi-agent workflows, web search, evidence verification, FastAPI, React, API integration and deployment.

The main focus is not just generating an answer, but showing where the answer came from and how the evidence was evaluated.

Future Improvements

Research history with a database

Better source ranking

Stronger citation validation

Parallel research tasks

Improved document management

Automated retrieval and answer evaluation

Authentication and user accounts

More document formats

Background research jobs for longer queries

Author

Poornima P
Computer Science Engineering Student

Built as a learning and portfolio project focused on RAG, agentic AI, and evidence-driven research.