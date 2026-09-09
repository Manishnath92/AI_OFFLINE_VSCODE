🤖 AI Offline Assistant

A simple offline AI assistant built with Python and "llama-cpp-python", using a local Phi-2 GGUF model.

The AI model runs locally on your computer, so after the required files and Python packages are installed, the assistant can work without an internet connection.

---

✨ Features

- 🖥️ Runs locally on your computer
- 📴 Can work offline after setup
- 🧠 Uses the Phi-2 Q4_K_M GGUF model
- 🐍 Built with Python
- ⚡ Uses "llama-cpp-python" for running the GGUF model
- 💾 Local memory support
- 📁 Simple project structure

---

📋 Requirements

Before running the project, install:

- Python 3.11
- "llama-cpp-python"
- Phi-2 Q4_K_M GGUF model
- VS Code (recommended)

---

🐍 Python

This project is developed and tested with Python 3.11.

Download Python from the official Python website:

"Download Python" (https://www.python.org/downloads/)

«Note: Python 3.11.9 is not the latest Python 3.11 release anymore. Use a suitable Python 3.11 installation for this project.»

During Python installation on Windows, make sure to enable:

Add Python.exe to PATH

---

🧠 AI Model

This project uses:

Phi-2 Q4_K_M GGUF

Model:

"Download Phi-2 Q4_K_M GGUF from Hugging Face" (https://huggingface.co/codegood/phi-2-Q4_K_M-GGUF)

The model file used by this project is:

phi-2.Q4_K_M.gguf

The model is approximately 1.74 GB in size.

«⚠️ The model file is intentionally not included in this GitHub repository because it is large. Download it separately and place it in the project folder.»

---

📦 llama-cpp-python

This project uses:

llama-cpp-python

Installed/tested version:

0.3.35

Official project:

"llama-cpp-python on GitHub" (https://github.com/abetlen/llama-cpp-python)

PyPI:

"llama-cpp-python on PyPI" (https://pypi.org/project/llama-cpp-python/)

Install it with:

python -m pip install llama-cpp-python

Check the installed version:

python -m pip show llama-cpp-python

You can also test the import:

python -c "import llama_cpp; print('llama_cpp OK')"

Expected result:

llama_cpp OK

---

📁 Project Structure

The project should look like this on your computer:

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

Important

The following files are not uploaded to GitHub:

phi-2.Q4_K_M.gguf
memory/memory.json

The ".gitignore" file prevents them from being uploaded.

---

⬇️ Step 1 — Clone the Repository

Clone this GitHub repository:

git clone YOUR_REPOSITORY_URL

Then enter the project folder:

cd AI_OFFLINE_VSCODE

«Replace "YOUR_REPOSITORY_URL" with the URL of this GitHub repository.»

---

🐍 Step 2 — Check Python

Open the terminal inside the project folder and run:

python --version

You should see Python 3.11.x.

Example:

Python 3.11.x

---

📦 Step 3 — Install llama-cpp-python

Run:

python -m pip install llama-cpp-python

After installation, check:

python -m pip show llama-cpp-python

Example:

Name: llama_cpp_python
Version: 0.3.35

---

🧠 Step 4 — Download the AI Model

Open the model page:

"Phi-2 Q4_K_M GGUF" (https://huggingface.co/codegood/phi-2-Q4_K_M-GGUF)

Download:

phi-2.Q4_K_M.gguf

Place the downloaded file directly inside the project folder.

Your structure should then look like:

AI_OFFLINE_VSCODE/
│
├── assistant.py
├── README.md
├── .gitignore
├── phi-2.Q4_K_M.gguf
│
└── memory/
    └── memory.json

---

▶️ Step 5 — Run the Assistant

Open the project folder in VS Code.

Open the terminal:

Terminal → New Terminal

Then run:

python assistant.py

The assistant should start using the local GGUF model.

---

🛠️ VS Code Setup

If VS Code shows this error:

Import "llama_cpp" could not be resolved
Pylance(reportMissingImports)

make sure VS Code is using the same Python environment where "llama-cpp-python" is installed.

In VS Code:

Ctrl + Shift + P

Then select:

Python: Select Interpreter

Choose your Python 3.11 interpreter.

Then restart/reload VS Code.

You can verify the package from the VS Code terminal:

python -m pip show llama-cpp-python

---

❗ Troubleshooting

"llama_cpp" cannot be imported

Run:

python -m pip show llama-cpp-python

If the package is not found:

python -m pip install llama-cpp-python

Then test:

python -c "import llama_cpp; print('llama_cpp OK')"

---

Python version is wrong

Check:

python --version

If VS Code is using another Python installation:

Ctrl + Shift + P
→ Python: Select Interpreter
→ Select Python 3.11

---

Model file not found

Make sure this file exists:

phi-2.Q4_K_M.gguf

and is located where "assistant.py" expects it.

The filename must match the path used inside the Python code.

---

🔒 Files Excluded from GitHub

The project uses ".gitignore" to prevent large or local files from being uploaded.

Example:

*.gguf
memory/memory.json
__pycache__/
*.pyc
.vscode/

This means your local AI model and personal/local memory remain on your computer.

---

🔄 Updating the Project

If you modify "assistant.py":

git status

Then:

git add assistant.py

Commit your changes:

git commit -m "Update assistant"

Push them to GitHub:

git push

You do not need GitHub Desktop every time. Git Bash can be used for the complete Git workflow.

---

🔗 Useful Links

- "Python" (https://www.python.org/)
- "llama-cpp-python" (https://github.com/abetlen/llama-cpp-python)
- "llama-cpp-python on PyPI" (https://pypi.org/project/llama-cpp-python/)
- "Phi-2 Q4_K_M GGUF Model" (https://huggingface.co/codegood/phi-2-Q4_K_M-GGUF)
- "GitHub" (https://github.com/)

---

👨‍💻 Author

Manish

This project was created as an offline/local AI assistant project for learning Python, local AI, GGUF models, and Git/GitHub.

---

📜 License

This project can be updated with an appropriate license in the future.

The AI model has its own licensing and usage terms. Check the model page before redistributing the model.

---

⭐ Project Status

🚧 Development / Learning Project

This project is actively being improved and experimented with.
