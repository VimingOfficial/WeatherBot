# WeatherBot :low_brightness:	
Daily weather updates are provided for selected cities through this Telegram bot. Fetches weather information at specific hours (6:00, 8:00, 10:00, and 12:00) and sends a report to all subscribed users at 5:30 AM. Users may also instantly get a weather report using the command [/report]. 

# Features :white_check_mark:
- Daily Weather Updates: Automatically sends weather reports to subscribed users every day at 5:30 AM.
- Customizable Cities: Currently set to specific cities in Iran, but can be modified to other cities.
- Specific Hours: Fetches weather information at exact times (6:00, 8:00, 10:00, and 12:00).
- Manual Report Command: Users can manually request the weather report using the /report command.
- Easy Subscription: Users can subscribe and unsubscribe using the /start and /stop commands.

# Installation :envelope_with_arrow:
### Prerequisites
- [Python](python.org) 3.8+
- Telegram Bot Token: Obtain it by creating a bot on [BotFather](t.me/BotFather).
- OpenWeather API Key: Sign up at [OpenWeather](https://openweathermap.org/) to get a free API key.
### Setup
1. **Clone the repository:**
   ```
   git clone https://github.com/VimingOfficial/WeatherBot.git
   cd WeatherBot
   ```
2. **Install the required Python packages:**

   ```
   pip install -r requirements.txt
   ```
   **or**
   
   ```
   pip install python-telegram-bot requests
   ```
3. **Replace 'TELEGRAM-BOT-TOKEN' and 'WEATHER-API' in weather.py with your actual Telegram bot token and OpenWeather API key.**

# Usage :desktop_computer:	
1. **Run the Bot:**

   ```
   python weather.py
   ```
   **on Linux servers**
   
   ```
   nohup python3 weather.py &
   ```
   > [!NOTE]
   > On Linux servers you can use this line to keep it running
2. **Commands:**
- /start: Subscribe to daily weather updates at 5:30 AM.
- /stop: Unsubscribe from daily weather updates.
- /report: Get an instant weather report with the latest data for the specified hours.
3. **Output:**
- The bot will send daily reports for each city at 5:30 AM.
- Each report contains weather data at 6:00, 8:00, 10:00, and 12:00 for each city.

# Customization :memo:
- **Change Cities:** Modify the cities list in weather.py to add or change the cities.
- **Adjust Report Times:** Modify the specific_hours list to specify different hours for weather reports.
- **Change Report Time:** Adjust the time in run_scheduler if you need the report at a different time than 5:30 AM.

# Example Output :arrow_forward:	
 Weather Report (YYYY-MM-DD)

 At 6:00:
- Tehran: Clear sky, 18°C
- Mashhad: Partly cloudy, 15°C

 At 8:00:
- Tehran: Sunny, 20°C
- Mashhad: Overcast, 16°C

 At 10:00:
- Tehran: Warm, 22°C
- Mashhad: Clear, 18°C

 At 12:00:
- Tehran: Sunny, 24°C
- Mashhad: Warm, 20°C

