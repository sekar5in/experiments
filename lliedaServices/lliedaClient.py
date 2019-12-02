#!/usr/bin/python

# Title           :lliedaClient.py
# Description     :This will create a header for a python script.
# Author          :Dhanasekara Pandian
# Email           :dhana.s@contecuae.com
# Date            :20191202
# Version         :0.1
# Usage           :python lliedaClient.py
# Notes           :This is proprietary software of i2i Telesource India Pvt Ltd.
# Python_version  :3.6

from lliedaServices import PyLleida
import sqlalchemy as db
import re

#global initialization
obj = PyLleida(username='csdemo', password='Contec123')


def db_connect():
    engine = db.create_engine('mysql+pymysql://root:Passw0rd@localhost/db_lleida')
    connection = engine.connect()
    metadata = db.MetaData()
    return engine, connection, metadata


def tbl_event_notify_select(engine, connection, metadata):
    subj, mail_id, msg_id, r_code, reason, msg_from, order_id = None, None, None, None, None, None, None
    values_list = []
    tbl_event_notify = db.Table('tbl_event_notify', metadata, autoload=True, autoload_with=engine)
    query = tbl_event_notify.select(tbl_event_notify.c.is_processed == 0)       # Filter only is_processed is False
    row = connection.execute(query)
    row_record = row.fetchall()
    for msg in row_record:
        matches = re.findall(r'\w*SUBJ\b', msg[5])            # Matches Subj holding record
        if matches:                                           # if record contains subj and processed
            event_id = msg[1]
            list_str = msg[5].split('\n')
            for line in list_str:
                if 'SUBJ' in line:
                    subj = line.split(':')[1]                 # ['SUBJ', 'Order # 1208 has been placed successfully']
                    # Specific to narporul.com
                    order_id = re.findall(r'\d+', subj)       # NarPorul.com: Order # 1208 has been placed successfully
                if 'MAIL_ID' in line:
                    mail_id = line.split(':')[1]              # ['MAIL_ID', '28887190']
                if 'MSGID' in line:
                    msg_id = line.split(':')[1]               # ['MAIL_ID', '28887190']
                if 'RCODE' in line:
                    r_code = line.split(':')[1]               # ['MAIL_ID', '28887190']
                if 'REASON' in line:
                    reason = line.split(':')[1]               # ['MAIL_ID', '28887190']
                if 'FROM' in line:
                    msg_from = line.split(':')[1]               # ['MAIL_ID', '28887190']

            # Create a dict list of valid alert records from notify table and add as record to lleida record table
            # for processing document generation monitoring.
            values_list.append({'tbl_lleida_record_eventid':event_id, 'tbl_lleida_record_from':msg_from,
                                'tbl_lleida_record_order_id': order_id, 'tbl_lleida_record_subj':subj,
                                'tbl_lleida_record_mail_id': mail_id, 'tbl_lleida_record_msg_id':msg_id,
                                'tbl_lleida_record_rcode':r_code, 'tbl_lleida_record_reason': reason,
                                'is_cert_processed': False, 'is_addendum_processed': False
                                })

        query = tbl_event_notify.update().where(tbl_event_notify.c.id == msg[0]).values(is_processed=1)
        try:
            '''
            Statement of query to execute to change the record of tbl_event_notify processed to True 
            to ignore on next execution
            '''
            connection.execute(query)                        # Execute table eventy notify to change progressed status to completed
            # print(c.rowcount)
        except Exception as e:
            print(e)

    # Insert list of records to table tbl_lleida_record for further processing.
    try:
        if values_list:
            tbl_lleida_record = db.Table('tbl_lleida_record', metadata, autoload=True, autoload_with=engine)
            insert_query = db.insert(tbl_lleida_record)
            connection.execute(insert_query, values_list)
    except Exception as e:
        print(e)


# method of Document Certificate generation
def doc_cert_generate(engine, connection, metadata, custom_cert_path):
    tbl_lleida_record = db.Table('tbl_lleida_record', metadata, autoload=True, autoload_with=engine)
    cert_query = tbl_lleida_record.select(tbl_lleida_record.c.is_cert_processed == 0)
    cert_row = connection.execute(cert_query)
    row_record = cert_row.fetchall()
    for row in row_record:
        # Just a final actual activity begins.
        print(row[4])
        resp = obj.list_pdf(mail_id=row[4])
        custom_name = row[10]
        # print(resp['result']['pdf_list']['pdf_row'])
        file_id = resp.get('result').get('pdf_list').get('pdf_row').get('file_id')
        if file_id:
            print("file id is found")
            print("proceeding with download of pdf")
            cert_pdf_resp = obj.download_pdf(file_id=file_id,custom_path=custom_cert_path, custom_name = custom_name)
            print(cert_pdf_resp)
            print("pdf downloaded")
            cert_update_query = tbl_lleida_record.update().where(tbl_lleida_record.c.id == row[0]).values(is_cert_processed=1)
            connection.execute(cert_update_query)
            print("updated record table with is_cert_processed as completed")


# method of Document addendum generation
def doc_addendum_generate(engine, connection, metadata, custom_addendum_path):
    tbl_lleida_record = db.Table('tbl_lleida_record', metadata, autoload=True, autoload_with=engine)
    cert_query = tbl_lleida_record.select(tbl_lleida_record.c.is_addendum_processed == 0)
    cert_row = connection.execute(cert_query)
    row_record = cert_row.fetchall()
    for row in row_record:
        # Just a final actual activity begins.
        print(row[4])
        resp = obj.list_pdf(mail_id=row[4])
        custom_name = row[10]
        # print(resp['result']['pdf_list']['pdf_row'])
        add_id = resp.get('result').get('pdf_list').get('pdf_row').get('add_id')
        if add_id:
            print("add id is found")
            print("proceeding with download of pdf")
            adden_pdf_resp = obj.download_pdf(file_id=add_id,custom_path=custom_addendum_path, custom_name = custom_name)
            print(adden_pdf_resp)
            print("pdf downloaded")
            adden_update_query = tbl_lleida_record.update().where(tbl_lleida_record.c.id == row[0]).values(is_addendum_processed=1)
            connection.execute(adden_update_query)
            print("updated record table with is_addendum_processed as completed")


# method to get default settings
def get_default_settings():
    resp = obj.get_default_settings()
    return resp


# method to set default settings
def set_default_settings():
    resp = obj.set_default_settings(admin_cgi='http://pi.labs.quehive.com:8000/postme', cert_lang='EN')
    return resp


# Main method definition
def main():

    # Database and Cursor Connection.
    engine, connection, metadata = db_connect()

    # Method to get default settings
    # resp = get_default_settings()
    # print(resp)

    # Method to set default settings
    # resp = set_default_settings()
    # print(resp)

    # Method to select notify table and insert record table of valid events
    tbl_event_notify_select(engine, connection, metadata)

    # Method of Document certificate generation process.
    custom_cert_path = "/sites/narporul/evidences/certificates"
    doc_cert_generate(engine, connection, metadata, custom_cert_path)

    # Method of Document certificate generation process.
    custom_addendum_path = "/sites/narporul/evidences/addendum"
    doc_addendum_generate(engine, connection, metadata, custom_addendum_path)


# Boiler Plate
if __name__ == '__main__':
    main()