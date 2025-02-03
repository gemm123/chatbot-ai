from transformers import AutoModelForQuestionAnswering, AutoTokenizer
import torch

class DistilBERT:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-distilled-squad")
        self.model = AutoModelForQuestionAnswering.from_pretrained("distilbert-base-uncased-distilled-squad")

    def answer_question(self, question: str, context: str) -> str:
        inputs = self.tokenizer.encode_plus(question, context, return_tensors="pt")

        with torch.no_grad():
            outputs = self.model(**inputs)
            start_logits = outputs.start_logits
            end_logits = outputs.end_logits

        start_index = torch.argmax(start_logits)
        end_index = torch.argmax(end_logits) + 1

        answer = self.tokenizer.convert_tokens_to_string(
            self.tokenizer.convert_ids_to_tokens(inputs["input_ids"][0][start_index:end_index])
        )

        return answer