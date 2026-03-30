from app.db_connection import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("SELECT * FROM Users")

for row in cursor:
    print(row)

cursor.close()
conn.close()