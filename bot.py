from flask import Flask, send_from_directory
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext

import os

TOKEN = "8043190032:AAHINL38KOx4d2LX2_0B0XEJe_ke84tLvzM"
app = Flask(__name__)

# ----- Flask Route για το παιχνίδι -----
@app.route('/')
def serve_game():
    return send_from_directory("game", "index.html")

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory("game", path)

# ----- Telegram Bot -----
async def start(update: Update, context: CallbackContext):
    keyboard = [[InlineKeyboardButton("🎮 Παίξε!", url="https://your-domain.com/")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Καλώς ήρθες στο mini game μου!", reply_markup=reply_markup)

def run_bot():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == "__main__":
    # Τρέχει το Flask σε άλλο thread
    from threading import Thread
    Thread(target=lambda: app.run(host="0.0.0.0", port=5000)).start()
    run_bot()
