# 🚆 TrackARP Daily Check

An automated Python-based train booking reminder system that checks upcoming journey dates and sends timely notifications through **Email** and **Telegram**.

---

## 📌 Overview

TrackARP Daily Check is designed to remind you when the train booking window for an upcoming journey is about to open.

The application:

- 📅 Calculates the upcoming journey date.
- 🔎 Determines whether a reminder is required.
- 🚆 Identifies the journey type — Departure or Return.
- 📋 Generates the next 5 backup dates.
- 📧 Sends a detailed email reminder.
- 📱 Sends a Telegram notification.
- 🤖 Runs automatically every day using GitHub Actions.
- 🇮🇳 Uses Indian Standard Time (IST) for date calculations.

---

## 🏗️ Project Structure

```text
TrackARP/
│
├── main.py
├── requirements.txt
├── .env
│
└── .github/
    └── workflows/
        └── track_arp_action.yml