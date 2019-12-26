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
    chat_ids = '😂'
    inter = '''Hola''' + chat_ids + ''', para tu comercio, asegúrate de que el @InterBanex esté disponible, antes de tipear tus monedas.

   ⚠️NOTA: Toda transacción tiene un costo del 1% del total de BANANO, NANO u otra moneda del @parjar_bot a comerciar, y ésta comisión debe pagarla el COMPRADOR en la moneda en cuestión.'''
    llamarinter = '/inter'


resp = requests.get('https://s3.amazonaws.com/dolartoday/data.json')
json.loads(resp.content)

    json_data = {
        "chat_id": chat_id,
        "text": message,
   }
    
    json_datad = {
        "chat_id": chat_id,
        "text": inter,
   }
    
    message_url = BOT_URL + 'sendMessage'
    if message == llamarinter:
        requests.post(message_url, json=json_datad, resp)
    else: 
        requests.post(message_url, json=json_data)
        
    return ''

if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
