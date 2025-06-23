import pymysql
from flask import g

def get_db():
    if 'db' not in g:
        g.db = pymysql.connect(
            host="localhost",
            user="root",
            password="12BRAHIM",  # Remplace par ton vrai mot de passe MySQL
            database="iot_surveillance",
            cursorclass=pymysql.cursors.DictCursor
        )
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
