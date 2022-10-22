import sqlite3
conn=sqlite3.connect("test.db")
cusor=conn.cursor()
cusor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cusor.rowcount()
conn.commit()
cusor.close()
conn.close()