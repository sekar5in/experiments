#!/usr/local/bin/python3

# This is the sample script to send the email text message to desired recipient.

from email.mime.text import MIMEText
import smtplib


msg = MIMEText("Welcome to the First Email communication for Testing Purpose Only")
msg['Subject'] = 'Welcome to LyricsOpedia'
msg['From'] = 'ownhomautomation@gmail.com'
msg['To'] = 'sekar5in@gmail.com'

s = smtplib.SMTP('localhost')
s.sendmail('root@localhost', ['root@localhost'], msg.as_string())

print("You email has sent")
