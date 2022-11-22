import sqlite3
connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()
cur.execute("insert into posts (title,content) values (?,?)",
('first post','Test 1')
)
cur.execute("insert into posts (title,content) values (?,?)",
('second post','Test 2'))
cur.execute("insert into users values (?,?,?,?,?)",("mahmous97","m1.shawamreh@gmail.com","Mahmoud","shawamreh","08.04.1997"))
cur.execute("delete  from users where psw=?",("08.04.1997",))
connection.commit()
connection.close()