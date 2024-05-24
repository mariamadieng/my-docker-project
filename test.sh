#!/bin/bash

# Attendre que le conteneur soit prêt
sleep 5

# Tester l'endpoint /chat avec une requête POST
curl -X POST http://localhost:8000/chat \
-H "Content-Type: application/json" \
-d '{"invite": "Qu\'est-ce qu\'un LLM?"}'
