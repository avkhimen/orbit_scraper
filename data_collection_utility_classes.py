from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from datetime import datetime
import requests
from concurrent.futures import ThreadPoolExecutor
from pprint import pprint
from database_setup import CoinsquareDogePricesVolumes, BittrexDogePricesVolumes

def get_prices_and_record_into_database(start_url, session):
	while True:
		try:
			currency_prices_volumes = CurrencyPricesVolumes(start_url, session)
			currency_prices_volumes.record_into_database()
		except Exception as e:
			print(e)
		else:
			current_time = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
			print(current_time + " Collecting prices/volumes"\
			" task finished. Sleep 25s")
			time.sleep(30)
		finally:
			True

class CurrencyPricesVolumes():
	def __init__(self, start_url, session):
		self.start_url = start_url
		self.session = session
		self.coinsquare_prices_volumes = CoinsquarePricesVolumes(self.start_url)
		self.bittrex_prices_volumes = BittrexPricesVolumes()

	def record_into_database(self):

		self.record_coinsquare_prices_and_volumes()
		self.record_bittrex_prices_and_volumes()

	def record_coinsquare_prices_and_volumes(self):
		orderbook = self.coinsquare_prices_volumes.get_orderbook()

		timestamp = self.coinsquare_prices_volumes.get_timestamp()

		db_entry = CoinsquareDogePricesVolumes(
			timestamp = timestamp,
		    price_ask_15 = orderbook['ask_15']['price'],
		    volume_ask_15 = orderbook['ask_15']['volume'],
		    price_ask_14 = orderbook['ask_14']['price'],
		    volume_ask_14 = orderbook['ask_14']['volume'],
		    price_ask_13 = orderbook['ask_13']['price'],
		    volume_ask_13 = orderbook['ask_13']['volume'],
		    price_ask_12 = orderbook['ask_12']['price'],
		    volume_ask_12= orderbook['ask_12']['volume'],
		    price_ask_11 = orderbook['ask_11']['price'],
		    volume_ask_11 = orderbook['ask_11']['volume'],
		    price_ask_10 = orderbook['ask_10']['price'],
		    volume_ask_10 = orderbook['ask_10']['volume'],
		    price_ask_9 = orderbook['ask_9']['price'],
		    volume_ask_9 = orderbook['ask_9']['volume'],
		    price_ask_8 = orderbook['ask_8']['price'],
		    volume_ask_8 = orderbook['ask_8']['volume'],
		    price_ask_7 = orderbook['ask_7']['price'],
		    volume_ask_7 = orderbook['ask_7']['volume'],
		    price_ask_6 = orderbook['ask_6']['price'],
		    volume_ask_6 = orderbook['ask_6']['volume'],
		    price_ask_5 = orderbook['ask_5']['price'],
		    volume_ask_5 = orderbook['ask_5']['volume'],
		    price_ask_4 = orderbook['ask_4']['price'],
		    volume_ask_4 = orderbook['ask_4']['volume'],
		    price_ask_3 = orderbook['ask_3']['price'],
		    volume_ask_3 = orderbook['ask_3']['volume'],
		    price_ask_2 = orderbook['ask_2']['price'],
		    volume_ask_2 = orderbook['ask_2']['volume'],
		    price_ask_1 = orderbook['ask_1']['price'],
		    volume_ask_1 = orderbook['ask_1']['volume'],
		    price_bid_1 = orderbook['bid_1']['price'],
		    volume_bid_1 = orderbook['bid_1']['volume'],
		    price_bid_2 = orderbook['bid_2']['price'],
		    volume_bid_2 = orderbook['bid_2']['volume'],
		    price_bid_3 = orderbook['bid_3']['price'],
		    volume_bid_3 = orderbook['bid_3']['volume'],
		    price_bid_4 = orderbook['bid_4']['price'],
		    volume_bid_4 = orderbook['bid_4']['volume'],
		    price_bid_5 = orderbook['bid_5']['price'],
		    volume_bid_5 = orderbook['bid_5']['volume'],
		    price_bid_6 = orderbook['bid_6']['price'],
		    volume_bid_6 = orderbook['bid_6']['volume'],
		    price_bid_7 = orderbook['bid_7']['price'],
		    volume_bid_7 = orderbook['bid_7']['volume'],
		    price_bid_8 = orderbook['bid_8']['price'],
		    volume_bid_8 = orderbook['bid_8']['volume'],
		    price_bid_9 = orderbook['bid_9']['price'],
		    volume_bid_9 = orderbook['bid_9']['volume'],
		    price_bid_10 = orderbook['bid_10']['price'],
		    volume_bid_10 = orderbook['bid_10']['volume'],
		    price_bid_11 = orderbook['bid_11']['price'],
		    volume_bid_11 = orderbook['bid_11']['volume'],
		    price_bid_12 = orderbook['bid_12']['price'],
		    volume_bid_12 = orderbook['bid_12']['volume'],
		    price_bid_13 = orderbook['bid_13']['price'],
		    volume_bid_13 = orderbook['bid_13']['volume'],
		    price_bid_14 = orderbook['bid_14']['price'],
		    volume_bid_14 = orderbook['bid_14']['volume'],
		    price_bid_15 = orderbook['bid_15']['price'],
		    volume_bid_15 = orderbook['bid_15']['volume'],
		    compared = 'False')
		self.session.add(db_entry)
		self.session.commit()

	def record_bittrex_prices_and_volumes(self):
		orderbook = self.bittrex_prices_volumes.get_orderbook()

		timestamp = self.bittrex_prices_volumes.get_timestamp()

		db_entry = BittrexDogePricesVolumes(
			timestamp = timestamp,
		    price_ask_15 = orderbook['ask_15']['price'],
		    volume_ask_15 = orderbook['ask_15']['volume'],
		    price_ask_14 = orderbook['ask_14']['price'],
		    volume_ask_14 = orderbook['ask_14']['volume'],
		    price_ask_13 = orderbook['ask_13']['price'],
		    volume_ask_13 = orderbook['ask_13']['volume'],
		    price_ask_12 = orderbook['ask_12']['price'],
		    volume_ask_12= orderbook['ask_12']['volume'],
		    price_ask_11 = orderbook['ask_11']['price'],
		    volume_ask_11 = orderbook['ask_11']['volume'],
		    price_ask_10 = orderbook['ask_10']['price'],
		    volume_ask_10 = orderbook['ask_10']['volume'],
		    price_ask_9 = orderbook['ask_9']['price'],
		    volume_ask_9 = orderbook['ask_9']['volume'],
		    price_ask_8 = orderbook['ask_8']['price'],
		    volume_ask_8 = orderbook['ask_8']['volume'],
		    price_ask_7 = orderbook['ask_7']['price'],
		    volume_ask_7 = orderbook['ask_7']['volume'],
		    price_ask_6 = orderbook['ask_6']['price'],
		    volume_ask_6 = orderbook['ask_6']['volume'],
		    price_ask_5 = orderbook['ask_5']['price'],
		    volume_ask_5 = orderbook['ask_5']['volume'],
		    price_ask_4 = orderbook['ask_4']['price'],
		    volume_ask_4 = orderbook['ask_4']['volume'],
		    price_ask_3 = orderbook['ask_3']['price'],
		    volume_ask_3 = orderbook['ask_3']['volume'],
		    price_ask_2 = orderbook['ask_2']['price'],
		    volume_ask_2 = orderbook['ask_2']['volume'],
		    price_ask_1 = orderbook['ask_1']['price'],
		    volume_ask_1 = orderbook['ask_1']['volume'],
		    price_bid_1 = orderbook['bid_1']['price'],
		    volume_bid_1 = orderbook['bid_1']['volume'],
		    price_bid_2 = orderbook['bid_2']['price'],
		    volume_bid_2 = orderbook['bid_2']['volume'],
		    price_bid_3 = orderbook['bid_3']['price'],
		    volume_bid_3 = orderbook['bid_3']['volume'],
		    price_bid_4 = orderbook['bid_4']['price'],
		    volume_bid_4 = orderbook['bid_4']['volume'],
		    price_bid_5 = orderbook['bid_5']['price'],
		    volume_bid_5 = orderbook['bid_5']['volume'],
		    price_bid_6 = orderbook['bid_6']['price'],
		    volume_bid_6 = orderbook['bid_6']['volume'],
		    price_bid_7 = orderbook['bid_7']['price'],
		    volume_bid_7 = orderbook['bid_7']['volume'],
		    price_bid_8 = orderbook['bid_8']['price'],
		    volume_bid_8 = orderbook['bid_8']['volume'],
		    price_bid_9 = orderbook['bid_9']['price'],
		    volume_bid_9 = orderbook['bid_9']['volume'],
		    price_bid_10 = orderbook['bid_10']['price'],
		    volume_bid_10 = orderbook['bid_10']['volume'],
		    price_bid_11 = orderbook['bid_11']['price'],
		    volume_bid_11 = orderbook['bid_11']['volume'],
		    price_bid_12 = orderbook['bid_12']['price'],
		    volume_bid_12 = orderbook['bid_12']['volume'],
		    price_bid_13 = orderbook['bid_13']['price'],
		    volume_bid_13 = orderbook['bid_13']['volume'],
		    price_bid_14 = orderbook['bid_14']['price'],
		    volume_bid_14 = orderbook['bid_14']['volume'],
		    price_bid_15 = orderbook['bid_15']['price'],
		    volume_bid_15 = orderbook['bid_15']['volume'],
		    compared = 'False')
		self.session.add(db_entry)
		self.session.commit()

