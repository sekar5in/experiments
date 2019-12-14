#!/usr/bin/python

# Title           :lleidaClient.py
# Description     :lleida API Services Client
# Author          :Dhanasekara Pandian
# Email           :dhana.s@contecuae.com
# Date            :20191202
# Version         :0.1
# Usage           :python lleidaClient.py
# Notes           :This is proprietary software of i2i Telesource India Pvt Ltd.
# Python_version  :3.6

from lleidaServices import PyLleida
import sqlalchemy as db
import re
import logging
import logging.config
import configparser


def db_connect(logger, **kwargs):
    db_user = kwargs.get('user')
    db_pass = kwargs.get('password')
    db_host = kwargs.get('host')
    db_database = kwargs.get('database')
    connect_str = str("mysql://" + db_user + ":" + db_pass + "@" + db_host + "/" + db_database)
    engine = db.create_engine(connect_str)
    logger.info("database connection initialized")
    connection = engine.connect()
    metadata = db.MetaData()
    logger.info("database connection established")
    return engine, connection, metadata


def tbl_event_record_insert(logger, obj, engine, connection, metadata):
    resp = get_list_pdf(logger, obj)
    values_list = []
    logger.info("tbl_event_record_insert started")
    tbl_lleida_record = db.Table('tbl_event_record', metadata, autoload=True, autoload_with=engine)
    query = tbl_lleida_record.select()
    row = connection.execute(query)
    row_record = row.fetchall()
    logger.info("tbl_event_record query completed.")
    for record in resp['result']['pdf_list']['pdf_row']:
        rec_status = list(row[1] for row in row_record if row[1] == record['mail_id'])

        subj = record["mail_subj"].split(':')  # ['SUBJ', 'Order # 1208 has been placed successfully']
        order_id = re.findall(r'\d+', str(subj[-1:]))  # NarPorul.com: Order # 1208 has been placed successfully

        if not rec_status:
            values_list.append(
                {'mail_id': record["mail_id"], 'mail_date': record["mail_date"], 'mail_to': record["mail_to"],
                 'mail_from': record["mail_from"], 'mail_subj': record["mail_subj"], 'order_id': "".join(order_id),
                 'is_processed': False, 'file_id': 0 , 'add_id': 0})
    try:
        if values_list:
            insert_query = db.insert(tbl_lleida_record)
            connection.execute(insert_query, values_list)
            logger.info("xml list_pdf mail_id details are inserted into table")
    except Exception as e:
        print("some error")
        print(e)
    logger.info("tbl_event_record_insert completed")

# method of Document Certificate generation
def doc_cert_generate(logger, obj, engine, connection, metadata, custom_cert_path):
    logger.info("tbl_cert_generate started")
    tbl_lleida_record = db.Table('tbl_event_record', metadata, autoload=True, autoload_with=engine)
    cert_query = tbl_lleida_record.select(tbl_lleida_record.c.is_cert_processed == 0)
    cert_row = connection.execute(cert_query)
    row_record = cert_row.fetchall()
    logger.info("filter of table query only non cert generated record done")
    for row in row_record:
        # Just a final actual activity begins.
        logger.info("Mail_id %s is processing", row[1])
        resp = obj.list_pdf(mail_id=row[1])
        custom_name = row[6]        # Order id is custom name for the downloaded pdf.
        file_id = resp.get('result').get('pdf_list').get('pdf_row').get('file_id')
        if file_id:
            logger.info("file id %s is found", file_id)
            cert_pdf_resp = obj.download_pdf(file_id=file_id,custom_path=custom_cert_path, custom_name = custom_name)
            logger.info(cert_pdf_resp)
            logger.info("pdf downloaded")
            cert_update_query = tbl_lleida_record.update().where(tbl_lleida_record.c.id == row[0]).values(is_cert_processed=1)
            connection.execute(cert_update_query)
            logger.info("updated event record table with is_cert_processed as completed")
    logger.info("tbl_cert_generate completed")

