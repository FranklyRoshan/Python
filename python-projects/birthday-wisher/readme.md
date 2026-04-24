# Birthday Wisher (Automated Email) 
🎂An automated Python system that checks a database of birthdays daily and sends a personalized greeting email using one of several randomized letter templates. This project is fully automated using GitHub Actions.

## 🚀 Features
1. Dynamic Matching: Compares the current date (Month/Day) against a CSV database.Template Randomization: Randomly selects one of three letter templates (letter_1.txt, letter_2.txt, etc.) to keep greetings varied.
2. String Manipulation: Automatically replaces the [NAME] placeholder in templates with the person's actual name.
3. Daily Automation: Scheduled via GitHub Actions to run every morning at 8:00 AM IST.

## 🛠️ Technical Stack
1. Language: Python 3.13
2. Libraries: pandas (Data handling), smtplib (Email delivery).
3. Automation: GitHub Actions.

## 📁 Project Structure
For the script to run correctly, your birthday-wisher folder must be organized as follows:
python-projects/birthday-wisher/
├── main.py              # Core logic
├── birthdays.csv        # Database (name, email, year, month, day)
├── requirements.txt     # pandas
├── letter_templates/    # Folder containing greeting templates
│   ├── letter_1.txt
│   ├── letter_2.txt
│   └── letter_3.txt
└── .github/workflows/   # CI/CD YAML configuration

## ⚙️ Setup & Configuration
1. Requirements
Your requirements.txt only needs:Plaintextpandas
2. GitHub Secrets
The script retrieves your email credentials safely from GitHub's encrypted secrets. Add these in Settings > Secrets and variables > Actions:
Secret              NameDescription
MY_EMAIL            Your Gmail address
MY_EMAIL_PASSWORD   Your Gmail App Password (not your regular password)
3. CSV Format
Ensure your birthdays.csv follows this header format:
    Code snippet
    name,email,year,month,day
    Test User,test@email.com,1995,4,24

## 📝 How It Works
1. Trigger: GitHub Actions wakes up at 2:30 AM UTC (8:00 AM IST).
2. Scan: The script reads birthdays.csv using pandas and creates a dictionary of birthdays keyed by (month, day).
3. Match: If today's date matches a key in the dictionary, the script:
    • Picks a random file from letter_templates/.
    • Replaces the [NAME] placeholder with the birthday person's name.
4. Email: Logs into the SMTP server and dispatches the personalized email.

A quick tip for your code:
1. In your main.py, you used an f-string inside another f-string for the email subject:msg=f"subject: Happy Birthday {birthdays_person["name"]}!\n\n{contents}"
2. Be careful: Using double quotes " inside double quotes will cause a syntax error. Change the inner ones to single quotes like this:{birthdays_person['name']}