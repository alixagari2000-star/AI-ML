from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_path = "./gpt-oss-20b"   # folder where you downloaded the model

# Always use CPU
device = torch.device("cpu")

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_path)

print("Loading model on CPU (this will take a while)...")
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype=torch.bfloat16,   # BF16 is usually better than FP16 on CPU
    device_map={"": "cpu"}        # force CPU
)

print("✅ Model loaded. Type 'exit' to quit.\n")

while True:
    prompt = input("You: ")
    if prompt.lower() in ["exit", "quit"]:
        break

    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    outputs = model.generate(
        **inputs,
        max_new_tokens=200,
        do_sample=True,
        temperature=0.7,
        top_p=0.9
    )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("Model:", response[len(prompt):].strip())
