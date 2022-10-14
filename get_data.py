import requests
import json
import pandas as pd

# Main variables
API_KEY = "ZQEXKMBKCRBJTR5Z"
SYMBOLS = ["AUD", "USD"]
TIMEFRAME = "15min"
csv_file = pd.read_csv("AUDUSD_M15.csv", index_col="TIME")

# Check if first row in csv exists
try:
    first_row = csv_file.index[0]
except:
    first_row = None

# API Call
url = "https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol={0}&to_symbol={1}&outputsize=full&interval={2}&apikey={3}".format(
    SYMBOLS[0], SYMBOLS[1], TIMEFRAME, API_KEY
)
print(url)
api_data = json.loads(requests.get(url).text)

new_line = True
for date_hour in api_data["Time Series FX (15min)"]:
    if date_hour != first_row:
        if new_line:
            new_line = False
            with open("AUDUSD_M15.csv", "a") as f:
                f.write("\n")
        candle = {
            "TIME": [date_hour],
            "OPEN": [api_data["Time Series FX (15min)"][date_hour]["1. open"]],
            "HIGH": [api_data["Time Series FX (15min)"][date_hour]["2. high"]],
            "LOW": [api_data["Time Series FX (15min)"][date_hour]["3. low"]],
            "CLOSE": [api_data["Time Series FX (15min)"][date_hour]["4. close"]],
        }
        candle = pd.DataFrame(candle)
        candle.to_csv("AUDUSD_M15.csv", mode="a", index=False, header=False)
    else:
        break

# csv_file = pd.read_csv("AUDUSD_M15.csv", index_col="TIME")
# csv_file = csv_file.sort_index(ascending=False)
# csv_file.to_csv("AUDUSD_M15.csv")
