# backend/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from gemini import get_gemini_reply  # your function to call the chatbot

app = FastAPI()

# Allow frontend to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for production, replace "*" with your frontend URL
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to Gemini Chatbot API!"}

@app.get("/chat")
def chat(message: str):
    try:
        reply = get_gemini_reply(message)
        return {"reply": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
