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

## Resource links
1. International Space Station Current Location - http://open-notify.org/Open-Notify-API/ISS-Location-Now/
   (API - http://api.open-notify.org/iss-now.json)
2. HTTP Status codes - http://httpstatuses.com/
3. Requests (HTTP library for Python) Documentation - https://docs.python-requests.org/en/latest/
4. Sunset and sunrise times API - https://sunrise-sunset.org/api
5. Latitude and longitude address tool - https://www.latlong.net/Show-Latitude-Longitude.html
   (API - https://api.sunrise-sunset.org/json)

## HTTP Status Code Categories
Organized for documentation in a Python file

1. 1xx: Informational
The request has been received, and the server is continuing the process.
Common Example: HTTPStatus.CONTINUE (100)

2. 2xx: Success
The action was successfully received, understood, and accepted.
Common Examples: HTTPStatus.OK (200), HTTPStatus.CREATED (201), HTTPStatus.NO_CONTENT (204)

3. 3xx: Redirection
Further action (e.g., a redirect) is required to complete the request.
Common Examples: HTTPStatus.MOVED_PERMANENTLY (301), HTTPStatus.NOT_MODIFIED (304)

4. 4xx: Client Error
The request contains bad syntax or cannot be fulfilled (client-side issue).
Common Examples: HTTPStatus.BAD_REQUEST (400), HTTPStatus.FORBIDDEN (403), HTTPStatus.NOT_FOUND (404)

5. 5xx: Server Error
The server failed to fulfill a valid request (server-side issue).
Common Examples: HTTPStatus.INTERNAL_SERVER_ERROR (500), HTTPStatus.SERVICE_UNAVAILABLE (503)

For programmatic use, import the enum:
from http import HTTPStatus


