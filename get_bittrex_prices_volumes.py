from pprint import pprint
from utility_classes import BittrexPricesVolumes

def main():
	"""Main program controller"""
	bittrex_prices_volumes = BittrexPricesVolumes()
	order_book, timestamp = bittrex_prices_volumes.get_prices_volumes()
	pprint(order_book)
	print(timestamp)

if __name__ == '__main__':
	main()