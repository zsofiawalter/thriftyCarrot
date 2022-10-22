from flask import current_app as app

# __cid__, __pid__, product_name, price, category, store
class OldCartContent:
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
        return OldCartContent(*(rows[0])) if rows else None

    @staticmethod
    def get_all_by_uid_since(uid, since):
        rows = app.db.execute('''
SELECT cid, pid, product_name, price, category, store
FROM OldCartContents, OldCarts
WHERE OldCarts.uid = :uid
AND OldCarts.time_created >= :since
AND OldCarts.cid = OldCartContents.cid
ORDER BY time_created DESC
''',
                              uid=uid,
                              since=since)
        return [OldCartContent(*row) for row in rows]
