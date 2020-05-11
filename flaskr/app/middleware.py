import os

from flask import g
from redis import Redis
import psycopg2


def init_db():
    if 'db' not in g:
        g.db = Redis(host=os.getenv('REDIS_SERVER_HOST'),
                     port=int(os.getenv('REDIS_SERVER_PORT')),
                     decode_responses=True)


def init_pg():
    db_cred = {
        'user': os.environ.get('PGUSER'),
        'password': os.environ.get('PGPASSWORD'),
        'database': os.environ.get('PGDATABASE'),
        'host': os.environ.get('PGHOST'),
        'port': os.environ.get('PGPORT')
    }
    print('Creating table')
    conn = psycopg2.connect(**db_cred)
    cur = conn.cursor()
    create_sql = '''CREATE TABLE IF NOT EXISTS  values(
                    row_id SERIAL PRIMARY KEY,
                    number INT
                    )'''
    cur.execute(create_sql)
    conn.commit()
    cur.close()
