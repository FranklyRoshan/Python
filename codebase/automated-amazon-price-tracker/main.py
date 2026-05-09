import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
import os
from email.message import EmailMessage

# Load environment variables
load_dotenv()

URL = os.environ["URL"]
MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASSWORD = os.environ["MY_PASSWORD"]
SMTP_SERVER = os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"]
PRICE_CAP = 10400


# ---------------- SCRAPER FUNCTION ---------------- #
def get_product_details(url):
    """
    Fetch product title and price from Amazon.

    Returns:
        (title, price) or None
    """

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9",
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return None

        soup = BeautifulSoup(response.text, "html.parser")

        # Product Title
        title_element = soup.find("span", id="productTitle")
        if not title_element:
            print("Title not found")
            return None

        title = title_element.get_text(strip=True)

        # Price
        price_whole = soup.find("span", class_="a-price-whole")
        price_fraction = soup.find("span", class_="a-price-fraction")

        if not price_whole or not price_fraction:
            print("Price not found")
            return None

        price = float(price_whole.text.replace(",", "")) + \
                float(price_fraction.text) / 100

        return title, price

    except Exception as e:
        print(f"Error: {e}")
        return None


# ---------------- EMAIL FUNCTION ---------------- #
def send_email(subject, body):
    """
    Send email using SMTP.
    """
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = MY_EMAIL
    msg["To"] = MY_EMAIL

    msg.set_content(body)  # Handles UTF-8 automatically

    with smtplib.SMTP(SMTP_SERVER, 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.send_message(msg)


# ---------------- MAIN LOGIC ---------------- #
def main():
    result = get_product_details(URL)

    if not result:
        print("Failed to fetch product details.")
        return

    product_name, price = result

    print(f"{product_name} → ₹{price}")

    # Price condition
    if price <= PRICE_CAP:
        email_body = f"""
Product: {product_name}
Price: ₹{price}

Link: {URL}
""" # ASCII
            # (f"Product: {product_name}\n"
            #           f"Price: ₹{price}\n\n"
            #           f"Link: {URL}").encode('utf-8'))

        send_email("Amazon Price Alert!", email_body)


# ---------------- RUN ---------------- #
if __name__ == "__main__":
    main()