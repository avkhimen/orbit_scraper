import requests
from pprint import pprint

def main():
	"""Main program controller"""
	order_book = get_bittrex_prices_volumes()
	pprint(order_book)

def get_bittrex_prices_volumes():
	"""Returns the dict of latest DOGE price-volume pairs from Bittrex exchange"""

	r = requests.get('https://api.bittrex.com/api/v1.1/public/getorderbook?market=BTC-DOGE&type=both')

	order_book = r.json()['result']

	price_volume_dict = {}

	#Get ask price and volume
	i = 1

	while i < 16:
	    try:
	        ask_price = order_book['sell'][i]['Rate']
	        
	        ask_volume = order_book['sell'][i]['Quantity']

	        price_volume_dict['ask_' + str(i)] = {'volume': ask_volume, 'price': ask_price}

	    except Exception as e:
	        print(e)
	        price_volume_dict['ask_' + str(i)] = {'volume': 'scrape_error', 'price': 'scrape_error'}
	    finally:
	        i += 1

	#Get bid price and volume
	i = 1

	while i < 16:
	    try:
	        bid_price = order_book['buy'][i]['Rate']
	        
	        bid_volume = order_book['buy'][i]['Quantity']

	        price_volume_dict['bid_' + str(i)] = {'volume': bid_volume, 'price': bid_price}

	    except Exception as e:
	        print(e)
	        price_volume_dict['bid_' + str(i)] = {'volume': 'scrape_error', 'price': 'scrape_error'}
	    finally:
	        i += 1

	return price_volume_dict


if __name__ == '__main__':
	main()