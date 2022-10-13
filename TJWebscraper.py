import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Takes apart table to be used
def decomposeTable(table):
    return table[0], table[1], table[2], table[3], table[4], table[5]

# Puts lists together into table for passing variables
def composeTable(stores, categories, subcats, brands, names, prices):
    return [stores, categories, subcats, brands, names, prices]

# Returns the list of categories on TJ page
def findTJCategories(driver):
    return driver.find_elements(By.CLASS_NAME, 'CategoryFilter_categoryFilter__subCategoryButton__4rOWH')

# Input: driver, string category being analyzed, array of arrays of data being accumulated
# Output: returns table with additional data entered
def findTJProducts(driver, category, table):
    stores, categories, subcats, brands, names, prices = decomposeTable(table)
    store = "Trader Joes"

    # Find all product cards on page
    pages = driver.find_elements(By.CLASS_NAME, "PaginationItem_paginationItem__2f87h")

    finished = False

    # Clicks through the pages for this category 
    while(not finished):
        # List of product cards on page
        navProduct_cards = driver.find_elements(By.CLASS_NAME, 'ProductCard_card__info__2M2Ao')
        
        # Retrieves information from each card
        for card in navProduct_cards: 
            # Find elements
            subcategory = card.find_element(By.CLASS_NAME, 'ProductCard_card__category__Hh3rT')
            name = card.find_element(By.CLASS_NAME, 'ProductCard_card__title__large__3bAY6')
            price = card.find_element(By.CLASS_NAME, 'ProductPrice_productPrice__price__3-50j')

            # Add strings to lists
            stores.append("Trader Joes")
            categories.append(category)
            subcats.append(subcategory.text)
            names.append(name.text)
            prices.append(price.text)
        try:
            arrow = driver.find_element(By.CLASS_NAME, "Pagination_pagination__arrow_side_right__9YUGr")
            arrow.click()
            time.sleep(4)
        except:
            break

    return composeTable(stores, categories, subcats, brands, names, prices)


def traderJoes(driver, table):
    # Load website
    driver.get(r"https://www.traderjoes.com/home/products/category/food-8")
    time.sleep(3)   # Wait for loading

    # decompose table
    stores, categories, subcats, brands, names, prices = decomposeTable(table)

    # Accept cookies
    driver.find_element("xpath", "/html/body/div/div[1]/div[1]/div[1]/div/button").click()

    # Find list of all web elements listing categories
    navCategories = findTJCategories(driver)

    # Initialize string list of categories
    textCategories = []
    for c in navCategories:
        textCategories.append(c.text)

    # Read all products for each category
    for category in textCategories:
        if category == "Food":      
            continue
        elif category == "Flowers & Plants":
            break

        # Reload list of category elements on page
        navCategories = findTJCategories(driver)
        for c in navCategories:
            if c.text == category:      # web element = element we want
                time.sleep(4)
                c.click()               # open page
                break
        
        time.sleep(4)                   # Wait for category page to load

        # Scrape information
        table = findTJProducts(driver, category, composeTable(stores, categories, subcats, brands, names, prices))
        stores, categories, subcats, brands, names, prices = decomposeTable(table)

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

chromeDriver.quit()

df = pd.DataFrame({'Category':categories, 'Name':names, 'Price':prices}) 
df = pd.DataFrame({'Store':stores, 'Category':categories, 'Subcategory':subcats, 'Brand':brands, 'Name':names, 'Price':prices}) 
df.to_csv('TJProducts.csv', index=False, encoding='utf-8')