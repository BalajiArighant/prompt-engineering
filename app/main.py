from fastapi import FastAPI
from pydantic import BaseModel
from scorer import evaluate_prompt
from fastapi.middleware.cors import CORSMiddleware
import os
import requests
import logging

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"
logger = logging.getLogger("uvicorn.error")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    prompt: str

def get_ai_response(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "mistral-small",
        "messages": [
            {
                "role": "user",
                "content": prompt
			}
        ]
    }
    response = requests.post(MISTRAL_API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        result = response.json()
        logger.info("AI Response: %s", result["choices"][0]["message"]["content"])
        print(result["choices"][0]["message"]["content"])
        return result["choices"][0]["message"]["content"]
    return "Failed to get AI response."

@app.post("/evaluate")
async def evaluate(req: PromptRequest):
    eval_result = evaluate_prompt(req.prompt)
    ai_response = get_ai_response(req.prompt)
    return {
        "score": eval_result["score"],
        "feedback": eval_result["feedback"],
        "ai_response": ai_response
    }