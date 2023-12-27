import telebot
from telebot import types
from glucose import glucose_check, send_daily_graph

bot = telebot.TeleBot('YOUR API')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Уровень глюкозы')                  # Glucose Level
    btn2 = types.KeyboardButton('Дневной график')                   # Daily Graph
    markup.row(btn1, btn2)
    bot.send_message(message.chat.id,
                     f'Привет <b>{message.from_user.first_name}</b>! Добро пожаловать в бот для проверки сахара',
                     parse_mode='html', reply_markup=markup)


@bot.message_handler()
def info(message):
    sugar = glucose_check()
    if message.text == 'Уровень глюкозы':                          # Check normal or not value
        if sugar == 0.0:
            bot.send_message(message.chat.id, f'Возникла ошибка данных, попробуйте в другой раз!')
        if sugar <= 3.8:
            bot.send_message(message.chat.id, f'Значение сахара: <b>{sugar} mmol</b> ❌', parse_mode='html')
        if sugar >= 10.0:
            bot.send_message(message.chat.id, f'Значение сахара: <b>{sugar} mmol</b> ❌', parse_mode='html')
        else:
            bot.send_message(message.chat.id, f'Значение сахара: <b>{sugar} mmol</b> ✅', parse_mode='html')

    if message.text == 'Дневной график':
        send_daily_graph()
        file = open('./' + 'Graph.png', 'rb')
        bot.send_photo(message.chat.id, file)


bot.polling(none_stop=True)
