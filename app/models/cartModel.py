from flask import current_app as app

# model
# __uid__, __pid__, quantity
class CartModel:
    def __init__(self, uid, pid, quantity):
        self.uid = uid
        self.pid = pid
        self.quantity = quantity

    @staticmethod
    def get(uid, pid):
        rows = app.db.execute('''
SELECT uid, pid, quantity
FROM Carts
WHERE uid = :uid
AND pid = :pid
''',
                              uid=uid,
                              pid=pid)
        return [CartModel(*row) for row in rows]

    @staticmethod
    def get_all_by_uid(uid):
        rows = app.db.execute('''
SELECT uid, pid, quantity
FROM Carts
WHERE uid = :uid
''',
                              uid=uid)
        return [CartModel(*row) for row in rows]