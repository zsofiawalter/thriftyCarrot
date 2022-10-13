from bs4 import BeautifulSoup as bs
import requests 
import pandas as pd

# Get Wholefoods Website
page = requests.get('https://www.wholefoodsmarket.com/sales-flyer?store-id=10041').text 
soup = bs(page,'html.parser')

# Extract Category, Name, and price of products
category = [line.get_text() for line in soup.find_all('div',{"class":"w-sales-tile__brand"})]
name = [line.get_text() for line in soup.find_all('h4',{"class":"w-sales-tile__product"})]
price = [line.get_text() for line in soup.find_all('span',{"class":"w-sales-tile__regular-price--strikeout"})]

# Remove foods with no price
foods_without_price = {'Single-Serve Meals*','Cut Pineapple*','Supplements*'}
name_copy = name.copy()
for food in foods_without_price:
    category_index = name_copy.index(food)
    name.remove(food)
    del category[category_index]

#Make a dataframe 
df = pd.DataFrame()
df['category'] = category
df['name'] = name
df['price'] = price
#Remove rows with no category
df = df[df["category"]!=""]

#Save it as a csv file
df.to_csv("whole_foods_products.csv")
