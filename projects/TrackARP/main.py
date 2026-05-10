from datetime import datetime, timedelta, timezone
from email.message import EmailMessage
from twilio.rest import Client
from dotenv import load_dotenv
import smtplib
import os

load_dotenv()

# --- Configuration ---
ADVANCE_DAYS_FOR_REMINDER = 61
DATE_FORMAT_SHORT = "%a, %b %d"

# Env vars
EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("MY_PASSWORD")
SMTP_SERVER = os.environ.get("EMAIL_PROVIDER_SMTP_ADDRESS")
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
VIRTUAL_TWILIO_NUMBER = os.environ.get("VIRTUAL_TWILIO_NUMBER")
VERIFIED_NUMBER = os.environ.get("VERIFIED_NUMBER")

def send_alerts(subject, email_body, sms_body):
    """Consolidated alert sender."""
    # Email
    try:
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = EMAIL
        msg["To"] = EMAIL
        msg.set_content(email_body)
        with smtplib.SMTP(SMTP_SERVER, 587) as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            connection.send_message(msg)
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Email Failed: {e}")

    # SMS
    try:
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(body=sms_body, from_=VIRTUAL_TWILIO_NUMBER, to=VERIFIED_NUMBER)
        print("✅ SMS sent successfully!")
    except Exception as e:
        print(f"❌ SMS Failed: {e}")

def generate_booking_schedule():
    ist_offset = timezone(timedelta(hours=5, minutes=30))
    today = datetime.now(ist_offset) 

    journey_date = today + timedelta(days=ADVANCE_DAYS_FOR_REMINDER)
    booking_date = today + timedelta(days=1)
    day_name = journey_date.strftime("%A")

    print(f"--- Run Summary ---")
    print(f"System Time (IST): {today.strftime('%Y-%m-%d %H:%M')}")
    print(f"Checking Journey: {day_name}, {journey_date.strftime('%b %d')}")

    # Determine if today is a target check day
    if day_name not in ["Friday", "Monday"]:
        print(f"⏭️ Skipping: {day_name} journeys do not require alerts today.")
        print(f"-------------------")
        return

    # Efficiency: Calculate these once as they are used in both types of alerts
    upcoming_options = [(journey_date + timedelta(days=i)).strftime(DATE_FORMAT_SHORT) for i in range(1, 10)]
    options_str = "\n   - ".join(upcoming_options)
    quick_backups = ", ".join(upcoming_options[:3])
    sms_date = journey_date.strftime("%b %d (%a)")
    
    # Set type-specific details
    is_departure = (day_name == "Friday")
    type_label = "DEPARTURE" if is_departure else "RETURN"
    extra_to_do = "- Set an alarm for 7:55 AM!" if is_departure else "- Confirm return time with the group!"

    # Unified Content Generation
    subject = f"🚨 Action Required: {type_label.capitalize()} Booking Window Opens Tomorrow ({booking_date.strftime('%b %d')})"
    
    email_body = (
        f"Hello Frank,\n\n"
        f"Tomorrow, the {type_label} booking window opens.\n\n"
        f"📍 TARGET JOURNEY:\n   {journey_date.strftime('%A, %b %d, %Y')}\n\n"
        f"⏰ BOOKING ACTION TIME:\n   Tomorrow, {booking_date.strftime('%b %d')} at 08:00 AM IST sharp.\n\n"
        f"📋 SUBSEQUENT TRAVEL INSIGHTS:\n   If you miss this slot, here are backups:\n   - {options_str}\n\n"
        f"💡 TO DO:\n   {extra_to_do}\n   - Good luck with the booking!"
    )

    sms_body = f"TRAIN {type_label}:\nTarget: {sms_date}\nAction: Tomorrow 8AM IST\nNext: {quick_backups}..."

    # Send consolidated alerts
    print(f"✅ Processing {type_label} reminder...")
    send_alerts(subject, email_body, sms_body)
    print(f"-------------------")

if __name__ == "__main__":
    try:
        generate_booking_schedule()
    except Exception as global_err:
        print(f"💥 Critical Script Failure: {global_err}")
