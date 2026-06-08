DecodeLabs — Project: Rule-Based AI Chatbot
Batch 2026 | Built by AI Engineering Intern

What This Project Is?
A Rule-Based AI Chatbot built in pure Python.
No machine learning. No external libraries. No internet needed.
Uses a Hash Map (dictionary) + IPO Model architecture.

````markdown
## Project Structure

```text
decodelabs_project1/
│
├── main.py                    ← Entry point. Run this file to start.
│
├── bot/
│   ├── __init__.py            ← Makes bot/ a Python package
│   └── engine.py              ← Core logic: lookup, display, pipeline
│
├── utils/
│   ├── __init__.py            ← Makes utils/ a Python package
│   └── sanitizer.py           ← Cleans user input (lower + strip)
│
├── config/
│   ├── __init__.py            ← Makes config/ a Python package
│   └── knowledge_base.py      ← All responses + bot settings
````
```
```


**How To Run :-**

Step 1 — Make sure Python is installed
bashpython --version
# Should show Python 3.x.x
# If not installed: https://www.python.org/downloads/
Step 2 — Navigate to the project folder
bashcd decodelabs_project1

Step 3 — Run the chatbot
bashpython main.py
That's it. No pip install needed. Zero dependencies.

## How to use

```text
====================================================
   ARIA — DecodeLabs AI Chatbot v1.0.0
   Project 1 | Rule-Based Intelligence
   Type 'help' to see what I can do
   Type 'exit' or 'quit' to stop
====================================================

You: hello
ARIA: Hey there! I'm ARIA, DecodeLabs' AI Assistant.

You: what is ai
ARIA: AI is the simulation of human intelligence by machines...

You: help
ARIA: Ask me about: AI, ML, NLP, who I am, DecodeLabs...

You: joke
ARIA: Why do programmers prefer dark mode? Because light attracts bugs!

You: exit
ARIA: Session ended. Thanks for using ARIA!
```


## How to Add New Responses

Open `config/knowledge_base.py` and add a new key-value pair to the `RESPONSES` dictionary:

```python
RESPONSES = {
    # Existing responses...

    "what is python": (
        "Python is a high-level programming language "
        "known for its simplicity and use in AI/ML."
    ),
}
```

Save the file and run the chatbot again.

That's all — no other file needs to be modified.



#**Architecture :-**
````markdown
## Architecture

```text
USER INPUT
    |
input("You: ")          ← main.py — INPUT phase
    |
sanitize()              ← utils/sanitizer.py — normalize
    |
is_empty() check        ← bot/engine.py — guard
    |
is_exit_command()       ← bot/engine.py — exit check
    |
RESPONSES.get()         ← config/knowledge_base.py — PROCESS
    |
show_response()         ← bot/engine.py — OUTPUT
    |
loops back (while True)
````

```
```


## Key Concepts Used

| Concept                     | Where               | Why                                      |
| --------------------------- | ------------------- | ---------------------------------------- |
| Dictionary (Hash Map)       | `knowledge_base.py` | O(1) lookup — instant response retrieval |
| `.lower().strip()`          | `sanitizer.py`      | Normalizes user input                    |
| `.get(key, default)`        | `engine.py`         | Lookup with automatic fallback           |
| `while True` + `break`      | `main.py`           | Infinite chat loop with clean exit       |
| `if __name__ == "__main__"` | `main.py`           | Safe program entry point                 |
| Separation of Concerns      | All files           | Each module has a single responsibility  |
| f-strings                   | `engine.py`         | Clean and readable string formatting     |


## Tech Stack

* **Language:** Python 3.x
* **Libraries:** None (Pure Standard Library)
* **Database:** None (In-Memory Dictionary)
* **Framework:** None (Terminal Application)
* **APIs:** None
