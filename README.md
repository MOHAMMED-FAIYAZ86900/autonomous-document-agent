# 🤖 Autonomous AI Document Generation Agent

> An autonomous AI-powered document generation system built with **FastAPI**, **Python**, and **Groq LLM**. The agent autonomously understands a natural language request, creates its own execution plan, executes the tasks, reflects on the generated content, and produces a polished Microsoft Word (`.docx`) document.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Groq](https://img.shields.io/badge/LLM-Groq-orange)
![GitHub Actions](https://img.shields.io/badge/CI-GitHub%20Actions-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 🚀 Live Demo

**API URL**

https://autonomous-document-agent-1.onrender.com

**Swagger Documentation**

https://autonomous-document-agent-1.onrender.com/docs

---

# 📌 Project Overview

This project demonstrates an **Autonomous AI Agent** capable of:

- Understanding natural language requests
- Creating its own execution plan
- Executing planned tasks
- Generating structured business documents
- Performing reflection/self-evaluation
- Exporting polished Microsoft Word documents
- Providing downloadable generated documents through REST APIs

Unlike a traditional chatbot, this system behaves like an autonomous agent by planning and executing multiple steps before producing the final output.

---

# ✨ Features

## Autonomous Planning

The Planner Agent analyzes the user's request and creates an internal execution plan.

Example:

User Request

```
Generate a business proposal for an AI startup.
```

Generated Plan

```
✔ Understand request
✔ Determine document structure
✔ Generate business proposal
✔ Format document
✔ Save DOCX
✔ Review output
```

---

## Intelligent Content Generation

Uses Groq LLM to generate high-quality structured content.

Supported document types include:

- Business Proposal
- Technical Report
- Project Plan
- SOP
- Meeting Minutes
- Product Specification
- Research Summary
- AI Reports
- Custom Business Documents

---

## Reflection / Self Evaluation

After generating the document, the Reflector Agent evaluates:

- completeness
- quality
- clarity
- missing information
- improvement suggestions

This improves document quality before returning the final response.

---

## Word Document Generation

Automatically exports

```
.docx
```

documents using **python-docx**.

---

## REST API

Built using FastAPI.

Interactive Swagger UI included.

---

## Docker Support

Fully containerized for deployment.

---

## CI/CD

GitHub Actions automatically runs:

- Ruff
- Black
- isort
- Pytest
- Coverage
- Docker Build

---

# 🏗 System Architecture

```
                   User
                     │
                     ▼
               FastAPI API
                     │
                     ▼
            Agent Orchestrator
                     │
      ┌──────────────┼──────────────┐
      ▼              ▼              ▼
  Planner         Executor      Reflector
      │              │              │
      └──────────────┼──────────────┘
                     ▼
          Document Generator
                     │
                     ▼
          Microsoft Word (.docx)
                     │
                     ▼
             File Storage
```

---

# 🧠 Autonomous Workflow

```
User Request
      │
      ▼
Planner
      │
      ▼
Task List Generation
      │
      ▼
Executor
      │
      ▼
Generate Content
      │
      ▼
DOCX Generator
      │
      ▼
Reflector
      │
      ▼
Final Response
```

---

# 📁 Project Structure

```
autonomous-document-agent/

│
├── app/
│   ├── api/
│   ├── agents/
│   │     ├── planner.py
│   │     ├── executor.py
│   │     ├── reflector.py
│   │
│   ├── services/
│   │     ├── groq_service.py
│   │     ├── document_generator.py
│   │
│   ├── models/
│   ├── schemas/
│   ├── core/
│   └── main.py
│
├── storage/
│
├── tests/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# ⚙ Technology Stack

## Backend

- Python 3.11
- FastAPI
- Pydantic

## AI

- Groq API
- LLM

## Document Generation

- python-docx

## Testing

- pytest
- pytest-cov

## Formatting

- Black
- Ruff
- isort

## Deployment

- Docker
- Render

## CI/CD

- GitHub Actions

---

# 📦 Installation

Clone

```bash
git clone https://github.com/USERNAME/autonomous-document-agent.git

cd autonomous-document-agent
```

Create virtual environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Linux

```bash
source .venv/bin/activate
```

Install

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create

```
.env
```

```
GROQ_API_KEY=your_api_key

MODEL_NAME=llama-3.3-70b-versatile

APP_ENV=development
```

---

# ▶ Run

```bash
uvicorn app.main:app --reload
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

# 🐳 Docker

Build

```bash
docker build -t autonomous-document-agent .
```

Run

```bash
docker run -p 8000:8000 autonomous-document-agent
```

---

# 📚 API Endpoints

## Health

```
GET /health
```

Returns service health.

---

## Run Agent

```
POST /agent/run
```

Request

```json
{
    "user_request":"Generate an AI business proposal."
}
```

Response

```json
{
    "status":"completed",
    "generated_content":"...",
    "reflection":"...",
    "errors":[]
}
```

---

## List Documents

```
GET /documents
```

---

## Download Document

```
GET /documents/{filename}
```

---

# 🧪 Example Request

```json
{
  "user_request":"Generate a detailed report on Artificial Intelligence."
}
```

---

# 📄 Generated Output

The agent produces:

- Executive Summary

- Objectives

- Detailed Content

- Recommendations

- Conclusion

- Reflection

- DOCX Export

---

# 🧪 Testing

Run

```bash
pytest
```

Coverage

```bash
pytest --cov=app
```

---

# 🔄 CI Pipeline

GitHub Actions performs

```
Push

↓

Black

↓

Ruff

↓

isort

↓

Pytest

↓

Coverage

↓

Docker Build

↓

Deployment Ready
```

---

# 🚀 Deployment

Hosted on

Render

Public URL

```
https://autonomous-document-agent-1.onrender.com
```

---

# 📈 Future Improvements

- Multi-Agent Architecture
- RAG
- Vector Database
- PostgreSQL
- Redis
- JWT Authentication
- Background Jobs
- Async Task Queue
- Streaming Responses
- Multi-LLM Routing
- AWS S3 Storage
- Monitoring
- LangGraph Integration

---

# 📊 Engineering Decisions

### Reflection

Implemented to improve generated content quality.

### FastAPI

Chosen for performance and automatic OpenAPI generation.

### Docker

Ensures reproducible deployments.

### Groq

Provides fast inference with a free developer tier.

---

# 🏆 Assignment Requirements Covered

✅ Autonomous Planning

✅ REST API

✅ Natural Language Understanding

✅ Task Planning

✅ LLM Integration

✅ Reflection / Self Check

✅ DOCX Generation

✅ Error Handling

✅ Docker Deployment

✅ GitHub Actions

✅ Public API

---

# 👨‍💻 Author

**Mohammed Faiyaz**

AI / ML Engineer

Python Developer

GitHub

https://github.com/MOHAMMED-FAIYAZ86900

LinkedIn

(Add Your LinkedIn URL)

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.