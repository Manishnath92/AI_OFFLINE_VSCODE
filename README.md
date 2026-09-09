# 🤖 AI Offline Assistant

A simple offline AI assistant built with Python and "llama-cpp-python", using a local Phi-2 GGUF model.

## ✨ Features

- Runs locally on your computer
- Works offline after setup
- Uses the `Phi-2 Q4_K_M GGUF` model
- Built with Python
- Uses `llama-cpp-python`
- Supports local memory

## 📋 Requirements

- Python 3.11
- llama-cpp-python 0.3.35
- Phi-2 Q4_K_M GGUF model
- VS Code (recommended)

## 🧠 AI Model

This project uses the Phi-2 Q4_K_M GGUF model.

[Download the model from Hugging Face](https://huggingface.co/codegood/phi-2-Q4_K_M-GGUF)

The model file used by this project is:

`phi-2.Q4_K_M.gguf`

> **Note:** The GGUF model is not included in this GitHub repository because of its large file size. Download it separately and place it in the project folder.»

## 🐍 Python

This project is developed and tested with Python 3.11.

[Download Python](https://www.python.org/downloads/)

Check your Python version:

```bash
python --version
```

Example:

Python 3.11.x

## 📦 llama-cpp-python

This project uses:

`llama-cpp-python`

Tested version:

`0.3.35`

[llama-cpp-python on GitHub](https://github.com/abetlen/llama-cpp-python)

[llama-cpp-python on PyPI](https://pypi.org/project/llama-cpp-python/)

Install it using:

```bash
python -m pip install llama-cpp-python
```

Check the installed version:
```bash
python -m pip show llama-cpp-python
```

You can test the installation with:
```bash
python -c "import llama_cpp; print('llama_cpp OK')"
```

Expected result:

`llama_cpp OK`

## 📁 Project Structure

The project should look like this on your computer:

```text  
AI_OFFLINE_VSCODE/
│
├── assistant.py
├── README.md
├── .gitignore
│
├── memory/
│   └── memory.json
│
└── phi-2.Q4_K_M.gguf
```

Important

These files are kept locally and are not uploaded to GitHub:

`phi-2.Q4_K_M.gguf`
`memory/memory.json`

The `.gitignore` file prevents these files from being uploaded.

## ⬇️ Setup

### Step 1 — Clone the Repository

Clone this GitHub repository:

```bash
git clone https://github.com/Manishnath92/AI_OFFLINE_VSCODE.git
```

Then enter the project folder:

`cd AI_OFFLINE_VSCODE`


### Step 2 — Check Python

Run:
```bash
python --version
```
Python 3.11 is recommended for this project.

### Step 3 — Install llama-cpp-python

Run:
```bash
python -m pip install llama-cpp-python
```
Then check the installation:
```bash
python -m pip show llama-cpp-python
```
### Step 4 — Download the AI Model

Download the model from Hugging Face:

[Phi-2 Q4_K_M GGUF](https://huggingface.co/codegood/phi-2-Q4_K_M-GGUF)

Download:

`phi-2.Q4_K_M.gguf`

Place the model file inside the project folder:

```text
AI_OFFLINE_VSCODE/
└── phi-2.Q4_K_M.gguf
```

### Step 5 — Run the Assistant

Open the project folder in VS Code.

`Open:`

`Terminal → New Terminal`

`Then run:`
```bash
python assistant.py
```
## 🛠️ VS Code Setup

If VS Code shows this error:
```text
Import "llama_cpp" could not be resolved
Pylance(reportMissingImports)
```
make sure VS Code is using the same Python environment where `llama-cpp-python` is installed.

Open the Command Palette:

`Ctrl + Shift + P`

**Search for:**
```text
Python: Select Interpreter
```
Select your Python 3.11 interpreter.

**Then check the package from the VS Code terminal:**
```bash
python -m pip show llama-cpp-python
```
If the package information appears, the package is installed in that Python environment.

**You can also test:**
```bash
python -c "import llama_cpp; print('llama_cpp OK')"
```
## ❗ Troubleshooting

Problem: ***"llama_cpp" cannot be imported***

**Install the package:**
```bash
python -m pip install llama-cpp-python
```
Then test:
```bash
python -c "import llama_cpp; print('llama_cpp OK')"
```
Problem: ***Python version is different***

Check:
```bash
python --version
```
If VS Code is using the wrong Python interpreter:

`Ctrl + Shift + P`
→ Python: Select Interpreter
→ Select Python 3.11

Problem: ***Model file not found***

Make sure the model file is named exactly:

`phi-2.Q4_K_M.gguf`

Also make sure it is placed in the location expected by `assistant.py`.

## 🔒 GitHub and .gitignore

The large AI model and local memory are intentionally excluded from GitHub.

The `.gitignore` contains rules such as:
```text
*.gguf
memory/memory.json
__pycache__/
*.pyc
.vscode/
```
This keeps the large model and local memory files out of the repository.

> **Security note:** Never upload API keys, passwords, tokens, or other private information to a public GitHub repository.»

## 🔄 Updating the Project

After making changes to the project, run these commands:
```bash
git status
```
```bash 
git add assistant.py
```
```bash
git commit -m "Update assistant"
```
```bash
git push
```

## 🔗 Useful Links

- [Python ](https://www.python.org/)
- [Python Downloads](https://www.python.org/downloads/)
- [llama-cpp-python on GitHub](https://github.com/abetlen/llama-cpp-python)
- [llama-cpp-python on PyPI](https://pypi.org/project/llama-cpp-python/)
- [Phi-2 Q4_K_M GGUF on Hugging Face](https://huggingface.co/codegood/phi-2-Q4_K_M-GGUF)

## 👨‍💻 Author

***Manish***

This is a learning project focused on:

- Python
- Local AI
- GGUF models
- "llama-cpp-python"
- Git and GitHub

## 🚧 Project Status

Development / Learning Project

This project is being developed and improved as part of learning about local AI and Python.
