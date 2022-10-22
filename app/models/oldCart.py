from flask import current_app as app

# model
# __cid__, uid, time_created, cart_name
class OldCart:
    def __init__(self, cid, uid, cart_name, time_created):
        self.cid = cid
        self.uid = uid
        self.cart_name = cart_name
        self.time_created = time_created

    @staticmethod
    def get(cid):
        rows = app.db.execute('''
SELECT cid, uid, cart_name, time_created
FROM OldCarts
WHERE cid = :cid
''',
                              cid=cid)
        return OldCart(*(rows[0])) if rows else None

    @staticmethod
    def get_all_by_uid_since(uid, since):
        rows = app.db.execute('''
SELECT cid, uid, cart_name, time_created
FROM OldCarts
WHERE uid = :uid
AND time_created >= :since
ORDER BY time_created DESC
''',
                              uid=uid,
                              since=since)
        return [OldCart(*row) for row in rows]
