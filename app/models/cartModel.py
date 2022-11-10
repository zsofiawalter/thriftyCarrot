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
    
    @staticmethod
    def startCart(uid, cart_name, time_started):
        rows = app.db.execute('''
INSERT INTO Carts(uid, product_name, time_started)
VALUES(:uid, :cart_name, :time_started)
''', 
                                uid=uid,
                                cart_name=cart_name,
                                time_started=time_started)

# __uid__, product_name
# list of things user wants to buy
class CartListModel:
    def __init__(self, uid, product_name):
        self.uid = uid
        self.carproduct_namename = product_name
    
    @staticmethod
    def addToCartList(uid, product_name):
            rows = app.db.execute("""
INSERT INTO CartLists(uid, product_name)
VALUES(:uid, :product_name)
""",
                                uid=uid,
                                product_name=product_name)


# __uid__, __pid__, quantity
# exact product list user will buy
class CartContentsModel:
    def __init__(self, uid, pid, quantity):
        self.uid = uid
        self.pid = pid
        self.quantity = quantity