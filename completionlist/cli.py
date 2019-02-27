from completionlist import app
from . import db


@app.cli.command()
def reload_schema():
    with open('schema.sql') as f:
        schema = f.read()
    db.query(schema)
    with open('static.sql') as f:
        static = f.read()
    db.query(static)
