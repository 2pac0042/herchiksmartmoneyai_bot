from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    menu = [
        ["📥 Купить доступ", "📞 Поддержка"],
        ["💳 Оплатить через карту (MasterCard/Visa)"],
        ["💳 Оплатить через HUMO"]
    ]
    reply_markup = ReplyKeyboardMarkup(menu, resize_keyboard=True)
    await update.message.reply_text(
        f"Привет, {user}! Я — умный бот по трейдингу. Выберите действие ниже 👇",
        reply_markup=reply_markup
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📞 По всем вопросам: @forex0042")

async def access(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💼 Чтобы получить доступ:\n"
        "1 месяц — 99 000 сум\n"
        "3 месяца — 199 000 сум\n"
        "Пожизненно — 499 000 сум"
    )

async def pay_card(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💳 Оплатить через MasterCard/Visa:\n"
        "Скоро будет доступно..."
    )

async def pay_humo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💳 Чтобы оплатить через HUMO-карту:\n"
        "Переведите на карту: 9860 6067 4467 5780\n"
        "И отправьте скриншот в поддержку 👉 @forex0042"
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("доступ", access))
app.add_handler(CommandHandler("оплата", pay_card))
app.add_handler(CommandHandler("humo", pay_humo))

app.run_polling()
