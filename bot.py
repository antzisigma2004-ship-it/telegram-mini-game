import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Παίρνει το token και το URL από το Render environment
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
GAME_URL = os.environ.get("GAME_URL")

if not TELEGRAM_TOKEN or not GAME_URL:
    raise ValueError("Missing TELEGRAM_TOKEN or GAME_URL in environment variables!")

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🎮 Παίξε!", url=GAME_URL)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Καλώς ήρθες! Πάτησε το κουμπί για να παίξεις:", reply_markup=reply_markup)

# Main function για να τρέχει ο bot
def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
