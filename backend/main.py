# backend/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from gemini import get_gemini_reply
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Gemini Chatbot API")

# Allow your frontend to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class ChatRequest(BaseModel):
    message: str

@app.get("/")
async def root():
    return {"status": "Server is running"}

@app.post("/chat")
async def chat_endpoint(payload: ChatRequest):
    user_message = payload.message
    try:
        reply = get_gemini_reply(user_message)
        return {"reply": reply}
    except Exception as e:
        # Return a proper JSON error
        return {"reply": f"❌ Gemini error: {str(e)}"}
