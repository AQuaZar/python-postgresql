import psycopg2

con = psycopg2.connect(database="database", host="localhost", port="5432")
print("Database opened successfully")

cur = con.cursor()
# cur.execute(
#     """CREATE TABLE test
#       (ID INT PRIMARY KEY     NOT NULL,
#       NAME           TEXT    NOT NULL,
#       AGE            INT     NOT NULL);"""
# )
cur.execute("SELECT * FROM test;")
# print("Table created successfully")
res = cur.fetchall()
# cur.execute("""INSERT INTO test VALUES (1,'Bob',26);""")
# con.commit()
print(res)
con.close()
