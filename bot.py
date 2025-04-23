import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.enums import ParseMode

API_TOKEN = '7756613979:AAFac7xtNc8G1E9cQm31xOLYxWJlDtQMp0A'

# Logging sozlamalari
logging.basicConfig(level=logging.INFO)

# Bot va Dispatcher yaratamiz
bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

# /start komandasi
@dp.message(F.text == "/start")
async def send_welcome(message: Message):
    await message.answer("Hello! I'm your admin bot.")

# Matnli xabarlar uchun handler
@dp.message(F.text.startswith('Location:'))
async def handle_location_message(message: Message):
    text = message.text.split('\n')
    try:
        phone = text[0].split(': ')[1]
        latitude = text[1].split(': ')[1]
        longitude = text[2].split(': ')[1]
        await message.answer(f"Phone: {phone}\nLatitude: {latitude}\nLongitude: {longitude}")
    except IndexError:
        await message.answer("Xabar formati noto‘g‘ri. Format quyidagicha bo‘lishi kerak:\n"
                             "Location: PHONE_NUMBER\nLatitude: XX.XXXX\nLongitude: YY.YYYY")

# Botni ishga tushiramiz
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
