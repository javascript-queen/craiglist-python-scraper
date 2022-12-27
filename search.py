# selenium
# text_unidecode 
# geckodriver + MAYBE Xcode
# Firefox

from selenium import webdriver
import time
from text_unidecode import unidecode
from send_email import test_sendmail
from selenium.webdriver.common.by import By
from datetime import datetime

# parameters
ZIPCODE = 85255
RADIUS = 50
WAIT = 1 # time in minutes the code should wait before checking for updates
ITEMS = ['mattress', 'bed', 'spring box']

url ='https://phoenix.craigslist.org/search/zip?search_distance=' + str(RADIUS) + '&postal=' + str(ZIPCODE) 


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
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(text, "Time =", current_time)
        if (text not in items) and (any(ext.lower().strip() in text.lower().strip() for ext in ITEMS)):
            items.append(text)
            test_sendmail(text)
            
    time.sleep(WAIT*60)