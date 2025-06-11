import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = "ТВОЙ_ТОКЕН_СЮДА"  # Замени на свой токен

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Клавиатура
main_menu = ReplyKeyboardMarkup(
    [
        ["📊 Индикатор", "🎓 Курсы"],
        ["💳 Оплата", "🌐 Язык"]
    ],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Добро пожаловать в Herchik Smart Money AI 💼\n\nВыберите действие:",
        reply_markup=main_menu
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📊 Индикатор":
        await update.message.reply_text("🔍 Доступ к индикатору будет выдан после оплаты.")
    elif text == "🎓 Курсы":
        await update.message.reply_text("🎓 Список платных курсов будет добавлен позже.")
    elif text == "💳 Оплата":
        await update.message.reply_text("💳 Доступные способы оплаты:\n1. Click\n2. Payme\n3. USDT\n\nОплата активирует доступ к продуктам.")
    elif text == "🌐 Язык":
        await update.message.reply_text("🌐 Функция выбора языка будет добавлена.")
    else:
        await update.message.reply_text("❓ Пожалуйста, выберите вариант из меню.")

if name == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()
