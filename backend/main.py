from fastapi import FastAPI
from pydantic import BaseModel
from gemini import get_gemini_reply

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"status": "ok", "message": "Gemini chatbot backend running"}

@app.post("/chat")
def chat(req: ChatRequest):
    reply = get_gemini_reply(req.message)
    return {"reply": reply}
