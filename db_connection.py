import oracledb
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    try:
        connection = oracledb.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            dsn=os.getenv("DB_DSN")
        )
        print("✅ Connected to Oracle successfully")
        return connection
    except Exception as e:
        print("❌ Connection failed:", e)
        return None