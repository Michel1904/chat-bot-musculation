import streamlit as st
import requests

# URL du backend FastAPI
API_URL = "http://backend:8000/ask"  # Remplace par l'endpoint réel de ton API

st.set_page_config(page_title="Chatbot Musculation", layout="wide")

# Initialisation de l'historique des messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Affichage des messages en bulles de discussion
st.markdown("<h2 style='text-align: center;'>💪 Chatbot Musculation</h2>", unsafe_allow_html=True)
chat_container = st.container()

with chat_container:
    for message in st.session_state.messages:
        with st.chat_message("user" if message["role"] == "user" else "assistant"):
            st.markdown(message["content"])

# Zone de saisie de texte
user_input = st.chat_input("Pose-moi une question sur la musculation...")

if user_input:
    # Ajouter le message utilisateur à l'historique
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Envoyer la requête au backend FastAPI
    response = requests.post(API_URL, json={"question": user_input})

    if response.status_code == 200:
        bot_reply = response.json().get("response", "Désolé, je n'ai pas compris.")
    else:
        bot_reply = "Erreur de communication avec le serveur."

    # Ajouter la réponse du bot à l'historique
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    # Affichage des messages mis à jour
    with chat_container:
        with st.chat_message("assistant"):
            st.markdown(bot_reply)
