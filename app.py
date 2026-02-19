import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

st.set_page_config(
    page_title="Inline Code Comment Generator",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🧠 Code Comment Generator")
st.markdown("Generate inline comments for any Python function using Qwen Code LLM.")

# =========================
# Sidebar Model Selection
# =========================

st.sidebar.header("⚙ Model Settings")

model_option = st.sidebar.selectbox(
    "Choose Model",
    (
        "Qwen/Qwen2.5-Coder-0.5B",
        "Qwen/Qwen2.5-Coder-1.5B",
    )
)

temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.2)
max_tokens = st.sidebar.slider("Max New Tokens", 50, 400, 250)


# =========================
# Model Loader (Cached)
# =========================

@st.cache_resource
def load_model(model_name):
    device = "cuda" if torch.cuda.is_available() else "cpu"

    tokenizer = AutoTokenizer.from_pretrained(
        model_name,
        trust_remote_code=True
    )

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        trust_remote_code=True,
        dtype=torch.float16 if device == "cuda" else torch.float32
    )

    model.to(device)

    return tokenizer, model




# Load selected model
with st.spinner("🔄 Loading model... This may take a few seconds."):
    tokenizer, model = load_model(model_option)

model.eval()


# Main UI

code_input = st.text_area(
    "📝 Enter Python Code:",
    height=300,
    placeholder="def factorial(n):\n    if n == 0:\n        return 1\n    return n * factorial(n-1)"
)

col1, col2 = st.columns([1, 1])

if st.button("🚀 Generate Inline Comments"):

    if code_input.strip() == "":
        st.warning("Please enter Python code.")
    else:

        prompt = f"""
You are a strict Python code annotator.

Your job is to add exactly ONE inline comment for EVERY executable line.

Rules:
- Use ONLY '#' comments
- Add one comment ABOVE every non-empty line
- Do not skip any line
- Do not add docstrings
- Do not modify logic
- Do not rename variables
- Do not remove lines
- Return full code with added comments

Example:

Input:
def add(a, b):
    return a + b

Output:
# Define function add with parameters a and b
def add(a, b):
    # Return sum of a and b
    return a + b

Now annotate this code:

Input:
{code_input}

Output:
"""



        with st.spinner("🤖 Generating comments..."):
            device = "cuda" if torch.cuda.is_available() else "cpu"
            inputs = tokenizer(prompt, return_tensors="pt").to(device)


            with torch.no_grad():
                outputs = model.generate(
                    **inputs,
                    max_new_tokens=max_tokens,
                    temperature=0.0,
                    top_p=1.0,
                    do_sample=False
                )

            result = tokenizer.decode(outputs[0], skip_special_tokens=True)

            if "Output:" in result:
                commented_code = result.split("Output:")[-1].strip()
            else:
                commented_code = result.strip()


        st.subheader("✨ Commented Code:")
        st.code(commented_code, language="python")

        # Download Button
        st.download_button(
            label="⬇ Download Commented Code",
            data=commented_code,
            file_name="commented_code.py",
            mime="text/plain"
        )


# Footer

st.markdown("---")
st.markdown("Built with ❤️ using Qwen2.5-Coder and Streamlit")
