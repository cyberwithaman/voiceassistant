import requests
from assistant.models import Message, Conversation

OLLAMA_URL = "http://localhost:11434"

def get_assistant_response(text, user=None, conversation=None, model_name="llama2"):
    # Optionally, add conversation context here
    payload = {
        "model": model_name,
        "prompt": text,
        "stream": False,
        "options": {
            "temperature": 0.7,  # Lower temperature for faster, more focused responses
            "top_p": 0.9,        # Nucleus sampling for faster generation
            "top_k": 40,         # Top-k sampling for faster generation
            "num_predict": 100,  # Limit response length for faster generation
            "repeat_penalty": 1.1,  # Prevent repetition
            "num_ctx": 512       # Smaller context window for faster processing
        }
    }
    try:
        r = requests.post(f"{OLLAMA_URL}/api/generate", json=payload, timeout=30)  # Reduced timeout
        r.raise_for_status()
        response = r.json()
        return response.get('response', '').strip()
    except Exception as e:
        print(f"Ollama error: {e}")
        return f"Error: {e}" 