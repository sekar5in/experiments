from pyhive import hive

'''
yum install gcc
yum install libsasl2-dev
pip install thrift+
pip install sasl
pip install thrift_sasl  (Optional)
pip install pyhive
'''

host_name = "192.168.1.4"
port = 10000
user = "admin"
password = "password"
database="test_db"


def hiveconnect(host_name, port, user, password, database):
    conn = hive.Connection(host=host_name, port=port, username=user, password=password,
                           database=database, auth="KERBEROS")
    cur = conn.cursor()

    return cur


# Call above function
cur = hiveconnect(host_name, port, user,password, database)
cur.execute('select item_sk,reason_sk, account_credit from returns limit 5')
result = cur.fetchall()
print(result)
