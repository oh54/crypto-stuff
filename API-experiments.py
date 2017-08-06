import json
import requests

#rates = requests.get("https://blockchain.info/ticker").json()
#rates = {'SGD': {'sell': 3172.81, '15m': 3172.82, 'symbol': '$', 'last': 3172.82, 'buy': 3172.82}, 'DKK': {'sell': 14972.74, '15m': 14972.8, 'symbol': 'kr', 'last': 14972.8, 'buy': 14972.8}, 'CNY': {'sell': 15659.48, '15m': 15659.55, 'symbol': '¥', 'last': 15659.55, 'buy': 15659.55}, 'BRL': {'sell': 7311.76, '15m': 7311.79, 'symbol': 'R$', 'last': 7311.79, 'buy': 7311.79}, 'TWD': {'sell': 70448.07, '15m': 70448.38, 'symbol': 'NT$', 'last': 70448.38, 'buy': 70448.38}, 'GBP': {'sell': 1779.66, '15m': 1779.67, 'symbol': '£', 'last': 1779.67, 'buy': 1779.67}, 'EUR': {'sell': 2013.29, '15m': 2013.3, 'symbol': '€', 'last': 2013.3, 'buy': 2013.3}, 'RUB': {'sell': 137173.1, '15m': 137173.69, 'symbol': 'RUB', 'last': 137173.69, 'buy': 137173.69}, 'HKD': {'sell': 18101.87, '15m': 18101.95, 'symbol': '$', 'last': 18101.95, 'buy': 18101.95}, 'CAD': {'sell': 2921.67, '15m': 2921.68, 'symbol': '$', 'last': 2921.68, 'buy': 2921.68}, 'KRW': {'sell': 2604000.81, '15m': 2604012.04, 'symbol': '₩', 'last': 2604012.04, 'buy': 2604012.04}, 'NZD': {'sell': 3150.07, '15m': 3150.08, 'symbol': '$', 'last': 3150.08, 'buy': 3150.08}, 'INR': {'sell': 149065.05, '15m': 149065.69, 'symbol': '₹', 'last': 149065.69, 'buy': 149065.69}, 'ISK': {'sell': 246247.71, '15m': 246248.77, 'symbol': 'kr', 'last': 246248.77, 'buy': 246248.77}, 'SEK': {'sell': 19246.93, '15m': 19247.02, 'symbol': 'kr', 'last': 19247.02, 'buy': 19247.02}, 'AUD': {'sell': 2920.35, '15m': 2920.36, 'symbol': '$', 'last': 2920.36, 'buy': 2920.36}, 'USD': {'sell': 2318.48, '15m': 2318.49, 'symbol': '$', 'last': 2318.49, 'buy': 2318.49}, 'PLN': {'sell': 8476.63, '15m': 8476.66, 'symbol': 'zł', 'last': 8476.66, 'buy': 8476.66}, 'CLP': {'sell': 1515590.38, '15m': 1515596.91, 'symbol': '$', 'last': 1515596.91, 'buy': 1515596.91}, 'JPY': {'sell': 259172.83, '15m': 259173.95, 'symbol': '¥', 'last': 259173.95, 'buy': 259173.95}, 'CHF': {'sell': 2213.37, '15m': 2213.38, 'symbol': 'CHF', 'last': 2213.38, 'buy': 2213.38}, 'THB': {'sell': 77877.74, '15m': 77878.08, 'symbol': '฿', 'last': 77878.08, 'buy': 77878.08}}
#eur_rates = rates["EUR"]
#usd_rates = rates["USD"]


def get_and_write_chart_data(chart, option_string):
    market_price_resp = requests.get("https://api.blockchain.info/charts/{}?{}".format(chart, option_string))
    with open("data/" + chart + ".csv", "w") as f:
        print(market_price_resp.text, file=f)

def get_and_write_all_data(charts, option_string):
    for chart in charts:
        get_and_write_chart_data(chart, option_string)

option_string="start=2012-12-31&timespan=all&rollingAverage=8hours&format=csv&sampled=false"
charts = ["market-price", "median-confirmation-time", "avg-block-size", "cost-per-transaction", "difficulty",
          "n-transactions-excluding-popular", "hash-rate", "market-cap", "miners-revenue", "n-orphaned-blocks",
          "n-transactions-per-block", "n-transactions", "n-unique-addresses", "total-bitcoins", "transaction-fees"]

# All data is daily close 
get_and_write_all_data(charts, option_string)


# https://pdfs.semanticscholar.org/e065/3631b4a476abf5276a264f6bbff40b132061.pdf
"""
Average Confirmation Time Ave. time to accept transaction in block
Block Size Average block size in MB
Cost per transaction percent Miners revenue divided by the number of transactions
Difficulty How difficult it is to find a new block

Estimated Transaction Volume Total output volume without change from value
Hash Rate Bitcoin network giga hashes per second
Market Capitalization Number of Bitcoins in circulation * the market price
Miners Revenue (number of BTC mined/day * market price) + transaction fees
Number of Orphaned Blocks Number of blocks mined / day not off blockchain

Number of TXN per block Average number of transactions per block
Number of TXN Total number of unique Bitcoin transactions per day
Number of unique addresses Number of unique Bitcoin addresses used per day
Total Bitcoins Historical total Number of Bitcoins mined
TXN Fees Total BTC value of transaction fees miners earn/day

missing - Trade Volume USD trade volume from the top exchanges - because different nr of rows
missing - Transaction to trade ratio Relationship of BTC transaction volume and USD volume - no precalculated ratio
"""
