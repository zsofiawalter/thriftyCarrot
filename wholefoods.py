import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Get Wholefoods Website
chromeDriver = webdriver.Chrome("C://Users/meske/Documents/chromedriver_2.exe")
time.sleep(3)
chromeDriver.get('https://www.wholefoodsmarket.com/products/all-products')
time.sleep(4)

# Enter zip code 
chromeDriver.find_element("xpath","//input[@id='pie-store-finder-modal-search-field']").send_keys(27708)
time.sleep(3)
chromeDriver.find_element("xpath","//li[@class='wfm-search-bar--list_item']").click()

#Load more
time.sleep(3)
chromeDriver.find_element("xpath","//button[@class='w-button w-button--secondary w-button--load-more']").click()
time.sleep(3)


# Extract Category, Name, and price of products
category = [element.text for element in chromeDriver.find_elements(By.XPATH, "//span[@data-testid='product-tile-brand']")]
name = [element.text for element in chromeDriver.find_elements(By.XPATH, "//h2[@data-testid='product-tile-name']")]
price = [element.find_element(By.CLASS_NAME,"regular_price").text for element in chromeDriver.find_elements(By.XPATH, "//div[@data-testid='pricing-block']")]

#Make a dataframe 
df = pd.DataFrame()
df['category'] = category
df['name'] = name
df['price'] = price

#Save it as a csv file
df.to_csv("whole_foods_products(1).csv")
