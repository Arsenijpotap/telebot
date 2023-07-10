import json
import telebot
from telebot import types
from bg import keep_alive

rzr = False

x = ''

# Токен бота
TOKEN = '6202973873:AAEZYdqqmj83pAbjV4hB6_zdFjqYO-yn5g8'

# Создание экземпляра бота
bot = telebot.TeleBot(TOKEN)


# Обработчик команды /start или нажатия на кнопку "Проверить"
@bot.message_handler(commands=['start'])
def handle(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("🎞️ Канал 🎞️",
                                         url='https://t.me/kinopoiskduo17')
    button2 = types.InlineKeyboardButton("✅ Проверить ✅", callback_data='check')
    markup.add(button1)
    markup.add(button2)
    global m_id
    m_id = int(message.chat.id)
    print(m_id)
    global msg
    check = bot.get_chat_member(-1001871291158, m_id)
    print(check.status)
    if check.status != "member" or check.status != 'creator' or check.status != 'administrator':
        msg = bot.send_message(
            message.chat.id,
            "Приветствую, я filmBot, я могу помочь вам отыскать нужный фильм🥁. Чтобы начать работу, подпишитесь на канал📸.",
            reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def inline(call):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("🎞️ Канал 🎞️",
                                         url='https://t.me/kinopoiskduo17')
    button2 = types.InlineKeyboardButton("✅ Проверить ✅", callback_data='check')
    markup.add(button1)
    markup.add(button2)

    if call.data == 'check':
        print(id)
    check = bot.get_chat_member(-1001871291158, m_id)
    if check.status == "member" or check.status == "creator" or check.status == 'administrator':
        # bot.delete_message(m_id,message.message_id-1)
        global x
        try:
            global rzr
            rzr = True
            bot.delete_message(m_id, msg.message_id)
            bot.send_message(
                m_id,
                'Проверка прошла успешно✔️. Спасибо за вашу поддержку🤝. Введите код нужного вам фильма.'
            )
        except:
            rzr = True
            bot.delete_message(m_id, x.message_id)
            bot.send_message(
                m_id,
                'Проверка прошла успешно✔️. Спасибо за вашу поддержку🤝. Введите код нужного вам фильма.'
            )
    else:
        try:
            bot.delete_message(m_id, msg.message_id)
            x = bot.send_message(
                m_id,
                'Вы не подписались на канал❌. Повторите попытку снова.',
                reply_markup=markup)
        except:
            print(111)
            bot.delete_message(m_id, x.message_id)
            x = bot.send_message(
                m_id,
                'Вы не подписались на канал❌. Повторите попытку снова.',
                reply_markup=markup)


@bot.message_handler(content_types=['text'])
def message(message):
    check = bot.get_chat_member(-1001871291158, message.chat.id)
    print(rzr)

    if check.status == "member" or check.status == "creator" or check.status == 'administrator':
        with open('spisok.json', 'r', encoding='utf-8') as fl:
            data = json.load(fl)

        sch = 0
        for item in data:
            for key in item:
                if not key == str(message.text):
                    sch += 1
                else:
                    bot.send_message(message.chat.id,
                                     f'Название фильма -  "{item[message.text]}".Приятного просмотра🌃.')
                    bot.send_message(1688488651, 'Кто то ищет фильм')
        if sch == len(data):
            bot.send_message(
                message.chat.id,
                'Извините, мы не смогли найти контент с таким кодом, убедитесь в правильности написания.'
            )
    else:
        handle(message)


keep_alive()
# Запуск бота
bot.polling(non_stop=True)

