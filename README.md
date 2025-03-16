
# Chatbot Musculation

## Description

Ce projet implémente un chatbot dédié à la musculation, utilisant un backend FastAPI et une interface frontend construite avec Streamlit. Le chatbot est capable de répondre à des questions sur la musculation et d'interagir avec l'utilisateur à propos de divers sujets liés à l'entraînement physique, en s'appuyant sur des textes extraits de documents PDF.

## Fonctionnalités

- **Réponse à des questions** : Le chatbot répond aux questions de l'utilisateur sur la musculation en utilisant un modèle d'IA.
- **Gestion d'informations** : Le chatbot est également capable de répondre à des informations ou des demandes non interrogatives.
- **Interface interactive** : L'interface utilisateur permet de dialoguer avec le chatbot via un chat avec des messages en bulles.
- **Historique des conversations** : Le chatbot garde un historique des 5 dernières interactions pour contextualiser ses réponses.

## Prérequis

Avant de commencer, vous devez avoir installé Docker et Docker Compose sur votre machine. Assurez-vous également d'avoir Python 3.x et les dépendances nécessaires.

## Installation

### 1. Clonez ce repository

```bash
git clone https://github.com/votre-utilisateur/chatbot-musculation.git
cd chatbot-musculation
```

### 2. Configuration des environnements

1. **Backend** : Le backend est une application FastAPI qui écoute sur le port 8000.
2. **Frontend** : Le frontend est une application Streamlit qui s'exécute sur le port 8501.
3. **Dépendances Docker** : Ce projet utilise Docker pour simplifier le déploiement de l'application.

### 3. Démarrer les conteneurs Docker

Dans le répertoire racine du projet, exécutez la commande suivante pour construire et démarrer les services backend et frontend :

```bash
docker-compose up --build
```

Cela construira les images Docker pour le frontend et le backend et démarrera les conteneurs correspondants.

### 4. Accéder à l'interface

Une fois les conteneurs démarrés, vous pouvez accéder à l'interface Streamlit en ouvrant votre navigateur à l'adresse suivante :

```bash
http://localhost:8501
```

Le chatbot devrait être opérationnel, et vous pouvez commencer à poser des questions ou fournir des informations sur la musculation.

## Structure du projet

```
chatbot-musculation/
│
├── backend/                 # Code backend FastAPI
│   ├── main.py              # Point d'entrée pour l'application FastAPI
│   └── ...                  # Autres fichiers nécessaires au backend
│
├── frontend/                # Code frontend Streamlit
│   ├── interface.py         # Code principal pour l'interface utilisateur
│   └── ...                  # Autres fichiers nécessaires au frontend
│
├── docker-compose.yml       # Configuration de Docker Compose
└── README.md                # Ce fichier README
```

## Backend - FastAPI

Le backend est développé avec FastAPI, qui fournit une API REST pour traiter les demandes de l'utilisateur. Lorsqu'une question est envoyée, le backend analyse la question, génère une réponse en utilisant un modèle d'IA (comme Gemini), puis renvoie cette réponse au frontend.

Le backend gère également l'historique des conversations pour mieux contextualiser les réponses.

## Frontend - Streamlit

L'interface utilisateur est construite avec Streamlit. Elle offre une interface conviviale de chat où l'utilisateur peut poser des questions ou entrer des informations liées à la musculation. Chaque message est affiché dans une bulle de chat, avec une distinction claire entre les messages de l'utilisateur et les réponses du chatbot.

## Personnalisation

- **API Key Gemini** : Assurez-vous d'avoir une clé API valide pour le modèle Gemini si vous utilisez un service tiers comme Google GenAI pour les réponses.
- **Fichiers PDF** : Le backend extrait les textes des fichiers PDF présents dans le dossier `Dossier pdf`. Vous pouvez personnaliser ce dossier pour inclure d'autres documents liés à la musculation.
- **Personnalisation des réponses** : Vous pouvez ajuster la logique des réponses dans le code backend pour mieux répondre à vos besoins.

## Déploiement

Le projet est conteneurisé avec Docker, ce qui permet de le déployer facilement dans différents environnements. Vous pouvez modifier le fichier `docker-compose.yml` pour personnaliser les ports ou l'environnement d'exécution.
