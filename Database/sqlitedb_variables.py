#!/usr/local/bin/python3

# Insert into tables dynamically.

import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('bluehive.db')
c = conn.cursor()

def table_create():
    c.execute('CREATE TABLE IF NOT EXISTS lyricsText(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

def data_entry():
    c.execute("INSERT INTO lyricsText VALUES(12334234,'2017-03-16', 'python', 5)")
    conn.commit()
    c.close()
    conn.close()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'python'
    value = random.randrange(0,10)
    c.execute("INSERT INTO lyricsText (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)", (unix, date, keyword, value))
    conn.commit()


#table_Create()
#data_entry()

for x in range(10):
    dynamic_data_entry()
    time.sleep(1)

c.close()
conn.close()

