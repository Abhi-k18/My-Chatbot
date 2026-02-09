# backend/gemini.py
import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# Use a valid Gemini model
MODEL_NAME = "models/gemini-2.5-flash"

BASE_URL = f"https://generativelanguage.googleapis.com/v1/{MODEL_NAME}:generateContent?key={API_KEY}"

def get_gemini_reply(user_input: str) -> str:
    payload = {
        "contents": [
            {"parts": [{"text": user_input}]}
        ]
    }

    response = requests.post(BASE_URL, json=payload)
    data = response.json()

    if "candidates" in data:
        return data["candidates"][0]["content"]["parts"][0]["text"]
    else:
        # Return the error JSON as string for debugging
        raise Exception(data)
