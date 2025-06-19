import os
import threading
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

from http.server import BaseHTTPRequestHandler, HTTPServer

# 👇 Фейковый сервер, чтобы Render "успокоился"
class KeepAliveHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Bot is running')

def run_fake_server():
    server = HTTPServer(('0.0.0.0', 10000), KeepAliveHandler)
    server.serve_forever()

threading.Thread(target=run_fake_server, daemon=True).start()

# 🔐 Бот
TOKEN = os.getenv("API_TOKEN")

brand_links = {
    "iphone": "https://t.me/Kosmoscaseprice/17",
    "айфон": "https://t.me/Kosmoscaseprice/17",
    "apple": "https://t.me/Kosmoscaseprice/17",
    "бу": "https://t.me/Kosmoscaseprice/18",
    "samsung": "https://t.me/Kosmoscaseprice/3",
    "pixel": "https://t.me/Kosmoscaseprice/14",
    "xiaomi": "https://t.me/Kosmoscaseprice/4",
    "poco": "https://t.me/Kosmoscaseprice/5",
    "tecno": "https://t.me/Kosmoscaseprice/11",
    "infinix": "https://t.me/Kosmoscaseprice/8",
    "realme": "https://t.me/Kosmoscaseprice/12",
    "honor": "https://t.me/Kosmoscaseprice/13",
    "huawei": "https://t.me/Kosmoscaseprice/13",
    "ноутбук": "https://t.me/Kosmoscaseprice/19",
    "планшет": "https://t.me/Kosmoscaseprice/15",
    "наушники": "https://t.me/Kosmoscaseprice/28",
    "колонка": "https://t.me/Kosmoscaseprice/28",
    "часы": "https://t.me/Kosmoscaseprice/49",
    "приставка": "https://t.me/Kosmoscaseprice/32",
    "телевизор": "https://t.me/Kosmoscaseprice/53",
    "проектор": "https://t.me/Kosmoscaseprice/53",
    "стик": "https://t.me/Kosmoscaseprice/53"
}

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "рассрочка" in text:
        await update.message.reply_text("💳 Рассрочка от 6 до 36 месяцев:\nhttps://t.me/kosmoscase/1407")
    elif "ремонт" in text:
        await update.message.reply_text("🔧 Укажите модель и проблему:\nhttps://t.me/kosmoscas")
    else:
        for key, link in brand_links.items():
            if key in text:
                await update.message.reply_text(f"📦 Актуальные предложения по «{key}»: {link}")
                return
        await update.message.reply_text("🤖 Напишите бренд, 'рассрочка' или 'ремонт'.")

if name == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
