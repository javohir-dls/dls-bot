import logging
from telegram.ext import ApplicationBuilder
from flask import Flask
import threading

# Flask qismi (Render uchun kerak)
app = Flask(__name__)
@app.route('/')
def home():
    return "Bot ishlayapti!"

def run_flask():
    app.run(host='0.0.0.0', port=10000)

# Tokeningiz
TOKEN = "8877479664:AAFLQjuDtLcKvrWofQt2LftuGJMabV46hig"

if __name__ == '__main__':
    # Flaskni fonda ishga tushirish
    threading.Thread(target=run_flask).start()
    
    # Botingizni ishga tushirish
    application = ApplicationBuilder().token(TOKEN).build()
    print("Bot ishga tushdi!")
    aapplication.run_polling(drop_pending_updates=True)


