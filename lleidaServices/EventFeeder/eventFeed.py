#!/usr/bin/python

# Title           :eventFeeder.py
# Description     :This will create a header for a python script.
# Author          :Dhanasekara Pandian
# Email           :dhana.s@contecuae.com
# Date            :20191202
# Version         :0.1
# Usage           :python eventFeeder.py
# Notes           :This is proprietary software of i2i Telesource India Pvt Ltd.
# Python_version  :3.6

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import base64

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:rootadmin@localhost/narpourl_market'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class tbl_event_notify(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tbl_event_notify_eventid = db.Column(db.String(50))
    tbl_event_notify_event_date = db.Column(db.String(100))
    tbl_event_notify_event_name = db.Column(db.String(50))
    tbl_event_notify_event_rcode = db.Column(db.String(50))
    tbl_event_notify_event_b64info = db.Column(db.String(1000))
    is_processed = db.Column(db.Boolean, unique=False, default=False)


@app.route('/postme', methods=['POST'])
def postme():
    if request.method == 'POST':
        print(request.form)
        if request.form['eventid'] and request.form['eventdate']:
            msg = str((str.rstrip(request.form['b64info'][:-5])) + '=')
            message = (base64.b64decode(msg).decode('utf-8'))
            record = tbl_event_notify(tbl_event_notify_eventid=request.form['eventid'],
                                      tbl_event_notify_event_date=request.form['eventdate'],
                                      tbl_event_notify_event_name=request.form['eventname'],
                                      tbl_event_notify_event_rcode=request.form['rcode'],
                                      tbl_event_notify_event_b64info=message,
                                      is_processed=False)
            db.session.add(record)
            db.session.commit()
            return request.form['eventname']
    else:
        return "Only POST is accepted with appropriate value"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)