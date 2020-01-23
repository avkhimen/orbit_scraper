import time
from datetime import datetime

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

def get_prices_and_record_into_database(start_url, session):
	while True:
		try:
			currency_prices_and_volumes = CurrencyPricesVolumes(start_url, session)
		except Exception as e:
			print(e)
		else:
			currency_prices_and_volumes.record_into_database()
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
		self.coinsquare_prices_volumes = CoinsquarePricesVolumes()
		self.bittrex_prices_volumes = BittrexPricesVolumes()

	def record_into_database(self):
		pass

	def get_prices(self):
		coinsquare_prices = self.coinsquare_prices_volumes.get_prices()
		bittrex_prices = self.bittrex_prices_volumes.get_prices()

		return coinsquare_prices, bittrex_prices

	def get_volumes(self):
		coinsquare_volumes = self.coinsquare_prices_volumes.get_volumes()
		bittrex_volumes = self.bittrex_prices_volumes.get_volumes()

		return coinsquare_volumes, bittrex_volumes

	def create_record(self):
		entry = {
		"RIPPLE":RIPPLE_cancelled_orders, \
		"DASH":DASH_cancelled_orders, \
		"ATOM":ATOM_cancelled_orders,
		"MONERO":MONERO_cancelled_orders, \
		"STELLAR":STELLAR_cancelled_orders, \
		"ETC_CLASSIC":ETC_CLASSIC_cancelled_orders
		}[self.currency]( \
			timestamp = self.timestamp, \
			txid = self.txid, \
			order_type = self.order_type)
		self.session.add(entry)
		self.session.commit()


class TextNotification():
	def __init__(self):
		pass

	def send_notification(self):
		if self.check_notification():
			pass

	def check_notification(self):
		pass

class CoinsquarePricesVolumes():
	def __init__(self):
		pass

	def get_prices(self):
		pass

	def get_volumes(self):
		pass

class BittrexPricesVolumes():
	def __init__(self):
		pass

	def get_prices(self):
		pass

	def get_volumes(self):
		pass

class PriceVolumePair():
	def __init__(self, price, volume):
		self.price = price
		self.volume = volume
