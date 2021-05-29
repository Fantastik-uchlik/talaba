import psycopg2

print("Starting connection . . . .")
conn = psycopg2.connect(
    host="localhost",
    database="universitet",
    port=5432,
    user="postgres",
    password="1323222"
)
conn.autocommit = True