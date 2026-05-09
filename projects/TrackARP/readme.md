# TrackARP 🚄

A professional-grade Python automation tool designed to monitor the **IRCTC Advance Reservation Period (ARP)**. It dispatches proactive Email and SMS alerts exactly 24 hours before the 60-day booking window opens.

---

## 🛠️ Features
*   **Intelligent Scheduling**: Monitors travel dates 61 days out to provide a "heads-up" alert 1 day before booking starts.
*   **High-Signal Alerts**:
    *   **Email**: Comprehensive insights including primary booking times and a 9-day backup schedule.
    *   **SMS**: Ultra-concise Twilio notifications for immediate awareness.
*   **Future-Proof**: GitHub Actions workflow optimized for Node.js 24.

---

## 💻 Tech Stack
*   **Language**: Python 3.9+
*   **APIs**: Twilio (SMS), SMTPLIB (Email)
*   **Automation**: GitHub Actions (Cron: `30 1 * * *` / 07:00 AM IST)
*   **Security**: GitHub Secrets & `python-dotenv`

---

## 🚀 Setup

### 1. Environment Variables
Create a `.env` file for local testing (or add as **Secrets** in GitHub):
```env
MY_EMAIL=your_email@gmail.com
MY_EMAIL_PASSWORD=your_app_password
EMAIL_PROVIDER_SMTP_ADDRESS=://gmail.com
TWILIO_SID=your_sid
TWILIO_AUTH_TOKEN=your_token
VIRTUAL_TWILIO_NUMBER=+123456789
TWILIO_VERIFIED_NUMBER=+91987654321
```

### 2. Installation
```bash
pip install -r requirements.txt
```

### 3. Folder Structure
Maintain this structure to ensure GitHub Actions finds your script:
```text
├── .github/workflows/reminder.yml
└── projects/
    └── TrackARP/
        ├── TrackARP.py
        └── requirements.txt
```

---

## 📅 Automation Logic
*   **Target Day**: The script specifically tracks journeys falling on **Fridays**.
*   **Timing**: Alerts are dispatched at **07:00 AM IST**, providing a 1-hour lead time before the **08:00 AM IST** IRCTC window opens.

---

## 🚉 IRCTC Booking Windows & Times
*   **General Quota**: Opens **60 days** in advance (excluding travel date) at **08:00 AM**.
*   **Tatkal AC**: Opens 1 day before departure at **10:00 AM**.
*   **Tatkal Sleeper**: Opens 1 day before departure at **11:00 AM**.
*   **Current Booking**: Available after chart preparation until 30 mins before departure.

💡 **Pro-Tips**:
1.  **Master List**: Pre-save passenger details in your IRCTC profile to skip typing.
2.  **Fast Logins**: Log in 5 minutes before the window opens.
3.  **Payment**: Use **UPI** or **IRCTC iPay** for the fastest checkout.
4.  **Maintenance**: Note that IRCTC services are usually down from **11:45 PM to 12:20 AM IST**.

---

## 📝 Appendix: `strftime` Cheat Sheet

### 📅 Date (Day, Month, Year)
*   `%d`: Day of the month as a zero-padded decimal (01 to 31)
*   `%-d`: Day of the month as a decimal (1 to 31)
*   `%b`: Abbreviated month name (Jan)
*   `%B`: Full month name (January)
*   `%m`: Month as a zero-padded decimal (01 to 12)
*   `%y`: Year without century (26)
*   `%Y`: Year with century (2026)

### ⏰ Time (Hours, Minutes, Seconds)
*   `%H`: Hour (24-hour clock) (00 to 23)
*   `%I`: Hour (12-hour clock) (01 to 12)
*   `%p`: Locale’s equivalent of AM or PM
*   `%M`: Minute as a zero-padded decimal (00 to 59)
*   `%S`: Second as a zero-padded decimal (00 to 59)
*   `%f`: Microsecond (6 digits)

### 🗓️ Weekdays & Calendar
*   `%a`: Abbreviated weekday name (Mon)
*   `%A`: Full weekday name (Monday)
*   `%w`: Weekday as a decimal (0 is Sunday, 6 is Saturday)
*   `%j`: Day of the year as a zero-padded decimal (001 to 366)

### 🌍 Timezone & Special
*   `%Z`: Timezone name (IST, UTC)
*   `%z`: UTC offset (+0530)
*   `%c`: Locale’s appropriate date and time representation

---
💡 **Tip**: Use `%-d` (Linux/Mac) or `%#d` (Windows) to remove leading zeros from numbers.
