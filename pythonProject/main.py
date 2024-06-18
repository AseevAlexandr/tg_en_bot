import telebot
from telebot import types
import os
from dotenv import load_dotenv



load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN'))
my_chat_id = 5166911677


@bot.message_handler(commands=['start', 'привет'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_1 = types.KeyboardButton(text='записаться на занятие')
    button_2 = types.KeyboardButton(text='обо мне')
    keyboard.add(button_1, button_2)
    bot.send_message(message.chat.id, 'привет я бот-ассистент для записи на уроки английского. С чего начнём?', reply_markup=keyboard)


def send_requests(message):
    mes = f"новый ученик {message.text}"
    bot.send_message(my_chat_id, mes)
    bot.send_message(message.chat.id, 'запрос принят')


def info_tec(message):
    hello_word = 'Привет! Меня зовут Анастасия. Вот уже более 7 лет я помогаю ученикам разного возраста осваивать и усваивать английский язык. У меня 2 красных диплома по специальности Лингвистика, каждый год прохожу курсы повышения квалификации по методике преподавания иностранных языков. Мои ученики успешно сдают государственные и международные экзамены по английскому, не боятся говорить на английском и слушают иностранную музыку без субтитров. Если тебе нужна помощь в изучении английского, оставляй заявку на звнятие». See you soon 🌸'
    bot.send_message(message.chat.id,hello_word)


@bot.message_handler(content_types=['text'])
def repest_all_messages(message):
    if message.text.lower() == 'обо мне':
        info_tec(message)
    if message.text.lower() == 'записаться на занятие':
        bot.send_message(message.chat.id, 'укажите своё имя, какая дата и время вас интересует?')
        bot.register_next_step_handler(message, send_requests)


if __name__ == '__main__':
    bot.infinity_polling()