# method of Document addendum generation
def doc_addendum_generate(logger, obj, engine, connection, metadata, custom_addendum_path):
    logger.info("doc_addendum_generate started")
    tbl_lleida_record = db.Table('tbl_event_record', metadata, autoload=True, autoload_with=engine)
    cert_query = tbl_lleida_record.select(tbl_lleida_record.c.is_addendum_processed == 0)
    cert_row = connection.execute(cert_query)
    row_record = cert_row.fetchall()
    logger.info("filter of table query only non addendum generated record done")
    for row in row_record:
        # Just a final actual activity begins.
        logger.info("Mail_id %s is processing", row[1])
        resp = obj.list_pdf(mail_id=row[1])
        custom_name = row[6]
        add_id = resp.get('result').get('pdf_list').get('pdf_row').get('add_id')
        if add_id:
            logger.info("add id %s is found", add_id)
            adden_pdf_resp = obj.download_pdf(file_id=add_id,custom_path=custom_addendum_path, custom_name=custom_name)
            logger.info(adden_pdf_resp)
            logger.info("pdf downloaded")
            adden_update_query = tbl_lleida_record.update().where(tbl_lleida_record.c.id == row[0]).values(is_addendum_processed=1)
            connection.execute(adden_update_query)
            logger.info("updated event record table with is_addendum_processed as completed")
    logger.info("doc_addendum_generate completed")

# method to get default settings
def get_default_settings(logger, obj):
    try:
        logger.info("get_default_settings started")
        resp = obj.get_default_settings()
        logger.info("get_default_settings completed")
        return resp
    except Exception as e:
        logging.info(e)
        exit(1)


# method to get default settings
def get_list_pdf(logger, obj):
    try:
        logger.info("get_list_pdf started")
        resp = obj.list_pdf()
        logger.info("get_list_pdf Completed")
        return resp
    except Exception as e:
        logging.info(e)
        exit(1)


# method to set default settings
def set_default_settings(logger, obj):
    try:
        logger.info("set_default_settings started")
        resp = obj.set_default_settings(admin_cgi='http://pi.labs.quehive.com:8000/postme', cert_lang='EN')
        logger.info("set_default_settings Completed")
        return resp
    except Exception as e:
        logging.info(e)
        exit(1)


# Main method definition
def main():

    # logging object initialization
    logging.config.fileConfig(fname='lleidaServices/conf/logger.ini', disable_existing_loggers=False)
    logger = logging.getLogger('lleidalogger')
    logger.info("Application Initialized")
    logger.info("All tasks are started")

    # Config Parser from config.ini file
    config = configparser.ConfigParser()
    config.read('lleidaServices/conf/config.ini')

    # Object initialization
    pylleida_username = config.get('PyLleida','username')
    pylleida_password = config.get('PyLleida','password')
    obj = PyLleida(username=pylleida_username, password=pylleida_password)

    # Database and Cursor Connection.
    db_user = config.get('mysqld','user')
    db_password = config.get('mysqld','password')
    db_host  = config.get('mysqld','host')
    db_database = config.get('mysqld','database')
    engine, connection, metadata = db_connect(logger, user=db_user, password=db_password, host=db_host, database=db_database)

    # Method to get default settings
    # resp = get_default_settings(logger, obj)
    # print(resp)

    # Method to set default settings
    # resp = set_default_settings(logger, obj)
    # print(resp)

    # Method to list all documents.
    tbl_event_record_insert(logger, obj, engine, connection, metadata)

    # Method of Document certificate generation process.
    custom_cert_path = config.get('custom_cert_path', 'cert_path')
    doc_cert_generate(logger, obj, engine, connection, metadata, custom_cert_path)

    # Method of Document certificate generation process.
    custom_addendum_path = config.get('custom_addendum_path', 'addendum_path')
    doc_addendum_generate(logger, obj, engine, connection, metadata, custom_addendum_path)
    logger.info("All tasks are Completed")


# Boiler Plate
if __name__ == '__main__':
    main()
