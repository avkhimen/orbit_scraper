import argparse
import bittrex.bittrex as bittrex
import os
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

def create_session():
	"""Returns a session for database operations"""
	engine = create_engine('sqlite:///doge_prices_volumes.db')
	Base.metadata.bind = engine
	DBsession = sessionmaker(bind=engine)
	session = DBsession()

	return session

def load_key(path):
	"""Returns the key and secret from file"""
	with open(path, 'r') as f:
		key = f.readline().strip()
		secret = f.readline().strip()
		
	return key, secret

def initialize_accounts():
	"""Initializes the bittrex object from API docs"""
	FILE_PATH = os.path.dirname(os.path.abspath(__file__))
	api_key, api_secret = load_key(FILE_PATH + r"\bittrex\key.txt")
	bittrex_account = bittrex.Bittrex(api_key = api_key, api_secret = api_secret)

	return bittrex_account