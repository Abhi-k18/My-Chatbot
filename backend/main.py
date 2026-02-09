from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from gemini import get_gemini_reply

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(data: dict):
    reply = get_gemini_reply(data["message"])
    return {"reply": reply}
