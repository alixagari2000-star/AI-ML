from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_path = "./gpt-oss-20b"  # Local model directory

# Check if CUDA is available
if not torch.cuda.is_available():
    raise SystemError("CUDA is not available. Make sure you have an NVIDIA GPU and the correct PyTorch installed.")

device = torch.device("cuda")

print("🔄 Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_path)

print("🔄 Loading model on GPU (this may take a while)...")
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype=torch.float16,      # Use FP16 for GPU (better performance)
    device_map="auto"               # Automatically spread model across GPUs (if multiple)
)

print("✅ Model loaded on GPU. Type 'exit' to quit.\n")

while True:
    prompt = input("You: ")
    if prompt.lower() in ["exit", "quit"]:
        break

    # Tokenize and move to GPU
    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=200,
            do_sample=True,
            temperature=0.7,
            top_p=0.9
        )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Optional: remove prompt from output
    if response.startswith(prompt):
        response = response[len(prompt):]

    print("Model:", response.strip())
