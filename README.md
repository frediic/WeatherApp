Weather App

A weather app built with Python and Tkinter that fetches real-time weather data using the OpenWeatherMap API. The app displays the current weather, temperature, and condition icon for the selected city, along with a 5-day weather forecast.

Features
• Real-Time Weather Data: Get up-to-date weather information for any city.
• 5-Day Forecast: View a detailed weather forecast for the next five days, including temperature, condition icons, and dates.
• Search Functionality: Enter the name of a city to retrieve its weather data.
• Dynamic Weather Icons: Displays weather condition icons based on the forecast.

Technologies Used
• Python: Core programming language.
• Tkinter: GUI framework for creating the app interface.
• Pillow: For handling and resizing images.
• OpenWeatherMap API: For retrieving weather data.

Setup Instructions

Prerequisites 1. Install Python 3.8 or later. 2. Install the required Python libraries:

pip install requests pillow python-dotenv

Set Up the API Key 1. Sign up at OpenWeatherMap to get your free API key. 2. Create a .env file in the project root directory and add your API key:

WEATHER_API_KEY=your_openweathermap_api_key

How to Run 1. Navigate to the project directory:

cd WeatherWpp

    2.	Run the app:

python main.py

Project Structure

weather_app/
│
├── main.py
├── config.py
├── weather_api.py
├── FendUI/
│ ├── ui.py
│ ├── icons/
├── assets/
│ └── background1.jpg
├── .env
├── README.md

Features Explained

Current Weather
• Displays the current temperature, weather description, and condition icon for the selected city.

5-Day Forecast
• Provides a detailed 5-day weather forecast with:
• Dates for each day.
• Weather condition icons (clear, rain, snow).
• Temperature for each day.
• Forecast data is retrieved in 3-hour intervals but condensed into daily summaries.

Weather Icon Setup 1. Download weather condition icons from OpenWeatherMap. 2. Save them in the FendUI/icons/ folder. 3. Ensure the file names match OpenWeatherMap’s icon codes (01d.png, 02n.png...).
