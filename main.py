import time
import requests
import openai

TELEGRAM_BOT_TOKEN = "8871773633:AAFyDMkUMvfK7-NMuU3d-m9h-dsmrsN9OtU"
TELEGRAM_CHAT_ID = "7113565313"

# Ta clé API OpenAI
OPENAI_API_KEY = "TA_CLE_OPENAI_ICI"

SYSTEM_PROMPT = """
Tu es l'Assistant Trading SMC personnel de l'utilisateur.
Lorsqu'une opportunité se présente, génère une alerte claire pour Telegram avec :
- Biais (ACHAT 🟢 / VENTE 🔴)
- Justification SMC (Sweep + FVG)
- Zone d'entrée (POI), SL et TP recommandés.
"""

def envoyer_alerte(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

print("Assistant SMC en ligne sur Render...")

# Message de bienvenue au lancement
envoyer_alerte("🚀 **Assistant SMC connecté et en cours d'exécution sur Render !**")

# Boucle principale
while True:
    time.sleep(60)
