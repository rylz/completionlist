from .. import db

class User:
    table_name = 'users'

    def __init__(self, uid):
        self.uid = uid

    @property
    def username(self):
        # TODO request caching
        return db.query(
            'SELECT username FROM users WHERE user_id = %s',
            (self.uid,))[0][0]
