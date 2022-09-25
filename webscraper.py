import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

def decomposeTable(table):
    return table[0], table[1], table[2], table[3], table[4], table[5]

def composeTable(stores, categories, subcats, brands, names, prices):
    return [stores, categories, subcats, brands, names, prices]


def traderJoes(driver, table):
    # Load website
    driver.get(r"https://www.traderjoes.com/home/products/category/food-8")
    time.sleep(3)   # Wait for loading

    # decompose table
    stores, categories, subcats, brands, names, prices = decomposeTable(table)

    # Accept cookies
    driver.find_element("xpath", "/html/body/div/div[1]/div[1]/div[1]/div/button").click()

    # Create list of all categories
    navCategories = driver.find_elements(By.CLASS_NAME, 'CategoryFilter_categoryFilter__subCategoryButton__4rOWH')

    # Read all products for each category
    for category in navCategories:
        if category.text == "Food":
            continue
        elif category.text == "Beverages":
            continue

        category.click()    # Open category page
        time.sleep(3)       # Wait for category page to load
        
        # Find all product cards on page
        navProduct_cards = driver.find_elements(By.CLASS_NAME, 'ProductCard_card__info__2M2Ao')

        for card in navProduct_cards: 
            # Find elements
            store = "Trader Joes"
            subcategory = card.find_element(By.CLASS_NAME, 'ProductCard_card__category__Hh3rT')
            name = card.find_element(By.CLASS_NAME, 'ProductCard_card__title__large__3bAY6')
            price = card.find_element(By.CLASS_NAME, 'ProductPrice_productPrice__price__3-50j')

            stores.append("Trader Joes")
            categories.append(category)
            subcats.append(subcategory.text)
            names.append(name.text)
            prices.append(price.text)
    
    return composeTable(stores, categories, subcats, brands, names, prices)



# Initialize columns for table
stores = []     # store where product is offered
categories = [] # category of the product
subcats = []    # subcategory of the product
brands = []     # brand of the product
names = []      # name of the product
prices = []     # price of the product
table = [stores, categories, subcats, brands, names, prices] # initial table

# Initialize Chrome driver
chromeDriver = webdriver.Chrome("/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/selenium/webdriver/chrome/chromedriver")

# Trader Joes
table = traderJoes(chromeDriver, table)
# for i in range(max(names.length, categories.length, prices.length, subcats.length)):
    # TODO: how to we deal with null values ex, TJ has no brands

chromeDriver.quit()

df = pd.DataFrame({'Category':categories, 'Name':names, 'Price':prices}) 
df.to_csv('products.csv', index=False, encoding='utf-8')