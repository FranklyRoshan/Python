from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from email.message import EmailMessage

from dotenv import load_dotenv

import os
import smtplib
import requests


load_dotenv()


# ============================================================
# Configuration
# ============================================================

ADVANCE_DAYS_FOR_REMINDER = 61
DATE_FORMAT_SHORT = "%a, %b %d"
BACKUP_DAYS = 5

# Email
EMAIL: ${{ secrets.EMAIL }}
PASSWORD: ${{ secrets.PASSWORD }}
SMTP_SERVER: ${{ secrets.SMTP_SERVER }}

# Telegram
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")


# ============================================================
# Send Telegram Notification
# ============================================================

def send_telegram(message):
    """Send a notification to Telegram using a Telegram Bot."""

    telegram_url = (
        f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    )

    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }

    response = requests.post(telegram_url, data=data)

    if response.ok:
        print("✅ Telegram notification sent successfully!")
    else:
        print(f"❌ Telegram Failed: {response.text}")


# ============================================================
# Send Email + Telegram
# ============================================================

def send_alerts(subject, email_body, notification_body):
    """Send the alert through email and Telegram."""

    # --------------------------------------------------------
    # Email
    # --------------------------------------------------------

    try:
        message = EmailMessage()

        message["Subject"] = subject
        message["From"] = EMAIL
        message["To"] = EMAIL

        message.set_content(email_body)

        with smtplib.SMTP(SMTP_SERVER, 587) as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            connection.send_message(message)

        print("✅ Email sent successfully!")

    except Exception as error:
        print(f"❌ Email Failed: {error}")

    # --------------------------------------------------------
    # Telegram
    # --------------------------------------------------------

    try:
        send_telegram(notification_body)

    except Exception as error:
        print(f"❌ Telegram Failed: {error}")


# ============================================================
# Generate Booking Schedule
# ============================================================

def generate_booking_schedule():
    """Determine whether a train-booking reminder is required."""

    today = datetime.now(ZoneInfo("Asia/Kolkata"))

    journey_date = today + timedelta(days=ADVANCE_DAYS_FOR_REMINDER)
    booking_date = today + timedelta(days=1)

    day_name = journey_date.strftime("%A")

    print("--- Run Summary ---")

    print(
        f"System Time (IST): "
        f"{today.strftime('%Y-%m-%d %H:%M')}"
    )

    print(
        f"Checking Journey: "
        f"{day_name}, {journey_date.strftime('%b %d')}"
    )

    # --------------------------------------------------------
    # Check whether today is a target reminder day
    # --------------------------------------------------------

    if day_name not in ["Friday", "Monday"]:
        print(
            f"⏭️ Skipping: {day_name} journeys "
            f"do not require alerts today."
        )
        print("-------------------")
        return

    # --------------------------------------------------------
    # Generate next 5 backup dates
    # --------------------------------------------------------

    backup_dates = [
        journey_date + timedelta(days=i)
        for i in range(1, BACKUP_DAYS + 1)
    ]

    options_str = "\n".join(
        f"   • {date.strftime('%A, %B %d, %Y')}"
        for date in backup_dates
    )

    quick_backups = ", ".join(
        date.strftime("%b %d")
        for date in backup_dates[:3]
    )

    journey_display_date = journey_date.strftime("%b %d (%a)")

    # --------------------------------------------------------
    # Determine departure / return
    # --------------------------------------------------------

    is_departure = day_name == "Friday"

    type_label = "DEPARTURE" if is_departure else "RETURN"

    extra_to_do = (
        "Set an alarm for 7:55 AM!"
        if is_departure
        else "Confirm the return time with the group!"
    )

    # ========================================================
    # Email
    # ========================================================

    subject = (
        f"🚨 Train Booking Reminder — "
        f"{type_label.capitalize()} Booking Tomorrow"
    )

    email_body = (
        f"🚆 TRAIN BOOKING REMINDER\n\n"

        f"Hi Frank,\n\n"

        f"This is a reminder that the "
        f"{type_label.lower()} train booking window opens tomorrow.\n\n"

        f"📅 JOURNEY DETAILS\n\n"

        f"Journey Date: "
        f"{journey_date.strftime('%A, %B %d, %Y')}\n"

        f"Booking Opens: "
        f"{booking_date.strftime('%A, %B %d, %Y')} "
        f"at 08:00 AM IST\n\n"

        f"🎯 ACTION REQUIRED\n\n"

        f"Please be ready before 08:00 AM IST and "
        f"complete the booking as soon as the window opens.\n\n"

        f"💡 {extra_to_do}\n\n"

        f"🔄 BACKUP DATES\n\n"

        f"If the preferred journey date is unavailable, "
        f"consider these alternative dates:\n\n"

        f"{options_str}\n\n"

        f"⏰ IMPORTANT\n\n"

        f"Set a reminder/alarm before 08:00 AM IST "
        f"so you don't miss the booking window.\n\n"

        f"Good luck with the booking! 🚆\n\n"

        f"— Train Booking Reminder"
    )

    # ========================================================
    # Telegram
    # ========================================================

    telegram_body = (
        f"🚨 TRAIN {type_label}\n\n"

        f"📍 Target: {journey_display_date}\n"

        f"⏰ Booking: Tomorrow at 08:00 AM IST\n\n"

        f"🎯 Action:\n"
        f"{extra_to_do}\n\n"

        f"🔄 Backup dates:\n"
        f"{quick_backups}\n\n"

        f"🚆 Be ready before 08:00 AM!"
    )

    # ========================================================
    # Send Alerts
    # ========================================================

    print(f"✅ Processing {type_label} reminder...")

    send_alerts(
        subject,
        email_body,
        telegram_body
    )

    print("-------------------")


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":

    try:
        generate_booking_schedule()

    except Exception as error:
        print(f"💥 Critical Script Failure: {error}")
