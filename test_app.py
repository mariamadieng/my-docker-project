from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_chat_endpoint():
    response = client.post("/chat", json={"invite": "Qu'est-ce qu'un LLM?"})
    assert response.status_code == 200
    # Ajoutez d'autres assertions basées sur la réponse attendue
