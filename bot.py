import requests  
import os
from flask import Flask, request

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, messagehandler
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


BOT_URL = f'https://api.telegram.org/bot{os.environ["BOT_KEY"]}/'  # <-- add your telegram token as environment variable


app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():  
    data = request.json

    print(data)  # Comment to hide what Telegram is sending you
    chat_id = data['message']['chat']['id']
    message = data['message']['text']
    inter = '''Hola, para tu comercio, asegúrate de que el @InterBanex esté disponible, antes de tipear tus monedas.

   ⚠️NOTA: Toda transacción tiene un costo del 1% del total de BANANO, NANO u otra moneda del @parjar_bot a comerciar, y ésta comisión debe pagarla el COMPRADOR en la moneda en cuestión.'''
    llamarinter = '/inter'

    json_data = {
        "chat_id": chat_id,
        "text": message,
   }
    
    json_datad = {
        "chat_id": chat_id,
        "text": inter,
   }
    
    json_dataw = {
        "chat_id": chat_id,
        "text": chat_id,
   }
    
    message_url = BOT_URL + 'sendMessage'
    if message == llamarinter:
        requests.post(message_url, json=json_datad)
    if message == llamarinter:
        requests.post(message_url, json=json_dataw)    
    else: 
        requests.post(message_url, json=json_data) 
        # Catch new_chat_member
def welcome(bot,update):
    msg = update.message
    chat_id = msg.chat.id
    bot.sendMessage(update.message.chat_id, "@%s \nWelcome!" % msg.new_chat_member.username)        
    
    return ''

if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
