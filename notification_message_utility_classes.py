import time
from datetime import datetime
from database_setup import CoinsquareDogePricesVolumes
from database_setup import BittrexDogePricesVolumes
from database_setup import BidAkPriceVolumeComparison
from twilio.rest import Client
from pprint import pprint
import sys

sys.path.append('../')

from keys.twilio_sid_token import ACCOUNT_SID, AUTH_TOKEN, FROM_NUMBER, TO_NUMBER

def send_text_notification(session):
	while True:
		try:
			text_notification = TextNotification(session)
		except Exception as e:
			print(e)
		else:
			need_notification = text_notification.check_if_need_notification()
			print('________Printing if notification needs to be sent: ', need_notification)
			if need_notification:
				text_notification.send_notification()
			text_notification.update_database(need_notification)

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
		print(self.price_volume_dict)

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
						print('_________________Compare bids and asks method returned True')
						return True
		else:
			print('_________________Compare bids and asks method returned False')
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
			print('_________________Method returned True')
			return True
		else:
			print('_________________Method returned False')
			return False

	@staticmethod
	def send_notication(self):
		text_message = TextMessage()
		text_message.send_notification()

	@staticmethod
	def update_database(self):
		update_database = UpdateDatabase(need_notification)
		update_database.update_database()

class CoinsqureBittrexPricesVolumesCompared():
	def __init__(self, session):
		self.session = session

	def get_coinsquare_bittrex_prices_volumes_compared(self):
		try:
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
		except Exception as e:
			print(e)

		return prices_dict

	def convert_to_float(self, x):
		try:
			return float(x.replace(',',''))
		except Exception as e:
			return x

class TextMessage():
	def __init__(self):
		pass

	def send_notification(self):
		message = self.construct_message()
		self.send_message(message)

	def construct_message(self):
		if self.coinsquare_price_ask_1 < self.bittrex_price_bid_1:
			return "Buy on Coinsquare for {} and sell on Bittrex for {}".format(self.coinsquare_price_ask_1, self.bittrex_price_bid_1)
		elif self.coinsquare_price_bid_1 > self.bittrex_price_ask_1:
			return "Buy on Bittrex for {} and sell on Coinsquare for {}".format(self.bittrex_price_ask_1, self.coinsquare_price_bid_1)

	@staticmethod
	def send_message(message):
		print('________Send message method executing')
		try:
			account_sid = ACCOUNT_SID
			auth_token = AUTH_TOKEN
			from_number = FROM_NUMBER
			to_number = TO_NUMBER
			client = Client(account_sid, auth_token)

			text_message = client.messages.create(body=message, from_=from_number, to=to_number)
		except Exception as e:
			print(e)
		else:
			print('Message sent')
			return True

class UpdateDatabase():
	def __init__(self, session, need_notification):
		self.session = session
		self.need_notification = need_notification

	def update_database(self):
		print('________Update database method executing')
		try:
			self.update_price_volume_tables()
		except Exception as e:
			print(e)
		try:
			self.record_into_comparison_table()
		except Exception as e:
			print(e)
		print('________Update database method finished')

	def update_price_volume_tables(self):
		print('________Update price volume method executing')

		coinsquare_last_entry = self.session.query(CoinsquareDogePricesVolumes).order_by(CoinsquareDogePricesVolumes.id.desc()).first()
		bittrex_last_entry = self.session.query(BittrexDogePricesVolumes).order_by(BittrexDogePricesVolumes.id.desc()).first()

		if coinsquare_last_entry.compared == 'message_sent' and bittrex_last_entry.compared == 'message_sent':
			return None
		else:
			message_sent_update = 'message_not_sent'
			if self.need_notification:
				message_sent_update = 'message_sent'

			coinsquare_last_entry.compared = message_sent_update
			bittrex_last_entry.compared = message_sent_update

			self.session.commit()

	def record_into_comparison_table(self):
		print('________Record into comparison table method executing')
		compared = 'False'
		if self.need_notification:
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