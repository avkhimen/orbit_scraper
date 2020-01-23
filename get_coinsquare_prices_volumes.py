
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pprint import pprint

def main():
    """Main program controller"""
    order_book = get_coinsquare_prices_volumes('https://coinsquare.com/trade?pair=DOGE-BTC')
    pprint(order_book)

def get_coinsquare_prices_volumes(start_url):
    """Returns the dict of latest DOGE price-volume pairs from Coinsquare exchange"""

    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)

    price_volume_dict = {}

    try:
        driver.get(start_url)
        time.sleep(10)
    except Exception as e:
        print('Failed to load site 1st time')
        try:
            print('Attemping to load site again')
            driver.get(start_url)
            time.sleep(10)
        except Exception as e:
            print("Couldn't load site")
            return False

    #Get ask price and volume
    i = 1

    while i < 16:
        try:
            xpath_path = "/html/body/div[1]/div/div[2]/div[3]/div[2]/div"\
            "[2]/div/div/div[2]/div/div[3]/div[1]/div[" + str(i) + "]/div[1]/div[2]"
            ask_price = driver.find_element_by_xpath(xpath_path).get_attribute('innerHTML')
            
            xpath_path = "/html/body/div[1]/div/div[2]/div[3]/div[2]/div["\
            "2]/div/div/div[2]/div/div[3]/div[1]/div[" + str(i) + "]/div[1]/div[1]"
            ask_volume = driver.find_element_by_xpath(xpath_path).get_attribute('innerHTML')

            price_volume_dict['ask_' + str(16-i)] = {'volume': ask_volume, 'price': ask_price}

        except Exception as e:
            print(e)
            price_volume_dict['ask_' + str(16-i)] = {'volume': 'scrape_error', 'price': 'scrape_error'}
        finally:
            i += 1
            time.sleep(0.0)

    #Get bid price and volume
    i = 1

    while i < 16:
        try:
            xpath_path = "/html/body/div[1]/div/div[2]/div[3]/div[2]/div[2"\
            "]/div/div/div[2]/div/div[3]/div[3]/div[" + str(i) + "]/div[1]/div[2]"
            bid_price = driver.find_element_by_xpath(xpath_path).get_attribute('innerHTML')
            
            xpath_path = "/html/body/div[1]/div/div[2]/div[3]/div[2]/div[2]/"\
            "div/div/div[2]/div/div[3]/div[3]/div[" + str(i) + "]/div[1]/div[1]"
            bid_volume = driver.find_element_by_xpath(xpath_path).get_attribute('innerHTML')

            price_volume_dict['bid_' + str(i)] = {'volume': bid_volume, 'price': bid_price}

        except Exception as e:
            print(e)
            price_volume_dict['bid_' + str(i)] = {'volume': 'scrape_error', 'price': 'scrape_error'}
        finally:
            i += 1
            time.sleep(0.0)

    driver.close()

    return price_volume_dict

class Error(Exception):
    """Returns basic exception class"""
    pass

class NoSuchElementException(Error):
    """Returned when xpath element couldn't be located"""
    pass

if __name__ == '__main__':
    main()