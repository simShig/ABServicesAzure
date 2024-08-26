from flask import Flask, render_template_string
import requests
import datetime
import logging

# Initialize Flask app
app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Variables for storing Bitcoin price data
prices = []
last_fetch_time = None
average_price = None

def fetch_bitcoin_price():
    global last_fetch_time, average_price
    try:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
        response.raise_for_status()
        bitcoin_price = response.json().get("bitcoin", {}).get("usd")
        if bitcoin_price is None:
            raise ValueError("Bitcoin price not found in response")
    except (requests.RequestException, ValueError) as e:
        logger.error(f"Error fetching bitcoin price: {e}")
        bitcoin_price = None
    else:
        prices.append(bitcoin_price)
        last_fetch_time = datetime.datetime.now()

        # Calculate 10-minute average every 10 prices
        if len(prices) == 10:
            average_price = sum(prices) / 10
            prices.clear()  # Reset the prices list

        # Log the current rate and average price
        logger.info(f"Current Bitcoin Price: {bitcoin_price} USD")
        logger.info(f"10-Minute Average Price: {average_price if average_price else 'Calculating...'} USD")

        return bitcoin_price

@app.route('/')
def index():
    bitcoin_price = fetch_bitcoin_price()
    return render_template_string('''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>Bitcoin Service</title>
            <meta http-equiv="refresh" content="60">
        </head>
        <body>
            <h1>Bitcoin Service</h1>
            <p>Last Fetch Time: {{ last_fetch_time if last_fetch_time is not none else "N/A" }}</p>
            <p>Current Bitcoin Price: {{ bitcoin_price if bitcoin_price is not none else "Fetching..." }} USD</p>
            <p>10-Minute Average Price: {{ average_price if average_price is not none else "Calculating..." }} USD</p>
        </body>
        </html>
    ''', last_fetch_time=last_fetch_time.strftime('%Y-%m-%d %H:%M:%S') if last_fetch_time else None,
                                  bitcoin_price=bitcoin_price,
                                  average_price=average_price)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
