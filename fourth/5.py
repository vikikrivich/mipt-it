import telebot
import re
from translate import Translator
import requests
from xml.etree import ElementTree as ET


# token = '8004104530:AAFFPWbo2rOb98rJ3wgRADAMfifsdemFkB4'
token = '' # place your token
bot = telebot.TeleBot(token)


def translate_word(s, lang):
    translator = Translator(to_lang=lang)
    return translator.translate(s)


def get_exchange_rate(currency_sym):
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    if currency_sym == '$':
        currency_type = 'USD'
    elif currency_sym == '₽':
        currency_type = 'RUB'
    else:
        return None

    try:
        res = requests.get(url)
        if res.status_code == 200:
            root = ET.fromstring(res.text)
            
            for valute in root.findall('Valute'):
                char_code = valute.find('CharCode').text
                if char_code == currency_type:
                    value = valute.find('Value').text
                    nominal = valute.find('Nominal').text
                    rate = float(value.replace(',', '.')) / float(nominal)
                    return rate
            
            print(f"{currency_type} hasn't found")
            return None
        else:
            print(res.status_code)
            return None
        
    except Exception as e:
        print(e)
        return None


def convert_currency(amount_s):
    amount = float(amount_s[1:])
    usd_rate = get_exchange_rate(amount_s[0])
    
    return amount * usd_rate


def get_weather(city_name):
    try:
        res = requests.get("https://raw.githubusercontent.com/pensnarik/russian-cities/master/russian-cities.json")
        cities = [city['name'] for city in res.json()]
        
        if city_name in cities:
            weather = requests.get(f"http://wttr.in/{city_name}?format=3").text
            return weather
        else:
            return "Город не найден в списке российских городов"
            
    except Exception as e:
        return f"Ошибка при получении погоды: {e}"


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    
    btn_translate = telebot.types.KeyboardButton('🔤 Перевод')
    btn_currency = telebot.types.KeyboardButton('💰 Валюта')
    btn_weather = telebot.types.KeyboardButton('🌤 Погода')
    btn_calc = telebot.types.KeyboardButton('🧮 Калькулятор')
    
    markup.add(btn_translate, btn_currency, btn_weather, btn_calc)
    
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == '💰 Валюта')
def currency_info(message):
    bot.send_message(message.chat.id, "Отправьте сумму в долларах ($100)")


@bot.message_handler(func=lambda message: message.text == '🧮 Калькулятор')
def calc_info(message):
    bot.send_message(message.chat.id, "Отправьте математическое выражение")


user_states = {}


@bot.message_handler(func=lambda message: message.text == '🔤 Перевод')
def translate_info(message):
    user_states[message.chat.id] = 'translate'
    bot.send_message(message.chat.id, "Отправьте текст для перевода")


@bot.message_handler(func=lambda message: message.text == '🌤 Погода')
def weather_info(message):
    user_states[message.chat.id] = 'weather'
    bot.send_message(message.chat.id, "Отправьте название города")


@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    text = message.text.strip()
    user_id = message.chat.id
    
    try:
        if not re.search('[a-zA-Zа-яА-Я]', text) and any(char in text for char in '+-*/**()'):
            result = eval(text)
            bot.reply_to(message, f"🧮 Результат: {result}")
            return
        
        if text.startswith('$') and text[1:].replace('.', '').replace(',', '').isdigit():
            amount = convert_currency(text)
            bot.reply_to(message, f"💱 {text} = {amount:.2f} ₽")
            return
        
        current_state = user_states.get(user_id)
        
        if current_state == 'weather':
            weather = get_weather(text)
            bot.reply_to(message, f"🌤 {weather}")
            user_states[user_id] = None
            
        elif current_state == 'translate':
            english_pattern = r'[a-zA-Z]'
            russian_pattern = r'[а-яА-ЯёЁ]'
            en_count = len(re.findall(english_pattern, text))
            ru_count = len(re.findall(russian_pattern, text))

            if en_count > ru_count:
                res = translate_word(text, 'ru')
            else:
                res = translate_word(text, 'en')
                
            bot.reply_to(message, f"🔤 {res}")
            user_states[user_id] = None
            
        else:
            english_pattern = r'[a-zA-Z]'
            russian_pattern = r'[а-яА-ЯёЁ]'
            en_count = len(re.findall(english_pattern, text))
            ru_count = len(re.findall(russian_pattern, text))

            if en_count > ru_count:
                res = translate_word(text, 'ru')
            else:
                res = translate_word(text, 'en')
                
            bot.reply_to(message, f"🔤 {res}")

    except Exception as e:
        bot.reply_to(message, f"❌ Ошибка: {e}")
        user_states[user_id] = None


if __name__ == "__main__":
    bot.infinity_polling()