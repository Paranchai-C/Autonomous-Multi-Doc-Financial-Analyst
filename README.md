# Assignment 3: Autonomous Multi-Doc Financial Analyst

**Student Name:** Paranchai Chianwichai  
**Student ID:** 114522606  
**LLM Model Used:** gpt-40-mini

## Benchmark Results Summary

The following table summarizes the evaluation scores across different chunk sizes, embedding models, and agent architectures:

| Chunk Size | Embedding Model | Legacy Mode (LangChain) | Graph Mode (LangGraph) |
| :--- | :--- | :--- | :--- |
| **1000** | `text-embedding-3-small` | 9/14 | 9/14 |
| **1000** | `text-embedding-3-large` | 10/14 | 11/14 |
| **2000** | `text-embedding-3-small` | 6/14 | 10/14 |
| **2000** | `text-embedding-3-large` | 9/14 | 10/14 |
| **3000** | `text-embedding-3-small` | 9/14 | 10/14 |
| **3000** | `text-embedding-3-large` | 10/14 | 11/14 |

---

## 1. Comparison of Differing Embedding Models

For this evaluation, two different embedding models from OpenAI were compared: `text-embedding-3-small` and `text-embedding-3-large`.

**Analysis:** Based on the benchmark data, `text-embedding-3-large` consistently outperformed or matched `text-embedding-3-small` across all configurations.

---

## 2. Chunk Size Impact: Context Precision vs. Context Completeness

### Small Chunks (1000) - Emphasizing "Context Precision"
* **Advantage:** The LLM receives highly focused, concise text snippets, effectively eliminating irrelevant noise. When paired with a powerful embedding model (Large), this precision yielded the peak score of 11/14.
* **Trade-off:** There is a high risk of "table splitting." A massive Consolidated Statement table might be cut in half, separating the year headers (e.g., 2023, 2024) from the actual financial figures. If this happens, the agent loses the ability to map the numbers to the correct year.

### Large Chunks (3000) - Emphasizing "Context Completeness"
* **Advantage:** Ensures that large financial tables remain structurally intact within a single chunk. The agent can see both the column headers and the data rows simultaneously, preventing alignment errors.
* **Trade-off:** Retrieving multiple massive chunks (e.g., k=3) floods the LLM with excessive text. This can trigger the "Lost in the Middle" phenomenon, where the LLM's attention span falters, and it overlooks specific numbers hidden deep within the dense context. Furthermore, it significantly increases token consumption.

### Conclusion
While 2000 serves as a safe baseline, the optimal configuration for this specific financial task was utilizing a smaller chunk size (1000) for strict precision, offset by the high semantic accuracy of a Large embedding model and the self-correcting routing of LangGraph to handle any retrieval misses.

---

## 🚀 How to Run the Project

### 1. Environment Setup
It is highly recommended to use a virtual environment (Python 3.11).

**Create and activate the environment:**
```bash
# macOS / Linux
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
