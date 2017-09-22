from yahoo_finance import Share


def parseStock(ticker):
    try:
        stock = Share(ticker)
        opening = float(stock.get_open())
        current = float(stock.get_price())
        tickerVals = {}
        tickerVals['name'] = stock.get_name()
        tickerVals['price'] = round(current, 2)
        tickerVals['pricechange'] = round((tickerVals['price'] - opening), 2)
        tickerVals['percentchange'] = round(((tickerVals['pricechange'] / opening) * 100), 2)
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
