# TrackARP 🚄

A professional-grade Python automation tool designed to monitor the **IRCTC Advance Reservation Period (ARP)**. It dispatches proactive Email and SMS alerts exactly 24 hours before the 60-day booking window opens.

---

## 🛠️ Features

*   **Intelligent Scheduling**: Monitors travel dates 61 days out to provide a "heads-up" alert 1 day before booking starts.
*   **Bi-Directional Support**: Specifically configured to track **Friday Departures** and **Monday Returns**.
*   **High-Signal Alerts**:
    *   **Email**: Comprehensive insights including primary booking times and a 9-day backup schedule.
    *   **SMS**: Ultra-concise Twilio notifications for immediate awareness.
*   **Reliable Automation**: GitHub Actions workflow optimized with `Asia/Kolkata` timezone logic.

---

## 💻 Tech Stack

*   **Language**: Python 3.10+
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

### 3. Repository Structure
The GitHub Action is configured to look for the script inside the `projects/TrackARP` directory:

```text
├── .github/workflows/TrackARP_Daily_Check.yml
└── projects/
    └── TrackARP/
        ├── main.py
        └── requirements.txt
```

---

## 📅 Automation Logic

*   **Calculation**: The script calculates `Journey Date = Today + 61 Days`. 
*   **Trigger**: Alerts only fire if the calculated Journey Date is a **Friday** or **Monday**.
*   **Timing**: GitHub Actions triggers at **07:00 AM IST**, giving you a 1-hour window before the **08:00 AM IST** IRCTC booking window opens.

---

## 🚉 IRCTC Booking Windows & Times

*   **General Quota**: Opens **60 days** in advance (excluding travel date) at **08:00 AM**.
*   **Tatkal AC**: Opens 1 day before departure at **10:00 AM**.
*   **Tatkal Sleeper**: Opens 1 day before departure at **11:00 AM**.

### 💡 Pro-Tips
1.  **Master List**: Pre-save passenger details in your IRCTC profile to skip typing.
2.  **Payment**: Use **UPI** or **IRCTC iPay** for the fastest checkout.
3.  **Maintenance**: Note that IRCTC services are usually down from **11:45 PM to 12:20 AM IST**.

---

## 📝 Appendix: `strftime` Cheat Sheet

### 📅 Date & Time Basics
*   `%A` / `%a`: Full / Abbreviated weekday (Monday / Mon)
*   `%B` / `%b`: Full / Abbreviated month (January / Jan)
*   `%d`: Day of the month (01 to 31)
*   `%Y`: Year with century (2024)
*   `%H` / `%M`: Hour (24-hour) and Minute (00 to 59)

### 🌍 Timezone 
*   `%Z`: Timezone name (IST, UTC)
*   `%z`: UTC offset (+0530)

---

> [!TIP]
> Ensure your GitHub Secrets match the variable names in the YAML workflow exactly to prevent authentication failures.
