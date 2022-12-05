from bot_commands import *
from user_stat import *


app = ApplicationBuilder().token("your_token_here").build()
print('bot is working...')
app.add_handler(CommandHandler("hello", hello_command))
app.add_handler(CommandHandler('help', help_command))
app.add_handler(CommandHandler('time', time_command))
app.add_handler(CommandHandler('sum', sum_command))
app.add_handler(CommandHandler('dif', dif_command))
app.add_handler(CommandHandler('mult', mult_command))
app.add_handler(CommandHandler('div', div_command))
app.add_handler(CommandHandler('stat', user_stats))
app.run_polling()
