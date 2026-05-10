from datetime import datetime, timedelta
from email.message import EmailMessage
# pip install flask twilio
from twilio.rest import Client
from dotenv import load_dotenv
import smtplib
import os

# Load environment variables
load_dotenv()

# --- Configuration ---
ADVANCE_DAYS_FOR_REMINDER = 61
DATE_FORMAT_FULL = "%A, %b %d, %I:%M %p IST"
DATE_FORMAT_SHORT = "%a, %b %d"

EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("MY_PASSWORD")
SMTP_SERVER = os.environ.get("EMAIL_PROVIDER_SMTP_ADDRESS")
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
VIRTUAL_TWILIO_NUMBER = os.environ.get("VIRTUAL_TWILIO_NUMBER")
VERIFIED_NUMBER = os.environ.get("VERIFIED_NUMBER")

def send_email_alert(subject, body):
    """Handles the SMTP connection and sends the email."""
    try:
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = EMAIL
        msg["To"] = EMAIL
        msg.set_content(body)

        with smtplib.SMTP(SMTP_SERVER, 587) as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            connection.send_message(msg)
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

def send_sms_alert(msg_body):
    """Sends a concise SMS notification."""
    try:
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(
            body= msg_body,
            from_= VIRTUAL_TWILIO_NUMBER,
            to= VERIFIED_NUMBER,
        )
        # print(f"Message status: {message.status}")
        print("✅ SMS sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send sms: {e}")

def generate_booking_schedule():
    today = datetime.now()
    # The date the train actually departs
    journey_date = today + timedelta(days=ADVANCE_DAYS_FOR_REMINDER)
    # The date you must book (Tomorrow)
    booking_date = today + timedelta(days=1)

    # Logic: Only trigger if the target journey is a Friday
    if journey_date.strftime("%A") == "Thrusday":

        # Generating subsequent dates with list comprehension
        upcoming_options = [
            (journey_date + timedelta(days=i)).strftime(DATE_FORMAT_SHORT)
            for i in range(1, 10)
        ]
        options_str = "\n   - ".join(upcoming_options)

        # --- Constructing the Email Body ---
        subject = f"🚨 Action Required: Booking Window Opens Tomorrow ({booking_date.strftime('%b %d')})"
        email_body = (
            f"Hello Frank,\n\n"
            f"Heads up!\n\n"
            f"Tomorrow, the primary booking window is going to open.\n\n"
            f"📍 TARGET JOURNEY:\n"
            f"   {journey_date.strftime('%A, %b %d, %Y')}\n\n"
            f"⏰ BOOKING ACTION TIME:\n"
            f"   Tomorrow, {booking_date.strftime('%b %d')} at 08:00 AM IST sharp.\n\n"
            f"📋 SUBSEQUENT TRAVEL INSIGHTS:\n"
            f"   If you miss the Friday slot, here are the next available dates:\n"
            f"   - {options_str}\n\n"
            f"💡 TO DO:\n"
            f"   - Set an alarm for tomorrow 7:55 AM!\n\n"
            f"Good luck with the booking!"
        )

        # --- SMS Body (Ultra-Concise for Twilio) ---
        # Using a cleaner date format without the timestamp
        sms_date = journey_date.strftime("%b %d (%a)")

        # Taking only the first 3 subsequent dates to keep SMS short
        quick_backups = ", ".join(upcoming_options[:3])

        sms_body = (
            f"TRAIN ALERT:\n"
            f"Target: {sms_date}\n"
            f"Action: Tomorrow 8AM IST\n"
            f"Next: {quick_backups}..."
        )

        print(f"Processing reminder for {journey_date.date()}...")
        send_email_alert(subject, email_body)
        send_sms_alert(sms_body)

if __name__ == "__main__":
    generate_booking_schedule()
