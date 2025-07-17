# import requests
# import os
# from dotenv import load_dotenv

# load_dotenv()

# def rewrite_review(original_text):
#     url = "https://api.groq.com/openai/v1/chat/completions"
#     headers = {
#         "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
#         "Content-Type": "application/json"
#     }

#     payload = {
#         "model": "llama-3.3-70b-versatile",
#         "messages": [
#             {
#                 "role": "system",
#                 "content": (
#                     "You are a Review Rewriter Assistant. Rewrite the given customer review "
#                     "to make it clear, polished, and professional while preserving the original meaning. "
#                     "Return the review only."
#                 )
#             },
#             {
#                 "role": "user",
#                 "content": original_text
#             }
#         ]
#     }

#     response = requests.post(url, headers=headers, json=payload)

#     if response.status_code != 200:
#         raise Exception("Groq API error: " + response.text)

#     result = response.json()
#     return result.get("choices", [{}])[0].get("message", {}).get("content", "")


import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://router.huggingface.co/hf-inference/models/meta-llama/Llama-3.2-11B-Vision-Instruct/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {os.environ['HF_TOKEN']}",
}


def rewrite_review(original_text):
    prompt = (
        "You are a Review Rewriter Assistant. Rewrite the given customer review "
        "to make it clear, polished, and professional while preserving the original meaning.\n\n"
        f"Customer Review: {original_text}\n\n"
        "Rewritten Review:\n\n"
        "Return the review only."
    )

    payload = {
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": prompt
                },
            ]
        }
    ],
    "model": "meta-llama/Llama-3.2-11B-Vision-Instruct"
}

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception("Hugging Face API error: " + response.text)

    result = response.json()
    return result["choices"][0]["message"]["content"]