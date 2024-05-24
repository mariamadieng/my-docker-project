# Utiliser une image de base officielle
FROM python:3.8-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers du projet
COPY . .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port de l'application
EXPOSE 5000

# Commande pour exécuter l'application
CMD ["python", "app.py"]
