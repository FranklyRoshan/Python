# ISS Pass Alert Daily Python Script

## Overview
This project is an automated tracking system that monitors the International Space Station (ISS) in real-time. It notifies the user via email when the ISS is currently overhead and visible in the night sky based on specific geographic coordinates.

## Core Functionality
1. Real-time Tracking: Fetches the current GPS coordinates (latitude/longitude) of the ISS using the Open Notify API.
2. Proximity Logic: Compares the ISS position against the user's fixed location (Chennai, India: $13.07°N, 80.20°E$), checking if the station is within a $\pm5°$ radius.
3. Visibility Filter: Uses the Sunrise-Sunset API to determine if it is currently dark at the user's location, ensuring the alert only triggers when the ISS is actually visible to the naked eye.
4. Automated Notification: Sends a "Look Up" alert via Gmail using Python’s smtplib and SSL/TLS for secure communication.

## Technical Stack
1. Language: Python 3.13
2. Libraries: requests (API handling), smtplib (Email), zoneinfo & tzdata (Timezone management).
3. Automation: GitHub Actions handles the execution using a cron schedule, allowing the script to run without a dedicated local server.

## How it Works
1. The script is triggered every 10 minutes via a GitHub Actions runner.
2. It converts the current UTC time to IST (India Standard Time) to check for night-time conditions.
3. If the ISS is within range AND it is night, an email is dispatched instantly to the user.