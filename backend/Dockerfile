# Utiliser l'image officielle de Python
FROM python:3.12.5

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de l'application dans le conteneur
COPY . /app

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port de FastAPI
EXPOSE 8000

# Lancer l'application FastAPI
CMD ["uvicorn", "chat:app", "--host", "0.0.0.0", "--port", "8000"]
