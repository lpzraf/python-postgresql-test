# DB_HOST="localhost"
# DB_NAME="learning"
# DB_USER=""
# DB_PW=""

import psycopg2

conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="dummypw",
    host="localhost"
)

cur = conn.cursor()

cur.execute("select * from users")

rows = cur.fetchall()

for user in rows:
    print(f"id: {user[0]}, age: {user[1]}, name: {user[2]}")

cur.close()
conn.close()