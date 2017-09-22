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
                            words = x['message']['text'].split()
                            for word in words:
                                if word[0] == '{' and word[-1] == '}':
                                    stocksymbol = word[1:-1]
                                    stockinfo = parseStock(stocksymbol)
                                    message = stockinfo['name'] + " " + str(stockinfo['price']) + " " + str(stockinfo['pricechange']) + " (" + str(stockinfo['percentchange']) + "%)"
                                    bot.send_text_message(recipient_id, message)
                    else:
                        pass
        except:
            return "Foreign Post Type"
        return "Success"


if __name__ == "__main__":
    app.run(port=5002, debug=True)
