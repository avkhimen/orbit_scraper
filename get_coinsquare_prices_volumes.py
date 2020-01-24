
from pprint import pprint
from utility_classes import CoinsquarePricesVolumes

def main():
    """Main program controller"""
    coinsquare_prices_volumes = CoinsquarePricesVolumes('https://coinsquare.com/trade?pair=DOGE-BTC')
    order_book, timestamp = coinsquare_prices_volumes.get_prices_volumes()
    pprint(order_book)
    print(timestamp)

class Error(Exception):
    """Returns basic exception class"""
    pass

class NoSuchElementException(Error):
    """Returned when xpath element couldn't be located"""
    pass

if __name__ == '__main__':
    main()