from flask import current_app as app

# __cid__, __pid__, product_name, price, category, store
class oldCartContent:
    def __init__(self, cid, pid, product_name, price, category, store):
        self.cid = cid
        self.pid = pid
        self.product_name = product_name
        self.price = price
        self.category = category
        self.store = store

    @staticmethod
    def get(cid):
        rows = app.db.execute('''
SELECT cid, pid, product_name, price, category, store
FROM OldCartContents
WHERE cid = :cid
''',
                              id=id)
        return oldCartContent(*(rows[0])) if rows else None

#     @staticmethod
#     def get_all_by_uid_since(uid, since):
#         rows = app.db.execute('''
# SELECT cid, pid, product_name, price, category, store
# FROM Purchases
# WHERE uid = :uid
# AND time_purchased >= :since
# ORDER BY time_purchased DESC
# ''',
#                               uid=uid,
#                               since=since)
#         return [oldCartContent(*row) for row in rows]
