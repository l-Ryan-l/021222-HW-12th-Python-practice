import datetime
from spy import *


async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Наконец-то ты очнулся, {update.effective_user.first_name}!')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hello - Приветствие;\n/help - Список доступных команд;\n'
                                    f'/time - Точное время и дата;\n'
                                    f'/sum - Сумма двух чисел.\n    • Формат ввода: "/sum число-х число-у";\n'
                                    f'/dif - Разность двух чисел.\n    • Формат ввода: "/dif число-х число-у";\n'
                                    f'/mult - Произведение двух чисел.\n    • Формат ввода: "/mult число-х число-у";\n'
                                    f'/div - Деление двух чисел.\n    • Формат ввода: "/div число-х число-у";\n'
                                    f'/stat - Показать общее кол-во запросов в бот.')


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().strftime("%d-%m-%Y %H:%M")}')


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    res = ((x + y) / 100) * 100
    await update.message.reply_text(f'{x} + {y} = {res}')


async def dif_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x} - {y} = {x - y}')


async def mult_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    res = ((x * y) * 100) / 100
    await update.message.reply_text(f'{x} * {y} = {res}')


async def div_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    res = ((x / y) * 100)
    await update.message.reply_text(f'{x} / {y} = {int(res) / 100 }')
