import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Получаем токен из переменной окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Проверка на наличие токена
if not BOT_TOKEN:
    print("❌ BOT_TOKEN не задан в переменных окружения!")
    exit()

# Инициализация
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Кнопки главного меню
menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(KeyboardButton("💎 Купить доступ"))
menu.add(KeyboardButton("📚 Курсы"))

# Команда /start
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer("👋 Добро пожаловать в Herchik Smart Money AI!\nВыберите действие:", reply_markup=menu)

# Обработка кнопки "Купить доступ"
@dp.message_handler(lambda message: message.text == "💎 Купить доступ")
async def buy_access(message: types.Message):
    await message.answer(
        "💼 Тарифы:\n"
        "• 1 месяц — 99,000 сум\n"
        "• 3 месяца — 199,000 сум\n"
        "• Lifetime — 499,000 сум\n\n"
        "💳 Оплата: Click, Payme, USDT (TRC20)\n"
        "Для оплаты — напишите администратору: @forex0042"
    )

# Обработка кнопки "Курсы"
@dp.message_handler(lambda message: message.text == "📚 Курсы")
async def courses_handler(message: types.Message):
    await message.answer("🎓 Курсы пока недоступны. Следите за обновлениями!")

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
