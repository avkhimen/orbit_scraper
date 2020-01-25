import time
from datetime import datetime
from database_setup import CoinsquareDogePricesVolumes
from twilio.rest import Client

def send_text_notification(session):
	while True:
		try:
			text_notification = TextNotification()
		except Exception as e:
			print(e)
		else:
			text_notification.check_notification()
			time.sleep(10)
			current_time = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
			print("Send notification sleep 10s " + current_time)
		finally:
			True

	#class PriceVolumeComparisonData()
		#def __init__(self):
			#Get data from price_volume table
			#self.bittrex_ask_1_price = bittrex_ask_1_price
			#self.bittrex_bid_1_price = bittrex_ask_1_price
		#def compare_data(self):
			#Compare bid ask data from price_volume table
			# if bittrex_bid_1_volume > 160,000 dogecoin and 
			#return True/False
	#Determine if message must be sent
		#def send_message_or_not():
			#if compare_date():
				#send_text_message()
	#Sent message if necessary
		#def send_text_message(self):
			#Use twilio api to send text message
			#Return True/False
	#Push data into comparison table

	#Mark data as compared in price_volume table

class TextNotification():
	def __init__(self, session, price_volume_dict):
		self.session = session
		self.price_volume_dict = self.get_coinsquare_bittrex_prices_volumes()
		self.bittrex_price_ask_1 = self.price_volume_dict['bittrex_price_ask_1']
		self.bittrex_volume_ask_1 = self.price_volume_dict['bittrex_volume_ask_1']
		self.bittrex_price_bid_1 = self.price_volume_dict['bittrex_price_bid_1']
		self.bittrex_volume_bid_1 = self.price_volume_dict['bittrex_volume_bid_1']
		self.coinsquare_price_ask_1 = self.price_volume_dict['coinsquare_price_ask_1']
		self.coinsquare_volume_ask_1 = self.price_volume_dict['coinsquare_volume_ask_1']
		self.coinsquare_price_bid_1 = self.price_volume_dict['coinsquare_price_bid_1']
		self.coinsquare_volume_bid_1 = self.price_volume_dict['coinsquare_volume_bid_1']

	def compare_bids_and_asks(self):
		if self.no_scrape_errors():
			if self.coinsquare_price_ask_1 < self.bittrex_price_bid_1 or self.coinsquare_price_bid_1 > self.bittrex_price_ask_1:
				if self.bittrex_volume_ask_1 > 160000 and self.bittrex_volume_bid_1 > 160000 and self.coinsquare_volume_ask_1 > 160000 and self.coinsquare_volume_bid_1 > 160000:
					return True
			else:
				return False
		else:
			return False

	def no_scrape_errors(self):
		price_list = [self.coinsquare_price_ask_1, self.bittrex_price_bid_1, self.coinsquare_price_bid_1, self.bittrex_price_ask_1]
		if 'scrape_error' not in price_list:
			return True
		else:
			return False

	def get_coinsquare_bittrex_prices_volumes(self):
		coinsquare_last_entry = self.session.query(CoinsquareDogePricesVolumes).\
		order_by(CoinsquareDogePricesVolumes.id.desc()).first()
		bittrex_last_entry = self.session.query(BittrexDogePricesVolumes).\
		order_by(BittrexDogePricesVolumes.id.desc()).first()
		prices_dict = {}
		prices_dict['coinsquare_price_ask_1'] = coinsquare_last_entry.price_ask_1
		prices_dict['coinsquare_price_bid_1'] = coinsquare_last_entry.price_bid_1
		prices_dict['coinsquare_volume_ask_1'] = coinsquare_last_entry.volume_ask_1
		prices_dict['coinsquare_volume_bid_1'] = coinsquare_last_entry.volume_bid_1
		prices_dict['bittrex_price_ask_1'] = bittrex_last_entry.price_ask_1
		prices_dict['bittrex_price_bid_1'] = bittrex_last_entry.price_bid_1
		prices_dict['bittrex_volume_ask_1'] = bittrex_last_entry.volume_ask_1
		prices_dict['bittrex_volume_bid_1'] = bittrex_last_entry.volume_bid_1

		return prices_dict

	def check_for_notification(self):
		if self.compare_bids_and_asks():
			self.send_notification()

	def send_notification(self):
		pass

class TextNotification():
	def __init__(self):
		pass

	def send_notification(self):
		if self.check_notification():
			pass

	def check_notification(self):
		pass
