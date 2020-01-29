import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base

def get_input_args():
    """Returns input arguments for main file execution"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--text_notification', '-t', type = str, default = 'False', 
                        help = 'Argument to enable text message notifications. "\
                        "Possible values are "True" and "False"')
    parser.add_argument('--currency', '-c', type = str, default = 'DOGE', 
                        help = 'Argument for currency which will be scraped')
    return parser.parse_args()

def get_startpage_url(currency):
	"""Returns url of currency traded against Bitcoin"""
	currency_url = "https://coinsquare.com/trade?pair=" + currency + "-BTC"

	return currency_url

def create_session():
	"""Returns a session for database operations"""
	try:
		engine = create_engine('sqlite:///doge_prices_volumes.db')
		Base.metadata.bind = engine
		DBsession = sessionmaker(bind=engine)
		session = DBsession()
	except Exception as e:
		print(e)

	return session