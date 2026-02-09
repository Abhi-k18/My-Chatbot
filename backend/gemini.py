import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise RuntimeError("GOOGLE_API_KEY not found in environment variables")

# Configure Gemini once
genai.configure(api_key=API_KEY)

# Use supported model
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_reply(message: str) -> str:
    try:
        response = model.generate_content(message)

        if not response or not response.text:
            return "⚠️ I didn't get a response from Gemini."

        return response.text.strip()

    except Exception as e:
        # Never crash FastAPI
        return f"❌ Gemini error: {str(e)}"
