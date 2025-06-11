from telegram import ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    menu = [["💳 Купить доступ", "📩 Что умеет бот"], ["📞 Поддержка"]]
    reply_markup = ReplyKeyboardMarkup(menu, resize_keyboard=True)
    await update.message.reply_text(f"Привет, {user}! Я — умный бот по трейдингу.", reply_markup=reply_markup)

async def help_command(update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📞 По всем вопросам: @forex0042")

async def доступ(update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💳 Чтобы скачать доступ:\n\n"
        "1 месяц — 99 000 сум\n"
        "3 месяца — 199 000 сум\n"
        "Lifetime — 499 000 сум\n\n"
        "🔗 Доступные способы оплаты:\n"
        "— UzCard/HUMO: 9860 6067 4467 5780\n"
        "— Click (QR): https://my.click.uz/clickp2p/CED5AE0EF20...\n"
        "— 💳 MasterCard/Visa: скоро\n\n"
        "После оплаты напишите: @forex0042"
    )

if name == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("доступ", доступ))  # <— зарегистрирована!

    app.run_polling()
