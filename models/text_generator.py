from llama_cpp import Llama

# Load the model (TinyLLaMA for speed in Codespaces)
llm = Llama(model_path="./models/tinyllama.gguf", n_ctx=2048)

def generate_text(prompt: str, max_tokens=200):
    """Generate text from a given prompt."""
    output = llm(prompt=prompt, max_tokens=max_tokens)
    return output["choices"][0]["text"].strip()
