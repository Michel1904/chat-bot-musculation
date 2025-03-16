import streamlit as st
import requests

# Définir l'URL de l'API FastAPI
API_URL = "http://backend:8000/ask"

st.title("💬 Chatbot Musculation")

# Interface utilisateur
question = st.text_input("Posez votre question à propos de la musculation")

if question:
    # Envoyer la question au backend
    response = requests.post(API_URL, json={"question": question})
    if response.status_code == 200:
        chatbot_response = response.json().get("response")
        st.write("🤖 Réponse : " + chatbot_response)
    else:
        st.write("Erreur lors de la communication avec le serveur")
