#!/usr/local/bin/python3

# This is the script to send email as html message / template.

from email.mime.text import MIMEText
import smtplib

msg = MIMEText("<h1> Welcome ! </h1> <h2> Lyricsopedia Users </h2> <p> We are happy to see you at this moment on our newsletter </p>", "html")

msg['Subject'] = 'Welcome to LyricsOpedia'
msg['From'] = 'ownhomautomation@gmail.com'
msg['To'] = 'sekar5in@gmail.com'

s = smtplib.SMTP('localhost')
s.sendmail('root@localhost', ['root@localhost'], msg.as_string())

print("You email has sent")

