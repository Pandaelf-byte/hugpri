import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

class AnonymousAIApp:
    def __init__(self, model_name="anonymous-ai-model"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def generate_response(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(**inputs, max_length=100)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

if __name__ == "__main__":
    app = AnonymousAIApp()
    prompt = input("Enter your prompt: ")
    response = app.generate_response(prompt)
    print("Response:", response)