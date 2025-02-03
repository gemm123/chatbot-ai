# Chatbot API for Message Completion Using FastAPI and GPT-2

## Introduction
This project is a chatbot API built using **FastAPI** and **GPT-2**. The chatbot is designed to generate and complete messages based on user input. It utilizes a **pre-trained transformer model** to predict the next words in a sentence, making it useful for text prediction and auto-completion applications.

## Features
- **FastAPI-based REST API** for chatbot interaction
- **GPT-2 model** for message completion

## Installation and Setup

### Cloning and Manual Setup
1. **Clone the repository** and navigate to the project directory:
   ```bash
   git clone <repository-url>
   cd chatbot-api
   ```

2. **Create a virtual environment** and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Run the FastAPI application:**
   ```bash
   uvicorn app.main:app --reload
   ```

4. **Access the API documentation** at:
   ```
   http://127.0.0.1:8000/docs
   ```

### Using Docker
1. **Build the Docker image:**
   ```bash
   docker build -t chatbot-api .
   ```

2. **Run the Docker container:**
   ```bash
   docker run -p 8000:8000 chatbot-api
   ```

3. **Access the API documentation** at:
   ```
   http://127.0.0.1:8000/docs
   ```

## API Usage
Send a **POST request** to the `/api/v1/chat` endpoint with the following JSON body:

```json
{
  "message": "Once upon a time in a mystical forest,"
}
```

The API will respond with a continuation of the message:

```json
{
  "response": "Once upon a time in a mystical forest, only one form could stand strong..."
}
```

