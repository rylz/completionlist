from .. import db
from .. import utils

class ListItem:
    table_name = 'list_item'

    def __init__(self, template_item_id, uid):
        self.template_item_id = template_item_id
        self.uid = uid

    @property
    def label(self):
        # TODO request caching
        return db.query(
            'SELECT item_label FROM template_item WHERE template_item_id = %s',
            (self.template_item_id,))[0][0]

    @property
    def checked(self):
        # TODO request caching
        res = list(db.query(
            'SELECT checked FROM list_item WHERE template_item_id = %s AND uid = %s',
            (self.template_item_id, self.uid)))
        if res:
            return bool(res[0][0])
        else:
            # list_item is sparse
            return False

    @property
    def modified_time(self):
        # TODO request caching
        res = list(db.query(
            'SELECT modified_time FROM list_item WHERE template_item_id = %s AND uid = %s',
            (self.template_item_id, self.uid)))
        if res:
            return int(res[0][0])
        else:
            return None


def get_user_list_items(uid, template_id):
    return [ListItem(int(r[0]), uid) for r in db.query(
        'SELECT template_item_id FROM template_item WHERE template_id = %s',
        (template_id,))]


def update(uid, template_item_id, template_id, checked, details=None):
    """Create or update a list item for the given user."""
    return db.query('''
        REPLACE INTO list_item VALUES
        (template_item_id, uid, template_id, checked, modified_time, details) VALUES
        (%s, %s, %s, %s, %s, %s)
    ''', (template_item_id, uid, template_id, checked, utils.now(), details))
