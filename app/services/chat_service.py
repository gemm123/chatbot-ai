from app.models.gpt2 import GPT2Model

async def generate_response(user_input: str) -> str:
    gpt2 = GPT2Model()
    response = gpt2.generate(user_input)

    return response