import psycopg2

url = "postgres://lrctglrv:FzFCcfArbPx4Xqp1ZYNgIOCKGHfnaoQu@kandula.db.elephantsql.com:5432/lrctglrv"

connection = psycopg2.connect(url)

cursor = connection.cursor()

cursor.execute("SELECT * FROM users;")
first_user = cursor.fetchone()

print(first_user)

connection.close()
