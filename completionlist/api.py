from flask import g, Response, request

import json
import logging

from completionlist import app

logger = logging.getLogger(__name__)

from . import model

@app.route('/')
def index():
    """Get homepage data.

    Returns a list of list instances that the user has started, along with user info.
    """
    res = {
        'lists': [
            {
                "template_id": list_model.template_id,
                "name": list_model.name,
                "creation_time": list_model.creation_time,
            }
            for list_model in model.list.get_user_lists(g.logged_in_uid)
        ],
        "user": {
            "uid": g.logged_in_uid,
            "username": model.user.User(g.logged_in_uid).username,
        },
    }

    res['lists'].sort(key=lambda d: -d["creation_time"])
    return Response(json.dumps(res), mimetype='application/json')


@app.route('/list/<int:template_id>/<int:uid>')
def list_details(template_id, uid):
    """Get list data.

    Returns:
        'items': list of items with the current user's checked state
        'users': list of other users who have started this list
    """
    items = [
        {
            "template_item_id": list_item.template_item_id,
            "name": list_item.label,
            "checked": list_item.checked,
            "modified_time": list_item.modified_time,
        }
        for list_item in model.list_item.get_user_list_items(uid, template_id)
    ]
    items.sort(key=lambda d: d["template_item_id"])
    users = [
        {
            "uid": list_model.uid,
            "username": model.user.User(list_model.uid).username,
            "creation_time": list_model.creation_time,
        }
        for list_model in model.list.get_template_lists(template_id)
        if list_model.uid != uid
    ]
    users.sort(key=lambda d: -d["creation_time"])
    res = {
        "items": items,
        "users": users,
    }
    return Response(json.dumps(res), mimetype='application/json')
