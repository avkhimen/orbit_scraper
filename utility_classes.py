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

	def record_into_database(self):
		prices = self.get_prices()
		volumes = self.get_volumes()
		timestamp = self.get_timestamp()

	def get_prices(self):
		pass

	def get_volumes(self):
		pass

	def get_timestamp(self):
		pass


class TextNotification():
	def __init__(self):
		pass

	def send_notification(self):
		if self.check_notification():
			pass

	def check_notification(self):
		pass