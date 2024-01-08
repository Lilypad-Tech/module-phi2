from huggingface_hub import snapshot_download
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import argparse

# Set the default tensor type to float16 for mixed precision (reduces memory usage)
torch.set_default_dtype(torch.float16)

# Set the path to the model directory (update this path according to your Docker setup)
model_path = "/usr/src/app/model/models--amgadhasan--phi-2/snapshots/673ea632ab7f63050d40a457dba895ce92efb7ae"

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_path, trust_remote_code=True)

# Move model to GPU if CUDA is available
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# Text generation function
def generate(prompt: str, generation_params: dict = {"max_length": 200}) -> str:
    try:
        torch.cuda.empty_cache()  # Clear CUDA cache
        inputs = tokenizer(prompt, return_tensors="pt").to(device)
        outputs = model.generate(**inputs, **generation_params)
        completion = tokenizer.batch_decode(outputs)[0]
        return completion
    except Exception as e:
        return f"Error generating text: {str(e)}"

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate text from a prompt using a pretrained model.")
    parser.add_argument('prompt', type=str, help='A prompt for the model')
    args = parser.parse_args()

    # Generate and print the result
    result = generate(args.prompt)
    print(result)

if __name__ == "__main__":
    main()
