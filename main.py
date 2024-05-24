import os
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import requests

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer le jeton API depuis les variables d'environnement
GROQ_API_TOKEN = os.getenv('GROQ_API_TOKEN')

if not GROQ_API_TOKEN:
    raise ValueError("Le jeton API Grog n'est pas défini. Vérifiez votre fichier .env.")

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/grog-data")
def get_grog_data():
    url = "https://console.groq.com/keys"  # Remplacez par l'URL réelle de l'API Grog
    headers = {
        "Authorization": f"Bearer {GROQ_API_TOKEN}"
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Erreur lors de l'appel à l'API Grog")

    return response.json()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
