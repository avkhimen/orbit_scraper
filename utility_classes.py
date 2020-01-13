def send_text_notification():
	pass

def get_prices_and_record_into_database(start_url):
	while True:
		try:
			currency_prices_and_volumes = CurrencyPricesVolumes()
		except Exception:
			pass
		finally:
			return True

class CurrencyPricesVolumes():
	def __init__(self):
		pass