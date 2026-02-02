from datetime import datetime
from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
from pathlib import Path



#get secrets from secrets.txt
secrets_path = Path(__file__).parent.parent / "secrets.txt"
with open(secrets_path, "r") as f:
    key = f.readline().strip()
    secret = f.readline().strip()
print(key)
print(secret)

APCA_API_BASE_URL = "https://paper-api.alpaca.markets" # For paper trading


# No keys required for crypto data
client = CryptoHistoricalDataClient()

# Creating request object
request_params = CryptoBarsRequest(
  symbol_or_symbols=["BTC/USD"],
  #symbol_or_symbols=["BTC/USD"],
  timeframe=TimeFrame.Day,
  start=datetime(2025, 9, 1),
  end=datetime(2025, 9, 7)
)

# Retrieve daily bars for Bitcoin in a DataFrame and printing it
btc_bars = client.get_crypto_bars(request_params)

# Convert to dataframe
btc_bars.df
print("Bitcoin Daily Bars DataFrame:")
print(btc_bars.df)