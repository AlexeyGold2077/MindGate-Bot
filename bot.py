import telebot
import mindgate_pywrapper
import _private
from telebot import types

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


@bot.message_handler(commands=['model'])
def command_model(message):
    mindgate_pywrapper.clearMessages(message.chat.id)
    bot.send_message(message.chat.id, "Вы не должны быть здесь...")


@bot.message_handler(commands=['settings'])
def command_settings(message):
    markup = types.InlineKeyboardMarkup()
    button_1 = types.InlineKeyboardButton('GPT-4', callback_data = 1)
    button_2 = types.InlineKeyboardButton('GPT-4-TURBO', callback_data = 2)
    button_3 = types.InlineKeyboardButton('GPT-4o' , callback_data = 3)

    for n in (button_1,button_2,button_3):
        markup.row(n)

    bot.send_message(message.chat.id, "Выберите версию нейросети".format(message.from_user), parse_mode = 'html', reply_markup=markup)



@bot.callback_query_handler(func=lambda callback: True)
def callback_model(call):
    if call.data == '123':
        markup = types.InlineKeyboardMarkup()
        button_1 = types.InlineKeyboardButton('GPT-4', callback_data = 1)
        button_2 = types.InlineKeyboardButton('GPT-4-TURBO', callback_data = 2)
        button_3 = types.InlineKeyboardButton('GPT-4o' , callback_data = 3)

        for n in (button_1,button_2,button_3):
            markup.row(n)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите версию нейросети'.format(call.message.from_user), reply_markup=markup)

    if call.data == '1':
        markup = types.InlineKeyboardMarkup()
        btn123 = types.InlineKeyboardButton('Назад', callback_data='123')
        markup.row(btn123)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Версия нейросети успешно установлена'.format(call.message.from_user), reply_markup=markup)
    
    elif call.data == '2':
        markup = types.InlineKeyboardMarkup()
        btn123 = types.InlineKeyboardButton('Назад', callback_data='123')
        markup.row(btn123)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Версия нейросети успешно установлена'.format(call.message.from_user), reply_markup=markup)
    
    elif call.data == '3':
        markup = types.InlineKeyboardMarkup()
        btn123 = types.InlineKeyboardButton('Назад', callback_data='123')
        markup.row(btn123)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Версия нейросети успешно установлена'.format(call.message.from_user), reply_markup=markup)


        

@bot.message_handler(content_types=['text'])
def respond_to_text(message):
    
    # mindgate_pywrapper.addBalance(message.chat.id, 10000)
    print(mindgate_pywrapper.getBalance(message.chat.id))
    user_message = message.text
    response = mindgate_pywrapper.sendMessageAsUser(message.chat.id, f'{user_message}')
    bot.send_message(message.chat.id,response["message"] + f'\n\n⛽️ {response["spent_tokens"]}', parse_mode="Markdown")
    print("\n\nid - " + str(message.chat.id))
    print("username - " + str(message.from_user.username))
    print("user - " + user_message)
    print("bot - " + response["message"])
    # if message.text == 'GPT-4':
    #     bot.send_message(message.chat.id, f'Версия GPT-4 успешно установлена')
    # elif message.text == 'GPT-4-TURBO':
    #     bot.send_message(message.chat.id, f'Версия GPT-4-TURBO успешно установлена')
    # elif message.text == 'GPT-4o':
    #     bot.send_message(message.chat.id, f'Версия GPT-4o успешно установлена')

bot.infinity_polling()