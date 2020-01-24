from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from datetime import datetime
import requests

def send_text_notification(session):
	while True:
		try:
			text_notification = TextNotification()
		except Exception as e:
			print(e)
		else:
			text_notification.check_notification()
			time.sleep(5)
			now = datetime.now()
			current_time = now.strftime("%H:%M:%S")
			print("Send notification sleep 5s " + current_time)
		finally:
			True

class TextNotification():
	def __init__(self):
		pass

	def send_notification(self):
		if self.check_notification():
			pass

	def check_notification(self):
		pass

def get_prices_and_record_into_database(start_url, session):
	while True:
		try:
			currency_prices_volumes = CurrencyPricesVolumes(start_url, session)
			print('Created currency_prices_volumes obj')
		except Exception as e:
			print(e)
		else:
			#currency_prices_volumes.record_into_database()
			print('CurrencyPricesVolumes obj has been created')
			currency_prices_volumes.test()
			time.sleep(2)
			now = datetime.now()
			current_time = now.strftime("%H:%M:%S")
			print("Prices and database sleep 2s " + current_time)
		finally:
			True

class CurrencyPricesVolumes():
	def __init__(self, start_url, session):
		self.start_url = start_url
		self.session = session
		# with ThreadPoolExecutor(max_workers=2) as executor:
		# 	future = executor.submit(CoinsquarePricesVolumes, (self.start_url))
		# 	future = executor.submit(BittrexPricesVolumes)
		self.coinsquare_prices_volumes = CoinsquarePricesVolumes(self.start_url)
		self.bittrex_prices_volumes = BittrexPricesVolumes()

	# def get_prices(self):
	# 	coinsquare_prices, timestamp = self.coinsquare_prices_volumes.get_prices_volumes()
	# 	bittrex_prices = self.bittrex_prices_volumes.get_prices()

	# 	return coinsquare_prices, bittrex_prices

	# def get_volumes(self):
	# 	coinsquare_volumes = self.coinsquare_prices_volumes.get_volumes()
	# 	bittrex_volumes = self.bittrex_prices_volumes.get_volumes()

	# 	return coinsquare_volumes, bittrex_volumes

	def record_into_database(self):
		entry = {
		"COINSQUARE":RIPPLE_cancelled_orders, \
		"DASH":DASH_cancelled_orders
		}[self.currency]( \
			timestamp = self.timestamp, \
			txid = self.txid, \
			order_type = self.order_type)
		self.session.add(entry)
		self.session.commit()

	def test(self):
		pass
		# now = datetime.now()
		# current_time = now.strftime("%H:%M:%S")
		# print("Prices and database sleep 2s " + current_time)

class CoinsquarePricesVolumes():
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
	        time.sleep(10)
	    except Exception as e:
	        print('Failed to load site 1st time')
	        try:
	            print('Attemping to load site again')
	            driver.get(self.start_url)
	            time.sleep(10)
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
	            time.sleep(0.0)

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
	            time.sleep(0.0)

	    driver.close()

	    #Get timestamp
	    timestamp = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

	    return price_volume_dict, timestamp

class BittrexPricesVolumes():
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
