from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Sample data: expand later or connect DB
BIBLE_VERSES = {
    "john 3:16": "For God so loved the world that he gave his one and only Son...",
    "psalm 23": "The Lord is my shepherd, I shall not want..."
}

HYMNS = {
    "45": "Amazing Grace, how sweet the sound...",
    "100": "Great is Thy faithfulness..."
}

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get("Body", "").strip().lower()
    resp = MessagingResponse()
    msg = resp.message()

    if incoming_msg.startswith("verse"):
        verse_key = incoming_msg.replace("verse", "").strip()
        response_text = BIBLE_VERSES.get(verse_key, "Sorry, I don't have that verse.")
        msg.body(response_text)

    elif incoming_msg.startswith("hymn"):
        hymn_number = incoming_msg.replace("hymn", "").strip()
        response_text = HYMNS.get(hymn_number, "Sorry, I don't have that hymn.")
        msg.body(response_text)

    else:
        msg.body("Welcome! Send 'verse <book chapter:verse>' or 'hymn <number>' to get content.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
