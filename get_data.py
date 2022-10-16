import requests
import json
import pandas as pd
import csv
from datetime import datetime

# Main variables
API_KEY = "ZQEXKMBKCRBJTR5Z"
SYMBOLS = ["AUD", "USD"]
TIMEFRAME = "15min"
csv_file = pd.read_csv("AUDUSD_M15.csv", index_col="Time")

# Check if first row in csv exists
try:
    first_row = csv_file.index[0]
except:
    first_row = None

# API Call
url = "https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol={0}&to_symbol={1}&outputsize=full&interval={2}&apikey={3}".format(
    SYMBOLS[0], SYMBOLS[1], TIMEFRAME, API_KEY
)
api_data = json.loads(requests.get(url).text)

# Append all new data until date_hour is the same as the first row in the CSV
new_line = True
for date_hour in api_data["Time Series FX (15min)"]:
    if date_hour != first_row:
        if new_line:
            new_line = False
            with open("AUDUSD_M15.csv", "a") as f:
                f.write("\n")
        date_hour_formatted = str(date_hour).replace("-", ".")
        candle = {
            "Time": [date_hour_formatted],
            "Open": [api_data["Time Series FX (15min)"][date_hour]["1. open"]],
            "High": [api_data["Time Series FX (15min)"][date_hour]["2. high"]],
            "Low": [api_data["Time Series FX (15min)"][date_hour]["3. low"]],
            "Close": [api_data["Time Series FX (15min)"][date_hour]["4. close"]],
        }
        candle = pd.DataFrame(candle)
        candle.to_csv("AUDUSD_M15.csv", mode="a", index=False, header=False)
    else:
        break

# Sort data -------https://stackoverflow.com/questions/68106205/how-to-sort-a-csv-file-by-date-------
with open('AUDUSD_M15.csv', newline='') as csv_file:
    csv_file = csv.reader(csv_file, delimiter=',')
    header = next(csv_file)
    csv_file = sorted(csv_file, key=lambda row: datetime.strptime(
        row[0], "%Y.%m.%d %H:%M:%S"), reverse=True)
    csv_file.insert(0, header)
    csv_data = pd.DataFrame(csv_file)

csv_data.to_csv("AUDUSD_M15.csv", mode="w", index=False, header=False)
