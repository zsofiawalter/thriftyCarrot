import datetime
from flask import current_app as app

# __id__, name, price, category, store, last_update
class Product:
    def __init__(self, id, name, price, category, store, last_update):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        self.store = store
        self.last_update = last_update

    @staticmethod
    def get(id):
        rows = app.db.execute('''
SELECT id, name, price, category, store, last_update
FROM Products
WHERE id = :id
''',
                                id=id)
        return Product(*(rows[0])) if rows is not None else None

    @staticmethod
    def get_all(since=datetime.datetime(2022, 10, 1, 0, 0, 0)):
        rows = app.db.execute('''
SELECT id, name, price, category, store, last_update
FROM Products
WHERE last_update >= :since
''',
                                since=since)
        return [Product(*row) for row in rows]
