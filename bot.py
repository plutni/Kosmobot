import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TOKEN = os.getenv("API_TOKEN")

price_posts = {
    "айфон": 17,
    "iphone": 17,
    "apple": 17,
    "samsung": 3,
    "планшет": 15
}

repair_keywords = [
    "сломал", "разбил", "треснул", "не включается", "не работает",
    "экран", "не заряжается", "разбит", "вода", "утопил", "уронил", "не реагирует"
]

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    # 1. Ответ по фразам ремонта
    if any(word in text for word in repair_keywords):
        await update.message.reply_text(
            "🔧 Похоже, у Вас проблема с устройством.\n"
            "Пожалуйста, укажите модель и суть проблемы.\n"
            "Для консультации напишите нашему менеджеру: https://t.me/kosmoscas"
        )
        return

    # 2. Ответ с пересылкой прайса
    for key, msg_id in price_posts.items():
        if key in text:
            await context.bot.copy_message(
                chat_id=update.effective_chat.id,
                from_chat_id='@Kosmoscaseprice',
                message_id=msg_id
            )
            return

    # 3. Ответ по рассрочке
    if "рассрочка" in text:
        await update.message.reply_text("💳 Рассрочка от 6 до 36 месяцев:\nhttps://t.me/kosmoscase/1407")
        return

    # 4. Ответ по умолчанию
    await update.message.reply_text("🤖 Напишите интересующий бренд, 'рассрочка' или опишите проблему устройства.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
