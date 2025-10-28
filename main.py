import psycopg2
import time

# Wait a bit to ensure Postgres is up before connecting
time.sleep(5)

try:
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        host="my-postgres",
        database="mydb",
        user="user",
        password="pass"
    )
    print("✅ Connected to the database!")

    # Create a table
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100)
        );
    """)

    # Insert a row
    cur.execute("INSERT INTO students (name) VALUES ('Alice','alice@email.com') RETURNING id;")
    new_id = cur.fetchone()[0]
    conn.commit()

    # Read the row
    cur.execute("SELECT * FROM students;")
    rows = cur.fetchall()

    print("📋 Data in table:")
    for row in rows:
        print(row)

    cur.close()
    conn.close()
    print("✅ Task completed successfully!")

except Exception as e:
    print("❌ Connection failed:", e)
