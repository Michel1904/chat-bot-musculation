from fastapi import FastAPI
from pydantic import BaseModel
import os
import fitz  # PyMuPDF
from google import genai

client = genai.Client(api_key="AIzaSyCf1mb4wr8nq59kJFZ5LSbYPtV1n0muIEU")

app = FastAPI()

# Charger le texte des PDFs UNE SEULE FOIS
def extract_text_from_pdfs_in_folder(folder_path):
    all_text = ""
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            with fitz.open(pdf_path) as doc:
                for page in doc:
                    all_text += page.get_text("text") + "\n\n"
    return all_text.strip()

folder_path = "Dossier pdf"  # Remplace par ton dossier
context = extract_text_from_pdfs_in_folder(folder_path)

conversation_history = []

class QuestionRequest(BaseModel):
    question: str

def ask_gemini(question):
    global conversation_history

    # Ajouter la question à l'historique
    conversation_history.append(f"Utilisateur : {question}")

    # Garder uniquement les 5 derniers échanges
    if len(conversation_history) > 5:
        conversation_history.pop(0)

    # Construire le prompt avec l'historique des conversations
    history_text = "\n".join(conversation_history)

    prompt = (
        f"{context}\n\n"
        f"Ne mentionne pas le guide, réponds directement et ne sors pas du contexte. "
        f"Voici l'historique des dernières conversations pour contexte :\n\n"
        f"{history_text}\n\n"
        f"Question : {question}"
    )

    response = client.models.generate_content(model="gemini-2.0-flash", contents=[prompt])

    # Ajouter la réponse du chatbot à l'historique
    conversation_history.append(f"Chatbot : {response.text}")

    return response.text

@app.post("/ask")
def ask_question(request: QuestionRequest):
    response = ask_gemini(request.question)
    return {"response": response}
