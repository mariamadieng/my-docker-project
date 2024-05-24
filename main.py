from fastapi import FastAPI, HTTPException
import os
import requests

app = FastAPI()

GROQ_API_URL = "https://console.groq.com/keys"  # Remplacez par l'URL de l'API Groq réelle

@app.get("/")
def read_root():
    return {"message": "Welcome to the Groq API tester"}

@app.get("/test-groq-api")
def test_groq_api():
    token = os.getenv("GROQ_API_TOKEN")
    if not token:
        raise HTTPException(status_code=500, detail="GROQ_API_TOKEN not found in environment variables")

    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(GROQ_API_URL, headers=headers)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch data from Groq API")

    return response.json()