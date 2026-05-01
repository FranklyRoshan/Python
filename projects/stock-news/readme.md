# 📈 Stock Alert & News Aggregator
A Python-based automation tool that monitors stock price fluctuations and sends relevant news articles via SMS (Twilio) when significant market movements occur.

## 🚀 Features
1. Real-time Monitoring: Fetches daily closing prices using the Alpha Vantage API.
2. Volatility Logic: Automatically triggers news retrieval if a stock moves by more than 5% (customizable).
3. News Integration: Sources the latest headlines and summaries via NewsAPI.
4. Automated Alerts: Sends formatted SMS alerts directly to your phone using Twilio.
5. Serverless Execution: Fully automated using GitHub Actions on a daily schedule.

## 🛠️ Tech Stack
1. Language: Python 3.10+
2. APIs: Alpha Vantage, NewsAPI, Twilio
3. Automation: GitHub Actions
4. Libraries: requests, twilio

## 📋 Setup & Installation
1. Clone the Repository
Bash
git clone https://github.com/your-username/your-repo-name.git
cd python-projects/stock-news
2. Install Dependencies
Bash
pip install -r requirements.txt
3. Environment Variables
To run this locally, create a .env file or export the following variables:

    • STOCK_API_KEY: Your Alpha Vantage API key.
    • NEWS_API_KEY: Your NewsAPI key.
    • TWILIO_SID: Your Twilio Account SID.
    • TWILIO_AUTH_TOKEN: Your Twilio Auth Token.
    • VIRTUAL_TWILIO_NUMBER: Your purchased Twilio phone number.
    • VERIFIED_NUMBER: Your personal phone number (verified in Twilio).

## 🤖 GitHub Actions Configuration
This project is configured to run automatically via GitHub Actions. To get it working:
1. Go to your GitHub Repository Settings.
2. Navigate to Secrets and variables > Actions.
3. Add each of the variables listed in the Environment Variables section as Repository Secrets.
4. The workflow is scheduled to run at 01:30 UTC (Tuesday-Saturday), but you can trigger it manually from the Actions tab.

    📊 Example Output
    When a 5% swing is detected, you will receive an SMS like this:

    TSLA: 🔺7% > Headline: Tesla hits new production milestone in Q3.

    Brief: Tesla Inc. announced today that it has exceeded its quarterly delivery targets...

## 📜 License
This project is open-source and available under the MIT License.

## 💡 Futrue Plan for Potential Improvements 
[ ] Add support for multiple stock tickers.
[ ] Implement sentiment analysis on news headlines.
[ ] Transition from SMS to Email (SendGrid) for cost savings.