import logging, os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = os.getenv("API_TOKEN")
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

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

@dp.message_handler(lambda m: "рассрочка" in m.text.lower())
async def inst(m: types.Message):
    await m.reply("Рассрочка от 6 до 36 месяцев 👇\nhttps://t.me/kosmoscase/1407")

@dp.message_handler(lambda m: "ремонт" in m.text.lower())
async def rep(m: types.Message):
    await m.reply("📱 Укажите модель и проблему.\nДля консультации: https://t.me/kosmoscas")

@dp.message_handler(lambda m: any(k in m.text.lower() for k in brand_links))
async def brands(m: types.Message):
    txt = m.text.lower()
    for key, link in brand_links.items():
        if key in txt:
            await m.reply(f"📦 Актуальные предложения по «{key}»: {link}")
            return

@dp.message_handler()
async def fallback(m: types.Message):
    await m.reply("🤖 Напишите бренд, 'рассрочка' или 'ремонт'.")

if name == "__main__":
    executor.start_polling(dp, skip_updates=True)
