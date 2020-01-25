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
			time.sleep(10)
			current_time = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
			print("Send notification sleep 10s " + current_time)
		finally:
			True

def sent_text_notification_dev():

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
	def __init__(self, session):
		self.session = session
		self.bittrex_price_ask_1 = bittrex_price_ask_1
		self.bittrex_volume_ask_1 = bittrex_volume_ask_1
		self.bittrex_price_bid_1 = bittrex_price_bid_1
		self.bittrex_volume_bid_1 = bittrex_volume_bid_1
		self.coinsquare_price_ask_1 = coinsquare_price_ask_1
		self.coinsquare_volume_ask_1 = coinsquare_volume_ask_1
		self.coinsquare_price_bid_1 = coinsquare_price_bid_1
		self.coinsquare_volume_bid_1 = coinsquare_volume_bid_1



class TextNotification():
	def __init__(self):
		pass

	def send_notification(self):
		if self.check_notification():
			pass

	def check_notification(self):
		pass
