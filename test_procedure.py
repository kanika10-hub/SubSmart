from db_connection import get_connection

conn = get_connection()

if conn:
    cursor = conn.cursor()

    try:
        cursor.callproc("add_subscription", 
                        [1, "Netflix",4, 499, "Monthly"])
        conn.commit()
        print("✅ Subscription added successfully")
    except Exception as e:
        print("❌ Error:", e)

    cursor.close()
    conn.close()