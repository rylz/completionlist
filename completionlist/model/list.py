from .. import db

class List:
    table_name = 'list'

    def __init__(self, template_id, uid):
        self.template_id = template_id
        self.uid = uid

    @property
    def name(self):
        # TODO request caching
        return db.query(
            'SELECT template_name FROM template WHERE template_id = %s',
            (self.template_id,))[0][0]

    @property
    def creation_time(self):
        # TODO request caching
        return int(db.query(
            'SELECT creation_time FROM list WHERE template_id = %s AND uid = %s',
            (self.template_id, self.uid))[0][0])


def get_user_lists(uid):
    return [List(int(r[0]), uid) for r in db.query(
        'SELECT template_id FROM list WHERE uid = %s', (uid,))]


def get_template_lists(template_id):
    return [List(template_id, int(r[0])) for r in db.query(
        'SELECT uid FROM list WHERE template_id = %s', (template_id,))]
