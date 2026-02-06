import yfinance as yf
import json

# Λίστα με τα σύμβολα που θέλεις
tickers = ["BTC-USD", "ETH-USD", "AAPL", "TSLA"]

data_to_save = {}

for symbol in tickers:
    ticker = yf.Ticker(symbol)
    # Παίρνουμε την τελευταία τιμή
    price = ticker.fast_info['last_price']
    data_to_save[symbol] = round(price, 2)

# Αποθήκευση σε JSON αρχείο για να το διαβάσει η HTML
with open('data.json', 'w') as f:
    json.dump(data_to_save, f)

print("Data updated successfully!")
