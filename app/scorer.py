import os
import requests
import logging

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"
logger = logging.getLogger("uvicorn.error")

def evaluate_prompt(prompt: str) -> dict[str, str]:
    score = ''
    feedback = []
    
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "mistral-small",
        "messages": [
            {
                "role": "system",
                "content": "Rate out of 10, the score of this prompt on being properly prompt engineered for accurate responses without giving any other supporting text for your answer. It MUST have only the number"
            },
            {
                "role": "user",
                "content": prompt
			}
        ]
    }
    response = requests.post(MISTRAL_API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        result = response.json()
        score = result["choices"][0]["message"]["content"][:1]
        feedback = result["choices"][0]["message"]["content"][2:]
        
        print("Score: ", score)
        logger.info("Score: %s", score)
        print("Feedback: ", feedback)
        logger.info("Feedback: %s", feedback)
        
        return {"score": score, "feedback": feedback}
    return {"score": "NaN", "feedback": "Failed to get AI response."}

# def evaluate_prompt(prompt: str) -> Dict[str, int]:
#     score = 0
#     feedback = []

#     if len(prompt.strip()) >= 20:
#         score += 3
#     else:
#         feedback.append("Prompt is too short.")

#     if any(word in prompt.lower() for word in ["context", "background", "situation"]):
#         score += 3
#     else:
#         feedback.append("Context missing.")

#     if any(word in prompt.lower() for word in ["limit", "constraint", "within"]):
#         score += 3
#     else:
#         feedback.append("Constraints missing.")

#     if any(word in prompt.lower() for word in ["formal", "casual", "friendly", "professional"]):
#         score += 1

#     return {"score": score, "feedback": feedback}