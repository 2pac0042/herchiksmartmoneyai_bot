import telebot
from flask import Flask, request

TOKEN = '8040390729:AAEr0iktkA-6yLBrtgGOwxFR6QbA7gl4F4M'
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

# Стартовое сообщение
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Добро пожаловать в Herchik Smart Money AI бот 💸")

# Простой ответ на текст
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, f"Вы написали: {message.text}")

# Webhook обработка
@app.route('/', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return '', 200
    else:
        return '!', 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
