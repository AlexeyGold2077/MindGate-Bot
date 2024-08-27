import telebot
import mindgate_pywrapper
import _private

bot = telebot.TeleBot(_private.TOKEN_DEV)

SYSTEM_MESSAGE = "Be brief"


@bot.message_handler(commands=['start'])
def command_start(message):
    mindgate_pywrapper.sendMessageAsSystem(message.chat.id, SYSTEM_MESSAGE)
    bot.reply_to(message, '🤙 Привет! Я ваш AI помощник. Чем могу помочь?')


@bot.message_handler(commands=['reset'])
def command_reset(message):
    mindgate_pywrapper.clearMessages(message.chat.id)
    mindgate_pywrapper.sendMessageAsSystem(message.chat.id, SYSTEM_MESSAGE)
    bot.send_message(message.chat.id, "🫨 Память сброшена!")
    bot.reply_to(message, '🤙 Привет! Я ваш AI помощник. Чем могу помочь?')


@bot.message_handler(commands=['model'])
def command_model(message):
    mindgate_pywrapper.clearMessages(message.chat.id)
    bot.send_message(message.chat.id, "Вы не должны быть здесь...")


@bot.message_handler(content_types=['text'])
def respond_to_text(message):
    user_message = message.text
    response = mindgate_pywrapper.sendMessageAsUser(message.chat.id, f'{user_message}')
    bot.send_message(message.chat.id,
                     response["message"] + f'\n\n⛽️ {response["total_tokens"]}',
                     parse_mode="Markdown")

    print(response["total_tokens"], response["prompt_tokens"], response["completion_tokens"])

    print("\n\nid - " + str(message.chat.id))
    print("username - " + str(message.from_user.username))
    print("user - " + user_message)
    print("bot - " + response["message"])


bot.infinity_polling()
