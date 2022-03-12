import telebot
from telebot import types

bot = telebot.TeleBot('5263814202:AAHl_6QJUeHrhTL2AJV_9sgdbzk8yXZ75II')
@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

#@bot.message_handler(ommands_types=['text'])
#def get_user_text(message):
#   if message.text == "Hello":
#       bot.send_message(message.chat.id, "И тебе привет!", parse_mode='html')
#   elif message.text == "id":
#       bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')
#    elif message.text == "photo":
#        photo = open('icon.png', "rb")
#        bot.send_photo(message.chat.id, photo)
#    else:
#        bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode='html')
@bot.message_handler(commands_types=['photo'])

def get_user_photo(message):
    bot.send_message(message.chat.id, "Крутое фото!")

@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="https://AlexandrOstapenko.pythonanywhere.com"))
    bot.send_message(message.chat.id, "Перейдите на сайт", reply_markup=markup)

@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton("Веб сайт")
    start = types.KeyboardButton("Start")
    markup.add(website, start)
    bot.send_message(message.chat.id, "Перейдите на сайт", reply_markup=markup)



bot.polling(none_stop=True)