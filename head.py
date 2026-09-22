from fastapi import FastAPI,HTTPException
from schema import Data
import requests
import uvicorn
import os
from dotenv import load_dotenv
load_dotenv()

# Auto-detect if running inside Docker by checking for the /.dockerenv file.
# If in Docker, replace 'localhost' with 'host.docker.internal' so the container
# can reach Ollama running on the host machine.
def get_ollama_url():
    base_url = os.getenv('ollama_url', 'http://localhost:11434/api/generate')
    if os.path.exists('/.dockerenv'):
        base_url = base_url.replace('localhost', 'host.docker.internal')
    return base_url

app = FastAPI()
@app.post('/correct')
def correct(data:Data)->str:
    url = get_ollama_url()
    payload = {
        'model':'llama3',
        'stream':False,
        'prompt':f"""
You are an expert English grammar correction assistant.

Your only task is to correct grammar, spelling, punctuation, capitalization, and subject-verb agreement.

Strict Rules:
1. Preserve the original meaning of the text.
2. Do NOT change facts, names, gender, people, places, numbers, or intent.
3. Do NOT rewrite, simplify, or improve the writing style.
4. Do NOT replace words with synonyms unless required for grammatical correctness.
5. Do NOT add or remove information.
6. Correct only grammatical mistakes.
7. If the input is already grammatically correct, return it unchanged.
8. Return only the corrected text.
9. Do not provide explanations, comments, notes, or formatting.
10. Follow correct English grammar and tense rules.

Examples:
Input:
we is happy today

Output:
We are happy today.

Input:
they was playing football

Output:
They were playing football.

Input:
she don't like coffee

Output:
She doesn't like coffee.

Input:
i has a car

Output:
I have a car.

Now correct the following text:

{data.text}
 
"""
    }

    response = requests.post(
        url,
        json = payload
    )

    if response.status_code!=200:
        raise HTTPException(
            status_code = response.status_code,
            detail = 'The request was not successfull'
            )
    result = response.json()
    res = result['response']

    return res

@app.get('/')
def hello():
    return {
        "message": "Welcome to the Grammar Corrector API!",
        "description": "This API uses the Llama 3 Large Language Model (LLM) through Ollama to automatically detect and correct grammatical errors in English text while preserving the original meaning.",
        "features": [
            "Corrects grammatical mistakes",
            "Fixes spelling errors",
            "Corrects punctuation",
            "Corrects capitalization",
            "Preserves the original meaning",
            "Does not add explanations",
            "Returns only the corrected text",
            "Powered by FastAPI and Ollama"
        ],
        "endpoints": {
            "POST /correct": "Submit English text and receive the grammatically corrected version."
        },
        "version": "1.0.0"
    }

if __name__ == '__main__':
    uvicorn.run(app,host = '0.0.0.0',port = 8002)

    
    












