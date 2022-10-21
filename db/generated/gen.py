from werkzeug.security import generate_password_hash
import csv
from faker import Faker
import random

num_users = 100
num_products = 2000
num_purchases = 2500

Faker.seed(0)
fake = Faker()


def get_csv_writer(f):
    return csv.writer(f, dialect='unix')

# id, email, password, firstname, lastname, birthdate
def gen_users(num_users):
    with open('Users.csv', 'w') as f:
        writer = get_csv_writer(f)
        print('Users...', end=' ', flush=True)
        for uid in range(num_users):
            if uid % 10 == 0:
                print(f'{uid}', end=' ', flush=True)
            profile = fake.profile()
            email = profile['mail']
            plain_password = f'pass{uid}'
            password = generate_password_hash(plain_password)
            name_components = profile['name'].split(' ')
            firstname = name_components[0]
            lastname = name_components[-1]
            birthdate = profile['birthdate']
            writer.writerow([uid, email, password, firstname, lastname, birthdate])
        print(f'{num_users} generated')
    return

stores = ["Trader Joes", "Whole Foods", "Harris Teeters"]
categories = ["Baked Goods", "Bread", "Produce", "Cheese", "Dairy & Eggs", "Sauces", "Prepared Food", "Frozen Food", "Produce", "Meat", "Seafood", "Baking", "Pantry", "Canned Goods", "Beverages"]
# id, name, price, category, store, last_update
def gen_products(num_products):
    available_pids = []
    with open('Products.csv', 'w') as f:
        writer = get_csv_writer(f)
        print('Products...', end=' ', flush=True)
        for pid in range(num_products):
            if pid % 100 == 0:
                print(f'{pid}', end=' ', flush=True)
            name = fake.sentence(nb_words=4)[:-1]
            price = f'{str(fake.random_int(max=500))}.{fake.random_int(max=99):02}'
            last_update = fake.date_time_between('-2w')
            category = random.choice(categories)
            store = random.choice(stores)
            available_pids.append(pid)
            writer.writerow([pid, name, price, category, store, last_update])
        print(f'{num_products} generated;')
    return available_pids

# uid, pid, like_dislike
def gen_preferences(num_preferences):
    with open('Preferences.csv', 'w') as f:
        writer = get_csv_writer(f)
        print('Preferences...', end=' ', flush=True)
        for i in range(random.randint(0, num_users*num_products)):
            
            like_dislike = random.boolean
            writer.writerow([i, like_dislike])
    return

# uid, pid, quantity
def gen_carts(num_itemsInCart):
    return

# uid, pid, like_dislike
def gen_oldCarts(num_carts, available_pids):
    with open('OldCarts.csv', 'w') as f:
        writer = get_csv_writer(f)
        print('OldCarts...', end=' ', flush=True)
        for cid in range(num_purchases):
            if cid % 100 == 0:
                print(f'{cid}', end=' ', flush=True)
            uid = fake.random_int(min=0, max=num_users-1)
            pid = fake.random_element(elements=available_pids)
            cart_name = fake.sentence(nb_words=2)[:-1]
            time_purchased = fake.date_time()
            writer.writerow([cid, uid, pid, cart_name, time_purchased])
        print(f'{num_purchases} generated')
    return

# cid, pid, product_name, price, category, store
def gen_oldCartContent(num_purchases):
    return

gen_users(num_users)
available_pids = gen_products(num_products)
gen_oldCarts(num_purchases, available_pids)

