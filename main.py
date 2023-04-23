from random import choice
import telebot
from telebot import types

from core.config import TOKEN, IMAGE

# Название будушего диспечера
bot = telebot.TeleBot(TOKEN)


# message_handler - ожидает сообщение сообщение и если оно появися то отдает ответ
@bot.message_handler(commands=["start"]) 
def start(message):
    bot.send_message(message.chat.id, "Добро пожаловать в прилавку ITC-Шаверма")
    bot.send_photo(message.chat.id, open(choice(IMAGE), "rb"))
    # with open ("test/test.py", "w") as file:
    #     file.write(f"a = {message}")

@bot.message_handler(content_types=["text"])
def sen_user(message):
    # bot.send_message(massage.chat.id, massage.text)
    if message.text.lower() == "hello":
        bot.send_message(message.chat.id, f" hello hi{message.from_user.username}")
    elif message.text.lower() == "image":
        bot.send_photo(message.chat.id, open(choice(IMAGE), "rb"))

    else:
        bot.send_message(message.chat.id, f"я не понимаю сообщение {message.text}")


bot.polling(non_stop=True)