
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pprint import pprint

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

price_volume_dict = {}

try:
    driver.get("https://coinsquare.com/trade?pair=DOGE-BTC")
    time.sleep(10)
except Exception as e:
    print("Couldn't load site")

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
    finally:
        i += 1
        time.sleep(0.0)

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
    finally:
        i += 1
        time.sleep(0.0)

pprint(price_volume_dict)

driver.close()