# AI-Search-Hub
# 🚀 Multi-Agent AI Research Hub

> **A scalable, state-driven Multi-Agent AI system for automated academic and technical research.**

Multi-Agent AI Research Hub is an end-to-end research automation framework that combines **LLMs, Retrieval-Augmented Generation (RAG), real-time web search, data visualization, and iterative quality assurance** into a single workflow orchestrated by **LangGraph**.

Instead of relying on a single LLM prompt, the system decomposes research into multiple specialized AI agents that collaborate through a shared graph state, enabling more reliable, verifiable, and comprehensive technical reports.

---

# ✨ Features

* 🧠 **Multi-Agent Architecture**

  * Independent agents with clearly separated responsibilities.
  * Cyclic execution using LangGraph StateGraph.

* 🌐 **Real-Time Web Research**

  * Retrieves the latest news, benchmarks, documentation, and API updates.

* 📚 **Local RAG Pipeline**

  * Queries technical papers stored in LanceDB.
  * Supports PDF text extraction, tables, and OCR images.

* 📊 **Automatic Data Visualization**

  * Detects numerical comparisons from research results.
  * Dynamically generates Plotly charts using Python REPL.

* 📝 **Professional Report Generation**

  * Produces structured Markdown reports with citations, figures, and technical summaries.

* ✅ **Iterative Quality Assurance**

  * Dedicated Critic Agent verifies evidence and detects hallucinations.
  * Automatically requests additional data or report revisions when necessary.

* ⚡ **Resource Efficient**

  * Local embeddings
  * API-based reasoning
  * Optimized for consumer GPUs (≈6GB VRAM)

---

# 🏗 System Architecture

```text
                         User Query
                              │
                              ▼
                  ┌─────────────────────┐
                  │ Manager / Planner   │
                  └─────────────────────┘
                              │
                 Creates Structured Research Plan
                              │
          ┌───────────────────┴───────────────────┐
          ▼                                       ▼
 ┌──────────────────┐                   ┌──────────────────┐
 │    Web Agent     │                   │   Paper Agent    │
 └──────────────────┘                   └──────────────────┘
          │                                       │
          │      Collect Research in Parallel     │
          └───────────────────┬───────────────────┘
                              ▼
                    Shared Graph State
                              │
                              ▼
                  ┌─────────────────────┐
                  │ Visualization Agent │
                  └─────────────────────┘
                              │
                              ▼
                  ┌─────────────────────┐
                  │    Writer Agent     │
                  └─────────────────────┘
                              │
                              ▼
                  ┌─────────────────────┐
                  │    Critic Agent     │
                  └─────────────────────┘
                     │              │
              Needs Revision      Pass
                     │              │
                     └──────┬───────┘
                            ▼
                    Final Markdown Report
```

---

# 🤖 Agent Responsibilities

## 1. Manager & Planner Agent

The central coordinator responsible for understanding the user's request and converting it into a structured execution plan.

### Responsibilities

* Analyze user intent
* Generate a strict `ResearchPlan`
* Route tasks to appropriate agents
* Coordinate workflow execution

---

## 2. Web Agent

The external information researcher.

### Responsibilities

* Search latest technical information
* Retrieve benchmarks
* Gather news
* Collect API documentation
* Append findings to Graph State

### Tools

* Tavily Search API

---

## 3. Paper Agent

The local academic researcher.

### Responsibilities

* Query LanceDB vector database
* Retrieve relevant document chunks
* Extract PDF text
* Parse tables
* OCR embedded images
* Summarize technical findings

### Technologies

* LanceDB
* PyMuPDF
* Tesseract OCR
* LangChain Retrieval

---

## 4. Visualization Agent

Transforms raw research into meaningful visual insights.

### Responsibilities

* Detect quantitative comparisons
* Generate Python plotting code
* Execute Plotly dynamically
* Store generated figures for report generation

Examples include:

* Benchmark comparison
* Model parameters
* Latency comparison
* Accuracy charts
* Memory consumption

---

## 5. Writer Agent

Synthesizes all collected information into a polished technical report.

### Responsibilities

* Merge web findings
* Merge RAG results
* Embed visualizations
* Produce structured Markdown

Report sections typically include:

* Executive Summary
* Technical Analysis
* Comparative Tables
* Visual Charts
* References

---

## 6. Critic Agent

Acts as the quality assurance layer.

Rather than generating new content, this agent verifies the report against the original user request.

### Validation

* Missing evidence
* Hallucinations
* Logical consistency
* Formatting
* Completeness

### Routing Logic

```text
PASS
   │
   ▼
Return Final Report

FORMAT ERROR
   │
   ▼
Writer Agent

INSUFFICIENT EVIDENCE
   │
   ▼
Web Agent / Paper Agent
```

---

# 🔄 Workflow

```text
User Query
      │
      ▼
Planning
      │
      ▼
Parallel Research
      │
      ▼
Visualization
      │
      ▼
Draft Generation
      │
      ▼
Quality Review
      │
      ▼
Revision Loop (if needed)
      │
      ▼
Final Report
```

---

# 🛠 Tech Stack

| Category              | Technology                 |
| --------------------- | -------------------------- |
| Workflow              | LangGraph                  |
| LLM Framework         | LangChain                  |
| Large Language Models | OpenAI GPT / Google Gemini |
| Vector Database       | LanceDB                    |
| Embedding Model       | BAAI/bge                   |
| User Interface        | Streamlit                  |
| Web Search            | Tavily API                 |
| Visualization         | Plotly                     |
| Python Execution      | Python REPL                |
| Validation            | Pydantic                   |
| Programming Language  | Python 3.11+               |

---

# 📂 Project Structure

```text
multi-agent-ai-research-hub/
│
├── agents/
│   ├── manager.py
│   ├── web_agent.py
│   ├── paper_agent.py
│   ├── visualization_agent.py
│   ├── writer_agent.py
│   └── critic_agent.py
│
├── graph/
│   ├── state.py
│   ├── builder.py
│   └── workflow.py
│
├── tools/
│   ├── tavily_search.py
│   ├── retrieval.py
│   ├── pdf_parser.py
│   ├── chart_generator.py
│   └── python_repl.py
│
├── database/
│   └── LanceDB/
│
├── prompts/
│
├── config/
│
├── reports/
│
├── data/
│
├── main.py
│
└── README.md
```

---

# 🚀 Why This Project?

Traditional LLM applications typically follow a single prompt → single response paradigm.

This project demonstrates how complex research workflows can be decomposed into specialized AI agents that collaborate through a shared state machine, enabling:

* Better modularity
* Easier debugging
* Improved scalability
* Higher factual reliability
* Automated iterative refinement
* Separation of concerns following modern software engineering principles

---

# 📈 Future Improvements

* Memory-enabled agents
* Multi-document citation tracking
* Hybrid retrieval (BM25 + Dense)
* Multi-modal report generation
* PDF & DOCX export
* Human-in-the-loop review
* Agent performance monitoring
* Streaming workflow execution
* Multi-user deployment
* Docker & Kubernetes support

---

# 📜 License

This project is released under the **MIT License**.

---

# 🙏 Acknowledgements

This project builds upon the excellent open-source ecosystem surrounding:

* LangGraph
* LangChain
* LanceDB
* Plotly
* Tavily
* Hugging Face
* OpenAI
* Google Gemini
