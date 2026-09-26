import os
import time
import requests
import openai
from flask import Flask
import threading

# Configuration du serveur web pour Render
app = Flask('')

@app.route('/')
def home():
    return "Bot SMC actif !"

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

threading.Thread(target=run, daemon=True).start()

# --- Ton code Bot SMC ---
TELEGRAM_BOT_TOKEN = "8871773633:AAFyDMKUmvfK7-N..." # Garde ta clé complète
TELEGRAM_CHAT_ID = "7113565313"
OPENAI_API_KEY = "TA_CLE_OPENAI_ICI"

# Colle la suite de ton script original ici
