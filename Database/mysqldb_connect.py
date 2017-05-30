#!/usr/bin/python

## connect to the mysql database.


import mysql.connector

cnx = mysql.connector.connect(user='root', password='Passw0rd',
                              host='127.0.0.1',
                              database='marketer')

c = cnx.cursor
x = c.execute("SELECT * FROM users")
print(x.fetchall())
c.close()
cnx.close()
