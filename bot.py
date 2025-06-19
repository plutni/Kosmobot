import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '6339993059:AAH-fUrMpwps4UucVRrJpByL96zYj4RLd1s' 

bot = telebot.TeleBot(TOKEN)

# Ключевые слова и ссылки на прайсы
PRICE_LINKS = {
    "iphone": (" Apple (новые)", "https://t.me/Kosmoscaseprice/17"),
    "apple": (" Б/У Apple и другие", "https://t.me/Kosmoscaseprice/18"),
    "samsung": ("💙 Samsung", "https://t.me/Kosmoscaseprice/3"),
    "pixel": ("🤍 Google Pixel", "https://t.me/Kosmoscaseprice/14"),
    "xiaomi": ("🧡 Xiaomi", "https://t.me/Kosmoscaseprice/4"),
    "poco": ("💛 Poco", "https://t.me/Kosmoscaseprice/5"),
    "tecno": ("💙 Tecno", "https://t.me/Kosmoscaseprice/11"),
    "infinix": ("💚 Infinix", "https://t.me/Kosmoscaseprice/8"),
    "realme": ("💛 Realme", "https://t.me/Kosmoscaseprice/12"),
    "honor": ("💙 Honor / Huawei", "https://t.me/Kosmoscaseprice/13"),
    "ноутбук": ("💻 Ноутбуки", "https://t.me/Kosmoscaseprice/19"),
    "планшет": ("📋 Планшеты", "https://t.me/Kosmoscaseprice/15"),
    "акустика": ("🎧 Акустика", "https://t.me/Kosmoscaseprice/28"),
    "часы": ("⌚️ Смарт часы", "https://t.me/Kosmoscaseprice/49"),
    "приставка": ("🎮 Консоли", "https://t.me/Kosmoscaseprice/32"),
    "телевизор": ("📺 ТВ, проекторы", "https://t.me/Kosmoscaseprice/53")
}

# Специальные ответы
SPECIAL = {
    "рассрочка": "📄 Условия рассрочки тут:\nhttps://t.me/kosmoscase/1407",
    "адрес": "🚀 Наш адрес:\nг. Кукмор, ул. Ленина 24к2\n\n🕘 Будни: 9:00–18:00\n🕓 Выходные и праздники: 9:00–16:00",
    "режим работы": "🚀 Наш адрес:\nг. Кукмор, ул. Ленина 24к2\n\n🕘 Будни: 9:00–18:00\n🕓 Выходные и праздники: 9:00–16:00"
}

# Ключевые слова для ремонта
REPAIR_KEYWORDS = ["ремонт", "сломался", "не включается", "разбил", "экран", "треснул", "уронил"]

@bot.message_handler(func=lambda m: True)
def handle_message(message):
    text = message.text.lower()

    # Проверка на спецкоманды
    for key in SPECIAL:
        if key in text:
            bot.send_message(message.chat.id, SPECIAL[key])
            return

    # Проверка на ремонт
    if any(word in text for word in REPAIR_KEYWORDS):
        bot.send_message(
            message.chat.id,
            "🔧 По вопросам ремонта лучше всего написать нашему менеджеру: @kosmoscas\n\n📱 Пожалуйста, укажите модель устройства и опишите проблему 🙏"
        )
        return

    # Проверка по брендам/категориям
    for keyword, (title, link) in PRICE_LINKS.items():
        if keyword in text:
            markup = InlineKeyboardMarkup()
            btn = InlineKeyboardButton(text="🔍 Открыть прайс", url=link)
            markup.add(btn)
            bot.send_message(message.chat.id, f"{title} доступен по кнопке ниже 👇", reply_markup=markup)
            return

    # Если ничего не найдено
    bot.send_message(message.chat.id, "🤖 Не совсем понял запрос. Уточните модель или напишите: 'iPhone', 'Samsung', 'рассрочка', 'ремонт' и т.п.")

# Запуск бота
bot.infinity_polling()
