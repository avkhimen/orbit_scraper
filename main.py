from support_functions import get_input_args, get_startpage_url
from utility_classes import send_text_notification
from utility_classes import get_prices_and_record_into_database
from threading import Thread
from ast import literal_eval

def main():
	"""Main function to execute all code"""

	# Get input arguments for main.py
	# Arguments are text notification on/off flag and currency
	text_notification_on_or_off = get_input_args().text_notification
	currency = get_input_args().currency

	# Get url of the starting page
	start_url = get_startpage_url(currency)
	
	# Scraping and database recording will run synchronously
	# Text message notification will run asynchronously
	t1 = Thread(target = get_prices_and_record_into_database(start_url))
	t1.start()
	if literal_eval(text_notification_on_or_off):
		t2 = Thread(target = send_text_notification())
		t2.start()




if __name__ == '__main__':
	main()