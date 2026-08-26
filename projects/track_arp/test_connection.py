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

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


# ============================================================
# Environment Variable / Secret Checks
# ============================================================

def check_environment_variables():
    """
    Check whether all required environment variables are loaded.

    The actual secret values are never printed.
    Only True/False is displayed.
    """

    print("=" * 60)
    print("🔐 Environment Variable Check")
    print("=" * 60)

    variables = {
        "EMAIL_ID": EMAIL,
        "EMAIL_ID_PASSWORD": PASSWORD,
        "EMAIL_PROVIDER_SMTP_ADDRESS": SMTP_SERVER,
        "TELEGRAM_BOT_TOKEN": TELEGRAM_BOT_TOKEN,
        "TELEGRAM_CHAT_ID": TELEGRAM_CHAT_ID,
    }

    all_loaded = True

    for name, value in variables.items():

        loaded = bool(value)

        status = "✅ Loaded" if loaded else "❌ Missing"

        print(f"{name}: {status}")

        if not loaded:
            all_loaded = False

    print("=" * 60)

    if all_loaded:
        print("✅ All required environment variables are loaded.")
    else:
        print("❌ One or more environment variables are missing.")

    print()

    return all_loaded


# ============================================================
# Test Email
# ============================================================

def test_email():
    """Send a test email to verify the SMTP configuration."""

    print("=" * 60)
    print("📧 Testing Email")
    print("=" * 60)

    try:

        if not EMAIL:
            raise ValueError("EMAIL_ID is missing.")

        if not PASSWORD:
            raise ValueError("EMAIL_ID_PASSWORD is missing.")

        if not SMTP_SERVER:
            raise ValueError(
                "EMAIL_PROVIDER_SMTP_ADDRESS is missing."
            )

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

        with smtplib.SMTP(
            SMTP_SERVER,
            587,
            timeout=10
        ) as connection:

            connection.starttls()
            connection.login(
                EMAIL,
                PASSWORD
            )

            connection.send_message(message)

        print("✅ Test email sent successfully.")

    except Exception as error:

        print(f"❌ Email failed: {error}")

    print()


# ============================================================
# Send Telegram Notification
# ============================================================

def send_telegram(message):
    """
    Send a message to Telegram using the Telegram Bot API.

    Raises:
        ValueError:
            If the Telegram bot token or chat ID is missing.

        RuntimeError:
            If the Telegram API rejects the request.
    """

    if not TELEGRAM_BOT_TOKEN:
        raise ValueError(
            "TELEGRAM_BOT_TOKEN is missing."
        )

    if not TELEGRAM_CHAT_ID:
        raise ValueError(
            "TELEGRAM_CHAT_ID is missing."
        )

    telegram_url = (
        f"https://api.telegram.org/bot"
        f"{TELEGRAM_BOT_TOKEN}/sendMessage"
    )

    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
    }

    print("📱 Sending Telegram notification...")

    response = requests.post(
        telegram_url,
        data=data,
        timeout=10,
    )

    response_data = response.json()

    if response_data.get("ok"):

        print(
            "✅ Telegram notification "
            "sent successfully!"
        )

    else:

        raise RuntimeError(
            f"Telegram API error: {response_data}"
        )


# ============================================================
# Test Telegram
# ============================================================

def test_telegram():
    """Test the Telegram notification function."""

    print("=" * 60)
    print("📱 Testing Telegram")
    print("=" * 60)

    try:

        test_message = (
            "🚆 TrackARP Test Message\n\n"
            "This message is being sent using the "
            "same send_telegram() function as main.py.\n\n"
            "✅ Telegram notification is working correctly!"
        )

        send_telegram(test_message)

    except Exception as error:

        print(f"❌ Telegram failed: {error}")

    print()


# ============================================================
# Run Tests
# ============================================================

if __name__ == "__main__":

    print()
    print("=" * 60)
    print("🚀 TrackARP Notification System Test")
    print("=" * 60)
    print()

    # --------------------------------------------------------
    # 1. Check all environment variables
    # --------------------------------------------------------

    environment_ok = check_environment_variables()

    # --------------------------------------------------------
    # 2. Test Email
    # --------------------------------------------------------

    test_email()

    # --------------------------------------------------------
    # 3. Test Telegram
    # --------------------------------------------------------

    test_telegram()

    # --------------------------------------------------------
    # Test Completed
    # --------------------------------------------------------

    print("=" * 60)
    print("🏁 Test completed.")
    print("=" * 60)
