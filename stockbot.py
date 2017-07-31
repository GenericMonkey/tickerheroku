"""
This bot listens to port 5002 for incoming connections from Facebook. It takes
in any messages that the bot receives and echos it back.
"""
from flask import Flask, request
from pymessenger.bot import Bot
from stockparser import parseStock
app = Flask(__name__)

ACCESS_TOKEN = "EAAESyTSZAuIwBAO94G27EtXBit7WJZC0v6AzpxVjrZCoXvZCTsqaMUmMwBk4puIKY4vjRk8UCjl9cuGxky77nMmxgphoKWZBrkUdnZCWOJaBamMZAZAW8mZAbSer1u8pbUi031ZCt5FwLzu2CBhnzm07SDqFuioo4SIrDaPWaDnMLYYgZDZD"
VERIFY_TOKEN = "tickersarecool"
bot = Bot(ACCESS_TOKEN)


@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        else:
            return 'Invalid verification token'

    if request.method == 'POST':
        try:
            output = request.get_json()
            for event in output['entry']:
                messaging = event['messaging']
                for x in messaging:
                    if x.get('message'):
                        recipient_id = x['sender']['id']
                        if x['message'].get('text'):
                            stocksymbol = x['message']['text']
                            if stocksymbol == 'help':
                                helpmessage = "Welcome to TickerBot! Enter a Stock Symbol to get current pricing information! Ex. FB, AAPL, GOOGL"
                            stockinfo = parseStock(stocksymbol)
                            elements = []
                            titlemessage = stockinfo['name'] + " " + str(stockinfo['price'])
                            submessage = str(stockinfo['pricechange']) + " (" + str(stockinfo['percentchange']) + "%)"
                            element = Element(title=titlemessage, subtitle=submessage)
                            elements.append(element)
                            bot.send_generic_message(recipient_id, elements)
                            # message = stockinfo['name'] + " " + str(stockinfo['price']) + " " + str(stockinfo['pricechange']) + " (" + str(stockinfo['percentchange']) + "%)"
                            # bot.send_text_message(recipient_id, message)
                        if x['message'].get('attachments'):
                            for att in x['message'].get('attachments'):
                                bot.send_attachment_url(recipient_id, att['type'], att['payload']['url'])
                    else:
                        pass
        except:
            return "Foreign Post Type"
        return "Success"


if __name__ == "__main__":
    app.run(port=5002, debug=True)
