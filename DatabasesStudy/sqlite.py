import sqlite3

conn = sqlite3.connect('example.db2')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS stocks (date text, trans text, symbol text, qty real, price real)''')
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

conn.commit()
conn.close()