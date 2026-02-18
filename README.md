# 🧠 Code Comment Generator (Inline)

> Automatically generate clean inline `#` comments for Python functions  
> Powered by **Qwen2.5-Coder** and built with **Streamlit**

---

## 🚀 Overview

This AI-powered web application allows you to paste any Python function  
and receive the same function enhanced with meaningful inline comments —  
without changing logic, variable names, or structure.

---

## ✨ Features

- 📝 Paste any Python function
- 💬 Adds inline `#` comments only
- 🧠 Powered by Qwen2.5-Coder models
- 🎛 Adjustable temperature & token settings
- 💾 Download as `.py` file
- ⚡ Clean, interactive Streamlit interface
- 🖥 Works on CPU or GPU

---

## 🏗 Tech Stack

- Python
- Streamlit
- HuggingFace Transformers
- PyTorch
- Qwen2.5-Coder (0.5B / 1.5B)

---

## 📂 Project Structure

code-comment-generator/
│
├── app.py
├── README.md
└── requirements.txt


---

# ⚙ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/VivekanandVivek/code-comment-generator.git
cd code-comment-generator
2️⃣ Create Virtual Environment
python -m venv venv
Activate Environment
Windows

venv\Scripts\activate
Mac/Linux

source venv/bin/activate
3️⃣ Install Dependencies
pip install streamlit torch transformers accelerate
▶ Run the Application
streamlit run app.py
Open in browser:

http://localhost:8501
🧠 Supported Models
Available from sidebar:

Model	Description
Qwen2.5-Coder-0.5B	Fast & lightweight
Qwen2.5-Coder-1.5B	Higher quality comments
Models are loaded dynamically and cached for efficiency.

🧪 Example
🔹 Input
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
🔹 Output
def factorial(n):
    # Check if n equals 0 (base case)
    if n == 0:
        # Return 1 since factorial(0) = 1
        return 1
    # Multiply n with factorial of n-1 (recursive step)
    return n * factorial(n-1)
🖥 System Requirements
Model	CPU	GPU
0.5B	✅ Supported	Optional
1.5B	⚠ Slower	Recommended (6GB+ VRAM)
👨‍💻 Author
Vivekanand Pandey
M.Tech (AI) – IIT Patna
Focused on LLMs, Code Intelligence, and Generative AI

