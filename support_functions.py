import argparse

def get_input_args():
    """Returns input arguments for main file execution"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--text_notification', '-t', type = str, default = 'False', 
                        help = 'Argument to enable text message notifications. Possible values are "True" and "False"')
    parser.add_argument('--currency', '-c', type = str, default = 'DOGE', 
                        help = 'Argument for currency which will be scraped')
    return parser.parse_args()

def get_startpage_url(currency):
	"""Returns url of currency traded against Bitcoin"""
	currency_url = "https://coinsquare.com/trade?pair=" + currency + "-BTC"

def create_session():
	"""Returns a session for database operations"""
	engine = create_engine('sqlite:///coin_database_test.db')
	Base.metadata.bind = engine
	DBsession = sessionmaker(bind=engine)
	session = DBsession()

	return session 