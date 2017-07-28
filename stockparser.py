from googlefinance import getQuotes
from yahoo_finance import Share


def parseStock(ticker):
    stock = Share(ticker)
    opening = float(stock.get_open())
    tickerVals = {}
    tickerVals['name'] = ticker
    tickerVals['price'] = round(float(getQuotes(ticker)[0]['LastTradePrice']), 2)
    tickerVals['pricechange'] = round((tickerVals['price'] - opening), 2)
    tickerVals['percentchange'] = round((tickerVals['pricechange'] / opening), 2)
    print( tickerVals)





if __name__ == '__main__':
    parseStock('AAPL')
