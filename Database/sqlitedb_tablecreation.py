#!/usr/local/bin/python3

# this for sqlite database and creation first program
# if sqlite3 is not importing then install libsqlite3-devel package and re-compile the python3.
# make; make install from the python3 path.

''' order of steps for sqlite3.
1. Connect into the database
2. Position the cursor
3. Execute the command such as create/ insert the tables or query the tables.

Addon SQL lite manager in firefox...install add-on sqllite manager
Open Firefox --> Tools --> WebDeveloper --> Sqlitemanager   (or) Open Firfox --> Tools --> SqliteManager
Open the required database and use it.
'''

import sqlite3

# it is does if its existing or not it creates new database.
conn = sqlite3.connect("bluehive.db")
c = conn.cursor()

def table_Create():
    c.execute('CREATE TABLE IF NOT EXISTS lyricsText(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

def data_entry():
    c.execute("INSERT INTO lyricsText VALUES(12334234,'2017-03-16', 'python', 5)")
    conn.commit()
    c.close()
    conn.close()

#table_Create()
data_entry()