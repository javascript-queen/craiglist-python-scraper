from selenium import webdriver
import time
from text_unidecode import unidecode
from send_email import test_sendmail
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# parameters
ZIPCODE = 85255
RADIUS = 10
WAIT = 60 # time in minutes the code should wait before checking for updates
ITEMS = ['motor', 'desk', 'tree']
MAX_PRICE = 1000

url ='https://phoenix.craigslist.org/search/zip?search_distance=' + str(RADIUS) + '&postal=' + str(ZIPCODE) + '&max_price=' + str(MAX_PRICE)


# initiate a firefox browser instance
driver = webdriver.Firefox()
# load the url
driver.get(url)

# declare and empty list to keep the items. This will also come in handy to check items
# that are newly added

items = []

# get all the items on the first page. Not concerned about the other pages
results = driver.find_elements(By.CSS_SELECTOR, '.cl-search-results')
time.sleep(5)

# iterate through the results to find the text
for result in results:
    a = results[0].find_element(By.CSS_SELECTOR, '.title-blob')
    time.sleep(5)
    items.append(unidecode(a.find_element(By.TAG_NAME, 'a').text))
    time.sleep(5)
  
while True:
    driver.get(url)
    time.sleep(5)
    results = driver.find_elements(By.CSS_SELECTOR,'.cl-search-results')
    for result in results:
        a = results[0].find_element(By.CSS_SELECTOR,'.title-blob')
        text = unidecode(a.find_element(By.TAG_NAME, 'a').text)
        print(text)
        if (text not in items) and (any(ext.lower().strip() in text.lower().strip() for ext in ITEMS)):
            items.append(text)
            test_sendmail(text)
            
    time.sleep(WAIT*60)