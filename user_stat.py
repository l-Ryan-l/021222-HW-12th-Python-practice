from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def user_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    line_count = sum(1 for line in open('db.csv'))
    await update.message.reply_text(f'Всего обращений: {line_count}')

