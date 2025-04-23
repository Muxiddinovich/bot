from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

# Muhit o'zgaruvchilari orqali token va chat ID olish (xavfsizroq usul)

BOT_TOKEN = '7756613979:AAFac7xtNc8G1E9cQm31xOLYxWJlDtQMp0A'
CHAT_ID = '7926224444'  # Adminning chat ID'si

def send_to_telegram(phone, lat, lon):
    if not BOT_TOKEN or not CHAT_ID:
        print("❌ BOT_TOKEN yoki CHAT_ID topilmadi.")
        return

    text = f"📱 Raqam: {phone}\n📍 Lokatsiya: https://maps.google.com/?q={lat},{lon}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': text}
    requests.post(url, json=payload)

@app.route('/send-location', methods=['POST'])
def send_location():
    data = request.get_json()

    if not all(k in data for k in ('phone_number', 'latitude', 'longitude')):
        return jsonify({'status': 'error', 'message': 'Missing data'}), 400

    send_to_telegram(data['phone_number'], data['latitude'], data['longitude'])
    return jsonify({'status': 'success'})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
