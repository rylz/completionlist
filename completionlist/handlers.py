from flask import g

from completionlist import app

@app.before_request
def initialize_user():
    # TODO: implement real login and auth
    g.logged_in_uid = 1
