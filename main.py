import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    menu = [["💳 Оплатить картой (HUMO)"], ["💸 Click (QR-код)"], ["📞 Поддержка"]]
    reply_markup = ReplyKeyboardMarkup(menu, resize_keyboard=True)
    await update.message.reply_text(f"Привет, {user}! Добро пожаловать в Herchik Smart AI 🤖", reply_markup=reply_markup)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Напиши @forex0042 по всем вопросам поддержки.")

async def access(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Чтобы получить доступ:\n\n1 месяц — 99,000 сум\n3 месяца — 199,000 сум\nLifetime — 499,000 сум\n\nОплати удобным способом и напиши @forex0042.")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("доступ", access))
    app.run_polling()

if name == '__main__':
    main()
