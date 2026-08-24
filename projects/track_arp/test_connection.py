import os
import smtplib
import requests

from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

# ============================================================
# Configuration
# ============================================================

EMAIL = os.getenv("EMAIL_ID")
PASSWORD = os.getenv("EMAIL_ID_PASSWORD")
SMTP_SERVER = os.getenv("EMAIL_PROVIDER_SMTP_ADDRESS")

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


# ============================================================
# Test Email
# ============================================================

def test_email():
    """Send a test email to verify SMTP configuration."""

    try:
        message = EmailMessage()
        message["Subject"] = "TrackARP - Test Email"
        message["From"] = EMAIL
        message["To"] = EMAIL

        message.set_content(
            "Hello Frank,\n\n"
            "This is a test email from TrackARP.\n\n"
            "If you received this message, the email "
            "notification system is working correctly.\n\n"
            "🚆 TrackARP"
        )

        with smtplib.SMTP(SMTP_SERVER, 587) as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            connection.send_message(message)

        print("✅ Test email sent successfully.")

    except Exception as error:
        print(f"❌ Email failed: {error}")


# ============================================================
# Test Telegram
# ============================================================

def test_telegram():
    """Send a test Telegram message to verify the bot."""

    try:
        url = (
            f"https://api.telegram.org/"
            f"bot{TELEGRAM_TOKEN}/sendMessage"
        )

        message = (
            "🚆 TrackARP Test Message\n\n"
            "✅ Telegram notification is working correctly!"
        )

        response = requests.post(
            url,
            data={
                "chat_id": TELEGRAM_CHAT_ID,
                "text": message
            }
        )

        if response.ok:
            print("✅ Test Telegram message sent successfully.")
        else:
            print(f"❌ Telegram failed: {response.text}")

    except Exception as error:
        print(f"❌ Telegram failed: {error}")


# ============================================================
# Run Tests
# ============================================================

if __name__ == "__main__":

    print("🚀 Starting TrackARP notification test...\n")

    test_email()
    test_telegram()

    print("\n🏁 Test completed.")