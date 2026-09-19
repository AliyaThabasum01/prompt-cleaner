# ✨ Prompt Cleaner

A lightweight Python CLI tool that transforms a messy prompt into a simple structured format.

## Features

- Organizes unstructured prompts
- Separates context and task
- Adds an expected output section
- Simple CLI interface
- No external dependencies

## Run

```bash
python main.py
```

## Example

```text
Enter your messy prompt:
> create a python project that reads csv files and shows useful statistics

🧠 Cleaned Prompt
===================================

Goal: Complete the requested task.

Context:
create a python project that

Task:
reads csv files and shows useful statistics

Output:
Provide a clear and structured response.
```

## Built With

- Python
- String processing
