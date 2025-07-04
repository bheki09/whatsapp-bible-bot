from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = "8155231562:AAHufu8A8q0UEExY0VpaA-wOLQ8ccyBudtQ"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

@app.route('/telegram', methods=['POST'])
def telegram_webhook():
    data = request.get_json()
    chat_id = data['message']['chat']['id']
    text = data['message'].get('text', '').lower()

    if 'john 3:16' in text:
        reply = "Here it is: For God so loved the world..."
    elif 'hymn 45' in text:
        reply = "Hymn 45: Blessed Assurance, Jesus is mine..."
    else:
        reply = "Sorry, I didn't understand. Try 'John 3:16' or 'hymn 45'."

    # Send the reply back
    requests.post(TELEGRAM_API_URL, json={
        'chat_id': chat_id,
        'text': reply
    })
    return "ok"

