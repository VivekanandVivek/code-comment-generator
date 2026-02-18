# 🧠 Code Comment Generator (Inline)

Generate **inline comments for Python functions** using Large Language Models powered by **Qwen2.5-Coder** and Streamlit.

This application allows users to paste any Python function and automatically receive a version of the same code with meaningful inline comments added — without modifying the original logic.

---

## 🚀 Features

- 📝 Input any Python function
- 💬 Automatically generate inline `#` comments
- 🧠 Uses Qwen2.5-Coder (0.5B / 1.5B)
- 🎛 Adjustable generation settings (temperature, max tokens)
- 💾 Download commented code as `.py`
- ⚡ Clean and interactive Streamlit UI
- 🖥 Runs on CPU or GPU

---

## 🏗 Tech Stack

- Python
- Streamlit
- HuggingFace Transformers
- PyTorch
- Qwen2.5-Coder Models

---

## 📂 Project Structure

📦 code-comment-generator
┣ 📜 app.py
┣ 📜 README.md
┗ 📦 requirements.txt


---

## ⚙ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/VivekanandVivek/code-comment-generator.git
cd code-comment-generator

## 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv

## Activate the Environment

**Windows**
```bash
venv\Scripts\activate


**Mac/Linux**
```bash
source venv/bin/activate

## 3️⃣ Install Dependencies

```bash
pip install streamlit torch transformers accelerate


## ▶ Run the Application

```bash
streamlit run app.py


Then open in browser:
http://localhost:8501

### 🧠 Supported Models

Selectable from the sidebar:

- **Qwen/Qwen2.5-Coder-0.5B**  
  Fast and lightweight.

- **Qwen/Qwen2.5-Coder-1.5B**  
  Provides better inline comment quality.

Both models are loaded dynamically and cached for efficient performance.


### Example Input

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

### Example output

```python
def factorial(n):
    # Check if n is equal to 0 (base case)
    if n == 0:
        # Return 1 since factorial of 0 is 1
        return 1
    # Recursively multiply n by factorial of n-1
    return n * factorial(n-1)

### 🖥 System Requirements

| Model | CPU | GPU |
|--------|------|------|
| 0.5B | ✅ Works | Optional |
| 1.5B | ⚠ Slower | Recommended (6GB+ VRAM) |


### 👨‍💻 Author

**Vivekanand Pandey**  
M.Tech (AI) – IIT Patna  
Focused on LLMs, Code Intelligence, and Generative AI.