class CoinsquarePricesVolumes():
	"""Returns the prices and volumes dictionary and a timestamp"""
	def __init__(self, start_url):
		self.start_url = start_url

	def get_prices_volumes(self):
	    """Returns the dict of latest DOGE price-volume pairs from Coinsquare exchange"""

	    options = Options()
	    options.headless = True
	    driver = webdriver.Firefox(options=options)

	    price_volume_dict = {}

	    try:
	        driver.get(self.start_url)
	        time.sleep(20)
	    except Exception as e:
	        print('Failed to load site 1st time')
	        try:
	            print('Attemping to load site again')
	            driver.get(self.start_url)
	            time.sleep(20)
	        except Exception as e:
	            print("Couldn't load site")
	            return False

	    #Get ask price and volume
	    i = 1

	    while i < 16:
	        try:
	            xpath_path = "/html/body/div[1]/div/div[2]/div[3]/div[2]/div"\
	            "[2]/div/div/div[2]/div/div[3]/div[1]/div[" + str(i) + "]/div[1]/div[2]"
	            ask_price = driver.find_element_by_xpath(xpath_path).get_attribute('innerHTML')
	            
	            xpath_path = "/html/body/div[1]/div/div[2]/div[3]/div[2]/div["\
	            "2]/div/div/div[2]/div/div[3]/div[1]/div[" + str(i) + "]/div[1]/div[1]"
	            ask_volume = driver.find_element_by_xpath(xpath_path).get_attribute('innerHTML')

	            price_volume_dict['ask_' + str(16-i)] = {'volume': ask_volume, 'price': ask_price}

	        except Exception as e:
	            print(e)
	            price_volume_dict['ask_' + str(16-i)] = {'volume': 'scrape_error', 'price': 'scrape_error'}
	        finally:
	            i += 1

	    #Get bid price and volume
	    i = 1

	    while i < 16:
	        try:
	            xpath_path = "/html/body/div[1]/div/div[2]/div[3]/div[2]/div[2"\
	            "]/div/div/div[2]/div/div[3]/div[3]/div[" + str(i) + "]/div[1]/div[2]"
	            bid_price = driver.find_element_by_xpath(xpath_path).get_attribute('innerHTML')
	            
	            xpath_path = "/html/body/div[1]/div/div[2]/div[3]/div[2]/div[2]/"\
	            "div/div/div[2]/div/div[3]/div[3]/div[" + str(i) + "]/div[1]/div[1]"
	            bid_volume = driver.find_element_by_xpath(xpath_path).get_attribute('innerHTML')

	            price_volume_dict['bid_' + str(i)] = {'volume': bid_volume, 'price': bid_price}

	        except Exception as e:
	            print(e)
	            price_volume_dict['bid_' + str(i)] = {'volume': 'scrape_error', 'price': 'scrape_error'}
	        finally:
	            i += 1

	    driver.close()

	    #Get timestamp
	    timestamp = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

	    return price_volume_dict, timestamp

	def get_orderbook(self):
		"""Returns the dict of doge prices and volumes"""
		orderbook = self.get_prices_volumes()[0]

		return orderbook

	def get_timestamp(self):
		"""Returns the timestamp of orderbook"""
		timestamp = self.get_prices_volumes()[1]

		return timestamp

class BittrexPricesVolumes():
	"""Returns the prices and volumes dictionary and a timestamp"""
	def __init__(self):
		pass

	def get_prices_volumes(self):
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

		#Get timestamp
		timestamp = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

		return price_volume_dict, timestamp

	def get_orderbook(self):
		"""Returns the dict of doge prices and volumes"""
		orderbook = self.get_prices_volumes()[0]

		return orderbook

	def get_timestamp(self):
		"""Returns the timestamp of orderbook"""
		timestamp = self.get_prices_volumes()[1]

		return timestamp
