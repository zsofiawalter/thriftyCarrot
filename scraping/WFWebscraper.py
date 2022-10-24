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
time.sleep(2)
#show more categories
chromeDriver.find_element(By.XPATH, '//button[@data-csa-c-content-id="showMore"]').click() 
time.sleep(2)

# get categories
categories = [i.text for i in chromeDriver.find_elements(By.XPATH, '//button[@class="w-link w-link--light-nav w-link--arrow"]')][1:18]

# get sub categories function
def get_sub_categories():
    sub_categories = []
    output = [i.text for i in chromeDriver.find_elements(By.XPATH, '//button[@class="w-link w-link--light-nav w-link--arrow"]')][2:]
    for out in output:
        if out!="":
            sub_categories.append(out)
    return sub_categories

grocery_table = pd.DataFrame()
for category in categories:
    print(category)
    try:
        # click category
        chromeDriver.find_element(By.XPATH, '//button[@data-csa-c-content-id="{}"]'.format(category)).click() 
    except:
        # show all categories
        chromeDriver.find_element(By.XPATH, '//button[@data-csa-c-content-id="showMore"]').click() 
        time.sleep(3)
        #click  category
        chromeDriver.find_element(By.XPATH, '//button[@data-csa-c-content-id="{}"]'.format(category)).click() 
    time.sleep(3)
    sub_categories = get_sub_categories()
    for sub_category in sub_categories:
        if sub_category == "Coffee":
            continue
        print(sub_category)
        # click on subcategory 
        chromeDriver.find_element(By.XPATH, '//button[@data-csa-c-content-id="{}"]'.format(sub_category)).click() 
        time.sleep(3)
        # extract name, and price
        name = [element.text for element in chromeDriver.find_elements(By.XPATH, "//h2[@data-testid='product-tile-name']")]
        price = [element.find_element(By.CLASS_NAME,"regular_price").text for element in chromeDriver.find_elements(By.XPATH, "//div[@data-testid='pricing-block']")]
        sub_category1 = [sub_category for i in range(len(name))]
        category1 = [category for i in range(len(name))]
        temp_table = pd.DataFrame({"name":name,"price":price,"sub-category": sub_category1, "category":category1})
        grocery_table = pd.concat([grocery_table,temp_table],ignore_index=True)
        chromeDriver.find_element(By.XPATH, '//button[@data-csa-c-content-id="{}"]'.format(category)).click() 
        time.sleep(2)
    chromeDriver.find_element(By.XPATH, '//button[@data-csa-c-content-id="All Products"]').click() 
    time.sleep(2)
#Save it as a csv file
grocery_table = grocery_table.to_csv("WFproducts.csv")
