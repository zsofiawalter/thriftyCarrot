from flask import current_app as app

# model
# __cid__, __pid__, product_name, price, category, store
class OldCartContentModel:
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
                              cid=cid)
        return OldCartContentModel(*(rows[0])) if rows else None
    @staticmethod
    def get_count_by_category(uid):
        rows = app.db.execute('''
SELECT COUNT(OldCarts.cid), COUNT(OldCartContents.pid), COUNT(OldCartContents.product_name), COUNT(OldCartContents.price), OldCartContents.category, COUNT(OldCartContents.store)
FROM OldCartContents, OldCarts
WHERE OldCarts.uid = :uid
AND OldCarts.cid = OldCartContents.cid
GROUP BY category
''',
                              uid=uid)
        return [OldCartContentModel(*row) for row in rows]

    @staticmethod
    def get_most_recent_by_uid(uid):
        rows = app.db.execute('''
SELECT OldCarts.cid, OldCartContents.pid, OldCartContents.product_name, OldCartContents.price, OldCartContents.category, OldCartContents.store
FROM OldCartContents, OldCarts
WHERE OldCarts.uid = :uid
AND OldCarts.cid = OldCartContents.cid
ORDER BY time_created DESC
''',
                              uid=uid)
        return [OldCartContentModel(*row) for row in rows]

    @staticmethod
    def get_all_by_uid_since(uid, since):
        rows = app.db.execute('''
SELECT OldCarts.cid, OldCartContents.pid, OldCartContents.product_name, OldCartContents.price, OldCartContents.category, OldCartContents.store
FROM OldCartContents, OldCarts
WHERE OldCarts.uid = :uid
AND OldCarts.time_created >= :since
AND OldCarts.cid = OldCartContents.cid
ORDER BY time_created DESC
''',
                              uid=uid,
                              since=since)
        return [OldCartContentModel(*row) for row in rows]

    @staticmethod
    def get_all_oldcartcontent_by_uid(uid):
        rows = app.db.execute('''
WITH AllOldCarts AS
(SELECT cid
FROM OldCarts
WHERE uid = :uid
ORDER BY time_created DESC)
SELECT OldCartContents.cid, OldCartContents.pid, OldCartContents.product_name, OldCartContents.price, OldCartContents.category, OldCartContents.store
FROM OldCartContents, AllOldCarts
WHERE AllOldCarts.cid = OldCartContents.cid
''',
                              uid=uid)        
        return [OldCartContentModel(*row) for row in rows]

    @staticmethod
    def get_content_of_recent_three_by_uid(uid):
        rows = app.db.execute('''
WITH RecentThree AS
(SELECT cid
FROM OldCarts
WHERE uid = :uid
ORDER BY time_created DESC
limit 3)
SELECT OldCartContents.cid, OldCartContents.pid, OldCartContents.product_name, OldCartContents.price, OldCartContents.category, OldCartContents.store
FROM OldCartContents, RecentThree
WHERE RecentThree.cid = OldCartContents.cid
''',
                              uid=uid)        
        return [OldCartContentModel(*row) for row in rows]

    @staticmethod
    def insert(cid, pid, product_name, price, category, store):
        try:
            app.db.execute("""
INSERT INTO OldCartContents(cid, pid, product_name, price, category, store)
VALUES(:cid, :pid, :product_name, :price, :category, :store)
""",
                                cid=cid,
                                pid=pid, 
                                product_name=product_name, 
                                price=price, 
                                category=category, 
                                store=store)
        except Exception as e:
            print(str(e))
            return None
