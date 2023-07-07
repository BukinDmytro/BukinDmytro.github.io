#----------6 урок----------
'''
import telebot
from telebot import types
from currency_converter import CurrencyConverter
bot = telebot.TeleBot("6071701883:AAECUyH0Q_H5Lz8JXy7icD6t7UMoD4uI-m0")
currency = CurrencyConverter()
amount = 0

@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, "Привіт ! Введи суму: ")
    bot.register_next_step_handler(message,summa)

def summa(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id , "Неправильний формат.Напишіть суму")
        bot.register_next_step_handler(message,summa)
        return

    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width = 2)
        btn1 = types.InlineKeyboardButton('USD/EUR' , callback_data = 'usd/eur')
        btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
        btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp')
        btn4 = types.InlineKeyboardButton('Інше значення', callback_data='else')
        markup.add(btn1,btn2,btn3,btn4)
        bot.send_message(message.chat.id , "Виберіть пару валют" , reply_markup = markup)
    else:
        bot.send_message(message.chat.id , "Число повинно бути більше за 0.Спробуйте ще раз.")
        bot.register_next_step_handler(message,summa)



@bot.callback_query_handler(func = lambda call: True)

def callback(call):
    if call.data != "else":
        values = call.data.upper().split('/')
        res = currency.convert(amount , values[0] , values[1])
        bot.send_message(call.message.chat.id , f"Виходить {round(res,2)}.Можете вписати суму ще раз")
        bot.register_next_step_handler(call.message,summa)
    else:
        bot.send_message(call.message.chat.id , "Введіть пару значень через '/'")
        bot.register_next_step_handler(call.message,my_currency)

def my_currency(message):
    try:
        values = message.text.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(message.chat.id, f"Виходить {round(res, 2)}.Можете вписати суму ще раз")
        bot.register_next_step_handler(message, summa)
    except Exception:
        bot.send_message(message.chat.id , "Щось не так.Спробуйте ще раз написати значення через '/'")
        bot.register_next_step_handler(message,my_currency)


bot.polling(none_stop = True)
'''


#----------7 урок----------
'''
from aiogram import Bot,Dispatcher,executor,types

bot = Bot("6022646643:AAGw4v8vGcP4qTWPxFodACS_EAkrjAUip-k")
dp = Dispatcher(bot) #просто для коректної роботи бота

@dp.message_handler(commands = ['inline'])
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup(row_width = 2)
    markup.add(types.InlineKeyboardButton('Site' , url = 'https://chat.openai.com/'))
    markup.add(types.InlineKeyboardButton('Hello', callback_data ='hello'))
    await message.reply("Hello" , reply_markup = markup)


@dp.callback_query_handler()
async def callback(call):
    await call.message.answer("Дароу братік")



@dp.message_handler(commands = ['reply'])
async def reply(message: types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard = True)
    markup.add(types.KeyboardButton('Site'))
    markup.add(types.KeyboardButton('Website'))
    await message.reply("Hello" , reply_markup = markup)

executor.start_polling(dp)
'''


#----------8 урок----------

from aiogram import Bot,Dispatcher,executor,types
from aiogram.types.web_app_info import WebAppInfo
bot = Bot("6317035643:AAHvhjqengVgEuZM923qNnZMcZoqQlJ1Lhk")
dp = Dispatcher(bot)

@dp.message_handler(commands = ['start'])

async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Відкрити веб-сторінку" , web_app = WebAppInfo(url = "https://github.com/BukinDmytro/WebAppTelegram.git")))
    await message.answer("Привіт !", reply_markup = markup)


executor.start_polling(dp)

