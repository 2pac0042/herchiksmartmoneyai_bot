from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    menu = [["💸 Купить доступ", "📈 Что умеет бот"], ["📞 Поддержка"]]
    reply_markup = ReplyKeyboardMarkup(menu, resize_keyboard=True)
    await update.message.reply_text(f"Привет, {user}! Я — умный бот по трейдингу Herchik Smart AI.", reply_markup=reply_markup)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📞 По всем вопросам: @forex0042")

async def access(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💸 Чтобы купить доступ:\n\n1 месяц — 99,000 сум\n3 месяца — 199,000 сум\nПожизненно — 499,000 сум\n\nОплатите на UzCard: 9860 6067 4467 5780 и напишите @forex0042")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("buy", access))

print("Бот запущен...")
app.run_polling()
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    keyboard = [["💳 Купить доступ", "📩 Поддержка"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(f"Привет, {user}! 👋 Добро пожаловать в умного бота по трейдингу.", reply_markup=reply_markup)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💬 По всем вопросам: @forex0042")

if name == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.run_polling()
