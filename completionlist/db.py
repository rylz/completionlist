import os
import psycopg2

POSTGRES_URL = os.environ.get('DATABASE_URL')
CONN = psycopg2.connect(POSTGRES_URL)

def query(sql, params=None):
    with CONN.cursor() as cur:
        cur.execute(sql, vars=params)
        if sql.strip().lower().startswith('select'):
            return cur.fetchall()
        CONN.commit()
