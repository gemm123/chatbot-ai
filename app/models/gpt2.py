from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

class GPT2Model:
    def __init__(self):
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        self.model = GPT2LMHeadModel.from_pretrained("gpt2")

        self.device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
        self.model.to(self.device)

    def generate(self, text: str) -> str:
        input_ids = self.tokenizer.encode(text, return_tensors="pt").to(self.device)
        outputs = self.model.generate(
            input_ids,
            max_length=200,
            do_sample=True,
            temperature=1.2,
            top_k=40,
            top_p=0.95,
            repetition_penalty=1.1,
        )
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response