import time
from datetime import datetime

def send_text_notification():
	while True:
		try:
			text_notification = TextNotification()
		except Exception as e:
			print(e)
		else:

			time.sleep(5)
			now = datetime.now()
			current_time = now.strftime("%H:%M:%S")
			print("Send notification sleep 5s " + current_time)
		finally:
			True

def get_prices_and_record_into_database(start_url):
	while True:
		try:
			currency_prices_and_volumes = CurrencyPricesVolumes()
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
	def __init__(self):
		pass

	def record_into_database(self):
		pass

class TextNotification():
	def __init__(self):
		pass

	def send_notification(self):
		if self.check_notification():
			pass

	def check_notification(self):
		pass