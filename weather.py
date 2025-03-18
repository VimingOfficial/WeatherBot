import requests
from datetime import datetime, time
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Add your own bot token and openweathermap API
BOT_TOKEN = 'TELEGRAM-BOT-TOKEN'
API_KEY = 'OPENWEATHERMAP-API'

# Define the cities for which to fetch weather
cities = ["City1", "city2"]  # Replace with your chosen cities

# Function to fetch weather for a specific city
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        wind_speed = data["wind"]["speed"]
        return f"{city}: {weather_desc}, {temp}°C, {wind_speed}kph"
    else:
        return f"Could not retrieve weather data for {city}."

# Function to compile weather report
def get_weather_report():
    report = f"Weather Report ({datetime.now().strftime('%Y-%m-%d')})\n"
    for city in cities:
        report += get_weather(city) + "\n"
    return report

# Function to send the weather report
async def send_weather_report(context: ContextTypes.DEFAULT_TYPE):
    report = get_weather_report()
    for chat_id in subscribed_users:
        await context.bot.send_message(chat_id=chat_id, text=report)

# Set up a command to start receiving reports
subscribed_users = set()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if chat_id not in subscribed_users:
        subscribed_users.add(chat_id)
        await update.message.reply_text("You will receive daily weather updates at 5:30 AM.")
    else:
        await update.message.reply_text("You are already subscribed to daily weather updates.")

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if chat_id in subscribed_users:
        subscribed_users.remove(chat_id)
        await update.message.reply_text("You have unsubscribed from daily weather updates.")
    else:
        await update.message.reply_text("You are not subscribed.")

# New: Command to manually trigger weather report
async def report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    report_text = get_weather_report()
    await update.message.reply_text(report_text)

# Function to run scheduler in the background
def run_scheduler(application):
    job_queue = application.job_queue
    job_queue.run_daily(send_weather_report, time=time(hour=5, minute=30))

# Main function to set up and start the bot
def main():
    application = Application.builder().token(BOT_TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("stop", stop))
    application.add_handler(CommandHandler("report", report))  # Added report command

    # Start the daily job scheduler
    run_scheduler(application)

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
