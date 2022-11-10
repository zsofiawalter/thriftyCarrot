from flask import current_app as app


# __uid__, cart_name, time_started
# name of current cart user is working on
class CartModel:
    def __init__(self, uid, cart_name, time_started):
        self.uid = uid
        self.cart_name = cart_name
        self.time_started = time_started

    @staticmethod
    def get(uid):
        rows = app.db.execute('''
SELECT uid, cart_name, time_started
FROM Carts
WHERE uid = :uid
''',
                              uid=uid)
        return [CartModel(*row) for row in rows]

# __uid__, product_name
# list of things user wants to buy
class CartListModel:
    def __init__(self, uid, product_name):
        self.uid = uid
        self.carproduct_namename = product_name

# __uid__, __pid__, quantity
# exact product list user will buy
class CartContentsModel:
    def __init__(self, uid, pid, quantity):
        self.uid = uid
        self.pid = pid
        self.quantity = quantity