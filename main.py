from support_functions import get_input_args

def main():
	"""Main function to execute all code"""

	# Get input arguments for main.py
	# Arguments are text notification on/off flag and currency
	text_notification_on_or_off = get_input_args().text_notification
	currency = get_input_args().currency
	
	# Scraping and database recording will run synchronously
	# Text message notification will run asynchronously





if __name__ == '__main__':
	main()