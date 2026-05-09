TrackARP 
🚄A professional-grade Python automation tool designed to monitor the IRCTC Advance Reservation Period (ARP). It sends proactive Email and SMS alerts exactly 24 hours before the 60-day booking window opens.

🛠️ Features
Intelligent Scheduling: Monitors travel dates 61 days out to provide a "heads-up" alert 24 hours before booking opens.
High-Signal Alerts:Email: Full travel insights, primary booking time (8:00 AM IST), and a 9-day backup schedule.
SMS: Ultra-concise Twilio notifications for immediate awareness.
Future-Proof: GitHub Actions workflow optimized for Node.js 24.

💻 Tech Stack
Language: Python 3.9+
APIs: Twilio (SMS), SMTPLIB (Email)
Automation: GitHub Actions (Cron: 30 1 * * * / 07:00 AM IST)
Security: GitHub Secrets & python-dotenv

🚀 Setup
1. Environment VariablesCreate a .env file for local testing (or add as Secrets in GitHub):
env
MY_EMAIL=your_email@gmail.com
MY_EMAIL_PASSWORD=your_app_password
EMAIL_PROVIDER_SMTP_ADDRESS=://gmail.com
TWILIO_SID=your_sid
TWILIO_AUTH_TOKEN=your_token
VIRTUAL_TWILIO_NUMBER=+123456789
TWILIO_VERIFIED_NUMBER=+91987654321

2. Installationbashpip install -r requirements.txt

3. Folder StructureEnsure your repository matches this structure to avoid Exit Code 

2:text├── .github/workflows/reminder.yml
└── projects/
    └── TrackARP/
        ├── TrackARP.py
        └── requirements.txt

📅 Automation Logic
Target Day: The script specifically tracks journeys falling on Firday.
Timing: Alerts are dispatched at 07:00 AM IST, giving you 1 hour to prepare before the 08:00 AM IST IRCTC window opens.


Indian Railways trains, booking opens 60 days before the journey date at 08:00 AM IST.

 📅 Booking Windows & TimesGeneral Quota:
 1. Opens 60 days in advance (excluding the travel date) at 08:00 AM.
 2. Tatkal AC: Opens 1 day before the train's departure from its source station at 10:00 AM.
 3. Tatkal Sleeper: Opens 1 day before departure at 11:00 AM.
 4. Current Booking: Available after chart preparation (usually 4 hours before departure)
    until 30 minutes before the train leaves.

 💡 Pro-Tips for Successful Booking
 1. The "Master List": Pre-save passenger detail names, ages, and ID details in your IRCTC profile before the booking window o
    pens to skip manual typing.
 2. Fast Logins: Log in to the Official IRCTC Portal at least 5 minutes before 08:00 AM, 10:00 AM, or 11:00 AM.
 3. Payment Readiness: Use UPI, IRCTC iPay or saved cards for the fastest checkout; Tatkal seats often vanish within seconds.
 4. 📍 Note: Booking services are usually down for maintenance from 11:45 PM to 12:20 AM IST.


Notes
 📅 Date (Day, Month, Year)
 1. %d: Day of the month as a zero-padded decimal (01 to 31)
 2. %-d: Day of the month as a decimal (1 to 31)
 3. %b: Abbreviated month name (Jan)
 4. %B: Full month name (January)
 5. %m: Month as a zero-padded decimal (01 to 12)
 6. %y: Year without century (26)
 7. %Y: Year with century (2026)

⏰ Time (Hours, Minutes, Seconds)
1. %H: Hour (24-hour clock) (00 to 23)
2. %I: Hour (12-hour clock) (01 to 12)
3. %p: Locale’s equivalent of either AM or PM
4. %M: Minute as a zero-padded decimal (00 to 59)
5. %S: Second as a zero-padded decimal (00 to 59)
6. %f: Microsecond (6 digits) (000000 to 999999)

🗓️ Weekdays & Calendar
1. %a: Abbreviated weekday name (Mon)
2. %A: Full weekday name (Monday)
3. %w: Weekday as a decimal (0 is Sunday, 6 is Saturday)
4. %j: Day of the year as a zero-padded decimal (001 to 366)
5. %U: Week number of the year (Sunday as first day) (00 to 53)
6. %W: Week number of the year (Monday as first day) (00 to 53)

🌍 Timezone & Special
1. %Z: Timezone name (IST, UTC)
2. %z: UTC offset (+0530)
3. %c: Locale’s appropriate date and time representation
4. %x: Locale’s appropriate date representation
5. %X: Locale’s appropriate time representation
6. %%: A literal % character

💡 Tip: Use %-d (Linux/Mac) or %#d (Windows) to remove leading zeros from numbers.
