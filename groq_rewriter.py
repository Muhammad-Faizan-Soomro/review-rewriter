import requests
import os
from dotenv import load_dotenv

load_dotenv()

def rewrite_review(original_text):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a Review Rewriter Assistant. Rewrite the given customer review "
                    "to make it clear, polished, and professional while preserving the original meaning. "
                    "Return the review only."
                )
            },
            {
                "role": "user",
                "content": original_text
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception("Groq API error: " + response.text)

    result = response.json()
    return result.get("choices", [{}])[0].get("message", {}).get("content", "")