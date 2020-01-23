import requests
from ast import literal_eval
from pprint import pprint

buy_or_sell = 'both'

r = requests.get('https://api.bittrex.com/api/v1.1/public/getorderbook?market=BTC-DOGE&type=' + buy_or_sell)

order_book = r.json()['result']

price_volume_dict = {}


i = 1

while i < 16:
    try:
        ask_price = order_book['sell'][i]['Rate']
        
        ask_volume = order_book['sell'][i]['Quantity']

        price_volume_dict['ask_' + str(i)] = {'volume': ask_volume, 'price': ask_price}

    except Exception as e:
        print(e)
    finally:
        i += 1

i = 1

while i < 16:
    try:
        bid_price = order_book['buy'][i]['Rate']
        
        bid_volume = order_book['buy'][i]['Quantity']

        price_volume_dict['bid_' + str(i)] = {'volume': bid_volume, 'price': bid_price}

    except Exception as e:
        print(e)
    finally:
        i += 1

pprint(price_volume_dict)