import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import os

TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)

PRICE_LINKS = {
    "iphone": (" Apple (новые)", "https://t.me/Kosmoscaseprice/17"),
    "айфон": (" Apple (новые)", "https://t.me/Kosmoscaseprice/17"),
    "новый айфон": (" Apple (новые)", "https://t.me/Kosmoscaseprice/17"),
    "айфон новый": (" Apple (новые)", "https://t.me/Kosmoscaseprice/17"),
    "новый эпл": (" Apple (новые)", "https://t.me/Kosmoscaseprice/17"),
    "б/у айфон": ("БУ устройства 📱💻⌚️", "https://t.me/Kosmoscaseprice/18"),
    "айфон бу": ("БУ устройства 📱💻⌚️", "https://t.me/Kosmoscaseprice/18"),
    "айфон б/у": ("БУ устройства 📱💻⌚️", "https://t.me/Kosmoscaseprice/18"),
    "бушный айфон": ("БУ устройства 📱💻⌚️", "https://t.me/Kosmoscaseprice/18"),
    "подержанный айфон": ("БУ устройства 📱💻⌚️", "https://t.me/Kosmoscaseprice/18"),
    "б/у эпл": ("БУ устройства 📱💻⌚️", "https://t.me/Kosmoscaseprice/18"),
    "apple": ("БУ устройства 📱💻⌚️", "https://t.me/Kosmoscaseprice/18"),
    "эпл": ("БУ устройства 📱💻⌚️", "https://t.me/Kosmoscaseprice/18"),
    "samsung": ("Samsung 💙", "https://t.me/Kosmoscaseprice/3"),
    "самсунг": ("Samsung 💙", "https://t.me/Kosmoscaseprice/3"),
    "pixel": ("Google Pixel 🤍", "https://t.me/Kosmoscaseprice/14"),
    "пиксель": ("Google Pixel 🤍", "https://t.me/Kosmoscaseprice/14"),
    "xiaomi": ("Xiaomi 🧡", "https://t.me/Kosmoscaseprice/4"),
    "сяоми": ("Xiaomi 🧡", "https://t.me/Kosmoscaseprice/4"),
    "poco": ("Poco 💛", "https://t.me/Kosmoscaseprice/5"),
    "поко": ("Poco 💛", "https://t.me/Kosmoscaseprice/5"),
    "tecno": ("Tecno 💙", "https://t.me/Kosmoscaseprice/11"),
    "текно": ("Tecno 💙", "https://t.me/Kosmoscaseprice/11"),
    "infinix": ("Infinix 💚", "https://t.me/Kosmoscaseprice/8"),
    "инфиникс": ("Infinix 💚", "https://t.me/Kosmoscaseprice/8"),
    "realme": ("Realme 💛", "https://t.me/Kosmoscaseprice/12"),
    "риалми": ("Realme 💛", "https://t.me/Kosmoscaseprice/12"),
    "honor": ("Honor / Huawei 🩵", "https://t.me/Kosmoscaseprice/13"),
    "huawei": ("Honor / Huawei 🩵", "https://t.me/Kosmoscaseprice/13"),
    "ноутбук": ("Ноутбуки 💻", "https://t.me/Kosmoscaseprice/19"),
    "планшет": ("Планшеты 🎛️", "https://t.me/Kosmoscaseprice/15"),
    "акустика": ("Акустика 🎧🔊", "https://t.me/Kosmoscaseprice/28"),
    "алиса": ("Акустика 🎧🔊", "https://t.me/Kosmoscaseprice/28"),
    "яндекс": ("Акустика 🎧🔊", "https://t.me/Kosmoscaseprice/28"),
    "часы": ("Смарт часы ⌚️", "https://t.me/Kosmoscaseprice/49"),
    "умные часы": ("Смарт часы ⌚️", "https://t.me/Kosmoscaseprice/49"),
    "приставка": ("Игровые консоли 🎮", "https://t.me/Kosmoscaseprice/32"),
    "консоль": ("Игровые консоли 🎮", "https://t.me/Kosmoscaseprice/32"),
    "телевизор": ("ТВ 📺, проекторы 📽️ , 🤖ТВ", "https://t.me/Kosmoscaseprice/53"),
    "тв": ("ТВ 📺, проекторы 📽️ , 🤖ТВ", "https://t.me/Kosmoscaseprice/53")
}

SPECIAL = {
    "рассрочка": "📄 Условия рассрочки тут:\nhttps://t.me/kosmoscase/1407",
    "адрес": "📍 Наш адрес:
г. Кукмор, ул. Ленина 24к2
☎️ +79600420440

🕘 Будни: 9:00–18:00
🕓 Выходные и праздники: 9:00–16:00",
    "режим работы": "📍 Наш адрес:
г. Кукмор, ул. Ленина 24к2
☎️ +79600420440

🕘 Будни: 9:00–18:00
🕓 Выходные и праздники: 9:00–16:00"
}

REPAIR_KEYWORDS = ["ремонт", "сломался", "не включается", "разбил", "экран", "тупит", "утопил", "треснул", "заменить", "уронил"]

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        KeyboardButton("📱 Прайс по брендам"),
        KeyboardButton("🔧 Ремонт"),
        KeyboardButton("💳 Рассрочка"),
        KeyboardButton("📍 Адрес и режим")
    )
    bot.send_message(
        message.chat.id,
        "Привет 👋 Я *КосмоБот* — помогу с техникой и аксессуарами! 🚀

"
        "Выбирай, что интересует:",
        parse_mode="Markdown",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: message.text == "📱 Прайс по брендам")
def handle_price_button(message):
    bot.send_message(message.chat.id, "📲 Напиши название бренда: iPhone, Samsung, Poco, Realme и т.п.")

@bot.message_handler(func=lambda message: message.text == "🔧 Ремонт")
def handle_repair_button(message):
    bot.send_message(message.chat.id, "🔧 Напиши модель устройства и суть поломки — наш менеджер поможет!

📩 Связь: @kosmoscas")

@bot.message_handler(func=lambda message: message.text == "💳 Рассрочка")
def handle_credit_button(message):
    bot.send_message(message.chat.id, SPECIAL["рассрочка"])

@bot.message_handler(func=lambda message: message.text == "📍 Адрес и режим")
def handle_address_button(message):
    bot.send_message(message.chat.id, SPECIAL["адрес"])

@bot.message_handler(func=lambda m: True)
def handle_message(message):
    text = message.text.lower()

    for key in SPECIAL:
        if key in text:
            bot.send_message(message.chat.id, SPECIAL[key])
            return

    if any(word in text for word in REPAIR_KEYWORDS):
        bot.send_message(
            message.chat.id,
            "🔧 По вопросам ремонта лучше всего написать нашему менеджеру: @kosmoscas

📱 Пожалуйста, укажите модель устройства и опишите проблему 🙏"
        )
        return

    for keyword, (title, link) in PRICE_LINKS.items():
        if keyword in text:
            markup = InlineKeyboardMarkup()
            btn = InlineKeyboardButton(text=title, url=link)
            markup.add(btn)
            bot.send_message(
                message.chat.id,
                "📦 Наличие и цены по кнопке ниже 👇",
                reply_markup=markup
            )
            return

    bot.send_message(message.chat.id, "🤖 Не совсем понял запрос. Напиши, например: iPhone, Poco, ремонт, рассрочка и т.п.")

bot.infinity_polling()
