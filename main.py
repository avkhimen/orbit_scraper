from support_functions import get_input_args, get_startpage_url
from notification_message_utility_classes import send_text_notification
from data_collection_utility_classes import get_prices_and_record_into_database
from concurrent.futures import ThreadPoolExecutor
from ast import literal_eval
from support_functions import create_session

def main():
	"""Main function to execute all code"""

	# Get input arguments for main.py
	# Arguments are text notification on/off flag and currency
	text_notification_on_or_off = get_input_args().text_notification
	currency = get_input_args().currency

	# Get url of the starting page
	start_url = get_startpage_url(currency)

	# Create session for data collection
	data_collection_session = create_session()

	# Create session for data collection
	text_notification_session = create_session()
	
	# Scraping and database recording will run synchronously
	# Text message notification will run asynchronously
	with ThreadPoolExecutor(max_workers=2) as executor:
		future = executor.submit(get_prices_and_record_into_database, start_url, data_collection_session)
		if literal_eval(text_notification_on_or_off) == True:
			future = executor.submit(send_text_notification, text_notification_session)

if __name__ == '__main__':
	main()