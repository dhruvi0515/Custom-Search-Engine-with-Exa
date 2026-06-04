# 🎀 Build a Custom Search Engine with Exa 🎀

Welcome to my custom-built, full-stack search engine application! This project started as a console-based tutorial journey to understand AI-powered semantic search and was beautifully upgraded into a live, interactive, pastel-themed web application.

## 🚀 Live Website Demo
See my search engine in action here: **[👉 https://custom-search-engine-with-exa-9bild48wnbwlgy6x4vnqjz.streamlit.app/ 👈]**

---

## 📖 Project Journey & Concepts Learned

### 💡 Introduction to Semantic Search & LLMs
Traditional search engines (like standard Google) rely strictly on **keyword matching**—looking for the exact phrases you typed. This project leverages **Natural Language Processing (NLP)** and **Large Language Models (LLMs)** via the **Exa API** to perform **semantic searches**. 

Exa understands the *intent* and *context* behind human language, allowing it to find exactly what you mean even if you don't use the exact keywords.

### ⚡ Step 1: The Core Backend (`main.py`)
Following the foundational tutorial, I first built a command-line search tool to understand how Exa structure queries and handles responses. 

* **Library Used:** `exa_py`
* **Data Fields Explored:** For every query, Exa returns custom data including `score` (relevance), `title`, `url`, `publishedDate`, and `author`.

The original console script queries for keyword-specific domains (like pulling coffee trends straight from TikTok):

```python
from exa_py import Exa

# Initialize Exa (API key hidden for security)
exa = Exa('YOUR_KEY_HERE')

query = input('Search here: ')

response = exa.search(
  query,
  num_results=5,
  type='keyword',
  include_domains=['[https://www.tiktok.com](https://www.tiktok.com)'],
)

# Clean, formatted console output
for result in response.results:
  print(f'Title: {result.title}')
  print(f'URL: {result.url}')
  print()
