# Rain Alert SMS 🌧️
An automated weather monitoring system that checks for rain in the next 12 hours and sends a SMS notification to your phone. This project is designed to run entirely on GitHub Actions, requiring no local server or manual execution.

## 🚀 Features
1. 12-Hour Forecast: Uses the OpenWeatherMap 5-day/3-hour forecast API to monitor the next four 3-hour windows.
2. Smart Filtering: Automatically identifies rain, snow, or storm conditions based on OpenWeatherMap condition codes (ID < 700).
3. Automated Scheduling: Runs daily at 7:00 AM IST via GitHub Actions cron scheduling.
4. Twilio Integration: Sends a direct SMS alert to your mobile device.

## 🛠️ Technical Stack
1. Language: Python 3.10
2. APIs: OpenWeatherMap API, Twilio API
3. Automation: GitHub Actions (Ubuntu Runner)
4. Libraries: requests, twilio

## 📁 Project StructurePlaintextpython-projects/rain-alert-SMS/
├── main.py              # Core logic for weather checking and SMS dispatch
├── requirements.txt      # Project dependencies (requests, twilio)
└── .github/workflows/    # GitHub Actions YAML configuration

## ⚙️ Setup & Configuration
1. Requirements
Ensure your requirements.txt includes:
    • requests
    • twilio
2. GitHub Secrets
To protect sensitive information, the script uses environment variables. You must add the following Repository Secrets in GitHub (Settings > Secrets and variables > Actions):

Secret Name             Description
WEATHER_API_KEY         Your OpenWeatherMap API Key
TWILIO_SID              Twilio Account SID
TWILIO_AUTH_TOKEN       Twilio Auth Token
VIRTUAL_TWILIO_NUMBER   Your assigned Twilio virtual number
VERIFIED_NUMBER         Your verified personal phone number

3. Automation Logic
The workflow is configured to trigger every morning:
    • Cron Schedule: 30 1 * * * (1:30 AM UTC / 7:00 AM IST).
    • Manual Trigger: Enabled via workflow_dispatch for testing purposes.

## 📝 How It Works
1. Fetch Data: The script calls the OpenWeatherMap endpoint for the specified Latitude and Longitude.
2. Analyze: It loops through the weather IDs. According to OpenWeatherMap Documentation, codes below 700 represent Rain, Drizzle, Snow, or Thunderstorms.
3. Notify: If will_rain is True, the Twilio Client is initialized, and an SMS is sent: "It's gonna rain 🌧️ today. Remember to bring an umbrella ☔"

## Resource links
1. Open Weather Map - https://openweathermap.org/
2. Twilio - https://www.twilio.com/en-us
3. HTTP Status codes - http://httpstatuses.com/
4. Requests (HTTP library for Python) Documentation - https://docs.python-requests.org/en/latest/
5. Latitude and longitude address tool - https://www.latlong.net/Show-Latitude-Longitude.html