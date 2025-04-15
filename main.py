from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import requests as re
 
BOT_TOKEN = ''
WEATHER_API = ''
 
# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
     await update.message.reply_text("Hello! Send me a city name and I’ll show you the weather ☀️")
 
# Message handler (replies to any text)
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    url = f"http://api.openweathermap.org/data/2.5/weather?q={user_text}&appid={WEATHER_API}&units=metric"
    response = re.get(url)
    if response.status_code == 200:
        data = response.json()
        await update.message.reply_text(f"Country : {data["sys"]["country"]}, Weather : {data["weather"][0]["main"]}, Temp : {int(data["main"]["temp"])} °C")
    else:
        await update.message.reply_text("City not found.\nPlease enter a valid city.",)
 
# Main function to start the bot
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
 
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
 
    print("Bot is running...")
    app.run_polling()
 
if __name__ == '__main__':
    main()
