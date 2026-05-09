# ===============================================================
# =============== Train Ticket Reminder =========================
# ===============================================================
from datetime import datetime, timedelta

# Get Current date
today = datetime.today().date()
tomorrow = today + timedelta(days=1)

# SixtyOne days before date of journey for prior notification
reminder_date = today

# Journey date
journey_date = today + timedelta(days=61)

if journey_date.strftime("%A") == "Thursday":

    f_journey_date= datetime(journey_date.year, journey_date.month, journey_date.day, 8, 0)
    fstring_journey_date= f_journey_date.strftime("%A, %b %d, %I:%M %p IST")
    print(fstring_journey_date)

    next_ten_days = []
    for i in range(1,10):
        date = journey_date + timedelta(days=i)
        fdate = date.strftime("%a, %b %d")
        next_ten_days.append(fdate)
    print(next_ten_days)
