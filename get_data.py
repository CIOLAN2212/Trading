import requests
import json

API_KEY = "ZQEXKMBKCRBJTR5Z"
SYMBOLS = ["AUD", "USD"]
TIMEFRAME = "15min"

url = "https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol={0}&to_symbol={1}&outputsize=full&interval={2}&apikey={3}".format(
    SYMBOLS[0], SYMBOLS[1], TIMEFRAME, API_KEY
)
api_data = json.loads(requests.get(url).text)

candles = []
for date_hour in api_data["Time Series FX (15min)"]:
    for candle in api_data["Time Series FX (15min)"][date_hour]:
        # candle = [
        #     date_hour,
        #     candle_json["1. open"],
        #     candle_json["2. high"],
        #     candle_json["3. low"],
        #     candle_json["4. close"],
        # ]
        # candles.append(candle)
        print(candle["1. open"])

# print(candles)
