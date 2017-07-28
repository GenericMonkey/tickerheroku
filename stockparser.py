from googlefinance import getQuotes
from yahoo_finance import Share


def parseStock(ticker):
    try:
        stock = Share(ticker)
        opening = float(stock.get_open())
        current = getQuotes(ticker)[0]
        tickerVals = {}
        tickerVals['name'] = current['StockSymbol']
        tickerVals['price'] = round(float(current['LastTradePrice']), 2)
        tickerVals['pricechange'] = round((tickerVals['price'] - opening), 2)
        tickerVals['percentchange'] = round((tickerVals['pricechange'] / opening), 2)
        return tickerVals
    except:
        tickerVals = {}
        tickerVals['name'] = 'NOTFOUND'
        tickerVals['price'] = 0
        tickerVals['pricechange'] = 0
        tickerVals['percentchange'] = 0
        return tickerVals




if __name__ == '__main__':
    print (parseStock('Aapl'))
