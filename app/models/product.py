from flask import current_app as app


class Product:
    def __init__(self, id, name, brand, category, price, lastUpdate):
        self.id = id
        self.name = name
        self.brand = brand
        self.category = category
        self.price = price
        self.store = category
        self.lastUpdate = lastUpdate

    @staticmethod
    def get(id):
        rows = app.db.execute('''
SELECT id, name, brand, category, price, lastUpdate
FROM Products
WHERE id = :id
''',
                              id=id)
        return Product(*(rows[0])) if rows is not None else None

    @staticmethod
    def get_all(available=True):
        rows = app.db.execute('''
SELECT id, name, brand, category, price, lastUpdate
FROM Products
WHERE available = :available
''', #TODO: set here to filter based on last update 
        available=available)
        return [Product(*row) for row in rows]
