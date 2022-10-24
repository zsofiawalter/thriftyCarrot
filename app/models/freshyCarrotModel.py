from flask import current_app as app

# __uid__, __pid__, like_dislike
class FreshyCarrotModel:
    """
    This is just a TEMPLATE for Review, you should change this by adding or 
        replacing new columns, etc. for your design.
    """
    def __init__(self, uid, pid, name, like_dislike, time_created):
        self.uid = uid
        self.pid = pid
        self.name = name
        self.like_dislike = like_dislike
        self.time_created = time_created
    """
    This method retrieves all reviews, whether fresh or rotten carrots, for user
    with the given uid.
    """
    @staticmethod
    def get_all_reviews(uid):
        rows = app.db.execute('''
SELECT uid, pid, like_dislike, time_created
FROM Preferences
WHERE uid = :uid
''',
                              uid=uid)
        return [FreshyCarrotModel(*row) for row in rows]
    
    """
    This method retrieves the 5 most recent FRESH carrots (likes) for the user with the given uid.
    It returns the uid, pid, product name, like or dislike boolean, and the time of creation for each
    freshy carrot review.
    """
    @staticmethod
    def get_5_recent_fresh_by_uid(uid):
        rows = app.db.execute('''
SELECT Preferences.uid, Preferences.pid, Products.name, Preferences.like_dislike, Preferences.time_created
FROM Preferences, Products
WHERE Preferences.uid = :uid AND Preferences.like_dislike = True AND Preferences.pid = Products.id
ORDER BY Preferences.time_created DESC
limit 5
''',
                              uid=uid)
        return [FreshyCarrotModel(*row) for row in rows]
    """
    This method retrieves the 5 most recent ROTTEN carrots (dislikes) for the user with the given uid.
    It returns the uid, pid, product name, like or dislike boolean, and the time of creation for each
    freshy carrot review.
    """
    @staticmethod
    def get_5_recent_rotten_by_uid(uid):
        rows = app.db.execute('''
SELECT Preferences.uid, Preferences.pid, Products.name, Preferences.like_dislike, Preferences.time_created
FROM Preferences, Products
WHERE Preferences.uid = :uid AND Preferences.like_dislike = False AND Preferences.pid = Products.id
ORDER BY Preferences.time_created DESC
limit 5
''',
                              uid=uid)
        return [FreshyCarrotModel(*row) for row in rows]

