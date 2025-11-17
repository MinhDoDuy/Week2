import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="aloalo123",
    host="localhost",
    port="5432"
)