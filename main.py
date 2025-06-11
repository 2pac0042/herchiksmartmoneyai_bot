from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
import logging
import os

API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("💎 Купить доступ"), KeyboardButton("📚 Курсы"))
    await message.reply("Добро пожаловать в Herchik Smart Money AI!", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "💎 Купить доступ")
async def buy_access(message: types.Message):
    await message.answer("Выберите тариф: \n1 месяц — 99,000 сум\n3 месяца — 199,000 сум\nПожизненно — 499,000 сум\n\n💳 Доступные оплаты:\n• Payme\n• Click\n• USDT (TRC20)")

@dp.message_handler(lambda message: message.text == "📚 Курсы")
async def send_courses(message: types.Message):
    await message.answer("🎓 Курсы в разработке. Скоро появятся видеоуроки!")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
