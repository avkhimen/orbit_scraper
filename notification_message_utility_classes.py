import time
from datetime import datetime
from database_setup import CoinsquareDogePricesVolumes
from database_setup import BittrexDogePricesVolumes
from database_setup import BidAkPriceVolumeComparison
from twilio.rest import Client
from keys.twilio_sid_token import ACCOUNT_SID, AUTH_TOKEN
from pprint import pprint

def send_text_notification(session):
	while True:
		try:
			text_notification = TextNotification(session)
		except Exception as e:
			print(e)
		else:
			notification_sent = text_notification.check_if_need_notification()
			print('________Printing if notification needs to be sent: ', notification_sent)
			if notification_sent:
				text_notification.send_notification()
			text_notification.update_database(notification_sent)
			current_time = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
			print(current_time + " Notification task finished. Sleep 20s.")
			time.sleep(20)
		finally:
			True

class TextNotification():
	def __init__(self, session):
		self.session = session
		self.price_volume_dict = self.get_coinsquare_bittrex_prices_volumes_compared()
		self.bittrex_price_ask_1 = self.price_volume_dict['bittrex_price_ask_1']
		self.bittrex_volume_ask_1 = self.price_volume_dict['bittrex_volume_ask_1']
		self.bittrex_price_bid_1 = self.price_volume_dict['bittrex_price_bid_1']
		self.bittrex_volume_bid_1 = self.price_volume_dict['bittrex_volume_bid_1']
		self.bittrex_compared = self.price_volume_dict['bittrex_compared']
		self.coinsquare_price_ask_1 = self.price_volume_dict['coinsquare_price_ask_1']
		self.coinsquare_volume_ask_1 = self.price_volume_dict['coinsquare_volume_ask_1']
		self.coinsquare_price_bid_1 = self.price_volume_dict['coinsquare_price_bid_1']
		self.coinsquare_volume_bid_1 = self.price_volume_dict['coinsquare_volume_bid_1']
		self.coinsquare_compared = self.price_volume_dict['coinsquare_compared']

	def get_coinsquare_bittrex_prices_volumes_compared(self):
		coinsquare_last_entry = self.session.query(CoinsquareDogePricesVolumes).\
		order_by(CoinsquareDogePricesVolumes.id.desc()).first()
		bittrex_last_entry = self.session.query(BittrexDogePricesVolumes).\
		order_by(BittrexDogePricesVolumes.id.desc()).first()
		prices_dict = {}
		prices_dict['coinsquare_price_ask_1'] = self.convert_to_float(coinsquare_last_entry.price_ask_1)
		prices_dict['coinsquare_price_bid_1'] = self.convert_to_float(coinsquare_last_entry.price_bid_1)
		prices_dict['coinsquare_volume_ask_1'] = self.convert_to_float(coinsquare_last_entry.volume_ask_1)
		prices_dict['coinsquare_volume_bid_1'] = self.convert_to_float(coinsquare_last_entry.volume_bid_1)
		prices_dict['coinsquare_compared'] = coinsquare_last_entry.compared
		prices_dict['bittrex_price_ask_1'] = self.convert_to_float(bittrex_last_entry.price_ask_1)
		prices_dict['bittrex_price_bid_1'] = self.convert_to_float(bittrex_last_entry.price_bid_1)
		prices_dict['bittrex_volume_ask_1'] = self.convert_to_float(bittrex_last_entry.volume_ask_1)
		prices_dict['bittrex_volume_bid_1'] = self.convert_to_float(bittrex_last_entry.volume_bid_1)
		prices_dict['bittrex_compared'] = bittrex_last_entry.compared

		return prices_dict

	def convert_to_float(self, x):
		try:
			return float(x.replace(',',''))
		except Exception as e:
			return x

	def check_if_need_notification(self):
		print('________Check if need notification method about to execute')
		if self.compare_bids_and_asks():
			return True
		else:
			return False

	def compare_bids_and_asks(self):
		print('________Compare bids and asks method executing')
		if self.no_scrape_errors():
			if self.data_not_looked_at():
				if self.coinsquare_price_ask_1 < self.bittrex_price_bid_1 or self.coinsquare_price_bid_1 > self.bittrex_price_ask_1:
					if self.bittrex_volume_ask_1 > 160000 and self.bittrex_volume_bid_1 > 160000 and self.coinsquare_volume_ask_1 > 160000 and self.coinsquare_volume_bid_1 > 160000:
						return True
		else:
			return False

	def no_scrape_errors(self):
		print('________No scrape errors method executing')
		price_list = [self.coinsquare_price_ask_1, self.bittrex_price_bid_1, self.coinsquare_price_bid_1, self.bittrex_price_ask_1]
		if 'scrape_error' not in price_list:
			return True
		else:
			return False

	def data_not_looked_at(self):
		print('________Data not looked at method executing')
		if self.bittrex_compared == 'False' and self.coinsquare_compared == 'False':
			return True
		else:
			return False

	def send_notification(self):
		message = self.construct_message()
		self.send_message(message)

	def construct_message(self):
		if self.coinsquare_price_ask_1 < self.bittrex_price_bid_1:
			return "Buy on Coinsquare for {} and sell on Bittrex for {}".format(self.coinsquare_price_ask_1, self.bittrex_price_bid_1)
		elif self.coinsquare_price_bid_1 > self.bittrex_price_ask_1:
			return "Buy on Bittrex for {} and sell on Coinsquare for {}".format(self.bittrex_price_ask_1, self.coinsquare_price_bid_1)

	def send_message(self, message):
		print('________Send message method executing')
		try:
			account_sid = ACCOUNT_SID
			auth_token = AUTH_TOKEN
			client = Client(account_sid, auth_token)

			text_message = client.messages.create(body=message, from_='+12012124816', to='+17809321716')
		except Exception as e:
			print(e)
		else:
			return True

	def update_database(self, notification_sent):
		print('________Update database method executing')
		try:
			self.update_price_volume_tables(self, notification_sent)
		except Exception as e:
			print(e)
		try:
			self.record_into_comparison_table(self, notification_sent)
		except Exception as e:
			print(e)
		print('________Update database method finished')

	@staticmethod
	def update_price_volume_tables(self, notification_sent):
		print('________Update price volume method executing')
		message_sent_update = 'message_not_sent'
		if notification_sent:
			message_sent_update = 'message_sent'
			

		coinsquare_last_entry = self.session.query(CoinsquareDogePricesVolumes).order_by(CoinsquareDogePricesVolumes.id.desc()).first()
		bittrex_last_entry = self.session.query(BittrexDogePricesVolumes).order_by(BittrexDogePricesVolumes.id.desc()).first()
		
		coinsquare_last_entry.compared = message_sent_update
		bittrex_last_entry.compared = message_sent_update

		self.session.commit()

	@staticmethod
	def record_into_comparison_table(self, notification_sent):
		print('________Record into comparison table method executing')
		compared = 'False'
		if notification_sent:
			compared = 'True'

		timestamp = self.get_current_time_timestamp()
		
		db_entry = BidAkPriceVolumeComparison(
			timestamp = timestamp,
		    coinsquare_price_ask_1 = self.coinsquare_price_ask_1,
		    bittrex_price_ask_1 = self.bittrex_price_ask_1,
		    coinsquare_volume_ask_1 = self.coinsquare_volume_ask_1,
		    bittrex_volume_ask_1 = self.bittrex_volume_ask_1,
		    coinsquare_price_bid_1 = self.coinsquare_price_bid_1,
		    bittrex_price_bid_1 = self.bittrex_price_bid_1,
		    coinsquare_volume_bid_1 = self.coinsquare_volume_bid_1,
		    bittrex_volume_bid_1 = self.bittrex_volume_bid_1,
		    message_sent = compared)

		self.session.add(db_entry)
		self.session.commit()

	def get_current_time_timestamp(self):

		timestamp = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

		return timestamp