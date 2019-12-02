#!/usr/bin/python

## connect to the mysql database.


import mysql.connector

cnx = mysql.connector.connect(user='root', password='Passw0rd',
                              host='127.0.0.1',
                              database='lop')

c = cnx.cursor()
c.execute("SELECT * FROM loptamil")
rel = c.fetchall()
print(rel)
c.close()
cnx.close()
