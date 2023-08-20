import psycopg2

DATABASE = 'test_db'
USER = 'root'
PASSWORD = 'root'
HOST = '127.0.0.1'
PORT = '56555'

connection = psycopg2.connect(
    database=DATABASE,
    user = USER,
    host = HOST,
    password=PASSWORD,
    port=PORT
)

cursor = connection.cursor()
cursor.execute("INSERT INTO instructors(name) VALUES('Percy');")
cursor.execute("INSERT INTO instructors(name) VALUES('Nico');")
connection.commit()
cursor.close()
connection.close()