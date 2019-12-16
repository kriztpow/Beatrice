import requests  
import os
from flask import Flask, request

BOT_URL = f'https://api.telegram.org/bot{os.environ["BOT_KEY"]}/'  # <-- add your telegram token as environment variable


app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():  
    data = request.json

    print(data)  # Comment to hide what Telegram is sending you
    chat_id = data['message']['chat']['id']
    message = data['message']['text']
    hola = 'mamamelabolanegra'
    message_urld = BOT_URL + 'sendMessage' + '?text=Pija'

    json_data = {
        "chat_id": chat_id,
        "text": message,
   }
    
    json_datad = {
        "chat_id": chat_id,
        "text": hola,
   }
    
    message_url = BOT_URL + 'sendMessage'
    requests.post(message_url, json=json_data)
    if message_url == message_urld:
        requests.post(message_url, jsond=json_datad)
    
    return ''

if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
