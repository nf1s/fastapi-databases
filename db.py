from fastapi_databases import FastAPIDatabases
import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

db = FastAPIDatabases(os.environ["DATABASE_URL"])
