import psycopg2

params = {
    "host": "localhost",
    "port": 5432,
    "dbname": "postgresdb",
    "user": "postgresadmin",
    "password": "admin123"
}

conn = psycopg2.connect(**params)

cur = conn.cursor()
cur.execute("SELECT version()")
version = cur.fetchone()

print(f"Postgres version: {version}")
