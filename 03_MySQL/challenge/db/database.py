import os
from dotenv import load_dotenv
from urllib import parse

from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine

load_dotenv()
db_host = os.environ.get("DB_HOST")
db_user = os.environ.get("DB_USER")
db_pass = parse.quote_plus(os.environ.get("DB_PASS"))
db_name = os.environ.get("DB_NAME")
db_port = os.environ.get("DB_PORT")

url = f"mysql+mysqlconnector://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"

if not database_exists(url):
    print(f"Creating {db_name} database...")
    create_database(url)

engine = create_engine(url, echo=True)