# inside main.py
from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware

# inside router.py
import os
import requests


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["ngrok-skip-browser-warning"] = '*'
    return response


@app.post('/posts/generate-ad-text')
def genenerate_ad():
    token = os.environ.get("TOKEN")

    headers = {
        'Authorization': "Bearer " + token
    }

    response = requests.post('https://7583-185-48-148-173.ngrok-free.app/custom-prompt', headers=headers, json={
        "input_text": "generate song text based on the following keywords: laptop, LENOVO, Intel Core i5, Nvidia, Windows 11"
    })

    body = response.json()
    return {
        "text": body['output']
    }