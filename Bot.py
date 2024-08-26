import telebot
import mindgate_pywrapper

bot = telebot.TeleBot("7150230176:AAFr7PRwQvSH7Dkxc3PiXj9X0z1lK1GV2cY")

system_message = "Be brief"


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """🤙 Привет! Я ваш AI помощник. Чем могу помочь?""")
    mindgate_pywrapper.sendMessageAsSystem(message.chat.id, system_message)


@bot.message_handler(commands=['reset'])
def clearMessages(message):
    mindgate_pywrapper.clearMessages(message.chat.id)
    mindgate_pywrapper.sendMessageAsSystem(message.chat.id, system_message)
    bot.send_message(message.chat.id, "MEMORY_RESET_SUCCESSFUL")


@bot.message_handler(content_types=['text'])
def respond_to_message(message):
    user_message = message.text
    response = mindgate_pywrapper.sendMessageAsUser(message.chat.id, f"""{user_message}""")
    bot.send_message(message.chat.id, response, parse_mode="Markdown")
    print("\n\nid - " + str(message.chat.id))
    print("user - " + user_message)
    print("bot - " + response)


bot.infinity_polling()
