import requests
import os

API_KEY = os.getenv("GOOGLE_API_KEY")

MODEL = "models/gemini-2.5-flash"  # confirmed available
URL = f"https://generativelanguage.googleapis.com/v1/{MODEL}:generateContent?key={API_KEY}"

def get_gemini_reply(user_message: str) -> str:
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": user_message}
                ]
            }
        ]
    }

    response = requests.post(URL, json=payload)
    data = response.json()

    try:
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except Exception:
        return f"Error: {data}"
