from flask import current_app as app


# __uid__, __pid__, quantity
class CartModel:
    def __init__(self, uid, pid, quantity):
        self.uid = uid
        self.pid = pid
        self.quantity = quantity

    @staticmethod
    def get(uid):
        rows = app.db.execute('''
SELECT uid, pid, quantity
FROM Carts
WHERE uid = :uid
''',
                              uid=uid)
        return [CartModel(*row) for row in rows]

# users cart names
class CartFormModel:
    def __init__(self, uid, cartName):
        self.uid = uid
        self.cartname = cartName

# users products in cart
class ProductsinCartForm:
    def __init__(self, uid, pid, quantity):
        self.uid = uid
        self.pid = pid
        self.quantity = quantity

    @staticmethod
    def addProductToCart(uid, product, quantity):
        try:
            rows = app.db.execute("""
INSERT INTO Users(email, password, firstname, lastname)
VALUES(:email, :password, :firstname, :lastname)
RETURNING id
""",
                                  email=email,
                                  password=generate_password_hash(password),
                                  firstname=firstname, lastname=lastname)
            id = rows[0][0]
            return CartForm.get(id)
        except Exception as e:
            # likely email already in use; better error checking and reporting needed;
            # the following simply prints the error to the console:
            print(str(e))
            return None


