import logging
from telegram.ext import ApplicationBuilder

# Tokeningizni shu yerga yozing
TOKEN = "8877479664:AAFLQjuDtLcKvrWofQt2LftuGJMabV46hig"

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    print("Bot ishga tushdi!")
    application.run_polling()

