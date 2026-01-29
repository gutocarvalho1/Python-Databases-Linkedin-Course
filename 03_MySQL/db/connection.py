import os
import mysql.connector as mysql
from dotenv import load_dotenv

load_dotenv()

db_host = os.environ.get("DB_HOST")
db_user = os.environ.get("DB_USER")
db_pass = os.environ.get("DB_PASS")
db_name = os.environ.get("DB_NAME")

def connect(db_name):
    try:
        return mysql.connect(
            host=db_host,
            user=db_user,
            password=db_pass,
            database=db_name,
        )
    except Exception as e:
        print(e)