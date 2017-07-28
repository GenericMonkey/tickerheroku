from googlefinance import getQuotes
from yahoo_finance import Share


def parseStock(ticker):
    stock = Share(ticker)
    opening = float(stock.get_open())
    tickerVals = {}
    tickerVals['name'] = ticker
    tickerVals['price'] = float(getQuotes(ticker)[0]['LastTradePrice'])
    tickerVals['pricechange'] = (tickerVals['price'] - opening)
    tickerVals['percentchange'] = tickerVals['pricechange'] / opening
    return tickerVals





if __name__ == '__main__':
    parseStock('AAPL')
