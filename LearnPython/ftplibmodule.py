#!/usr/local/bin/python3

# This program helps to use the ftp library module.

from ftplib import FTP

ftp = ftp('domainname.com')
ftp.login(user='username', passwd = 'password')
ftp.cwd('/specificdomain-or-location')

def grabFile():
    filename = 'filename.txt'
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR' + filename, localfile.write,(1024))
    ftp.quit()
    localfile.close()

def placeFile():
    filename = 'filename.txt'
    ftp.storbinary('STOR' + filename, open(filename, 'rb'))
    ftp.quit()
    
