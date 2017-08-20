import mysql.connector


def lopConnection():
    try:
        conn = mysql.connector.connect(user='root', password='Passw0rd', host='127.0.0.1', database='lop', buffered=True, charset='utf8')
        c = conn.cursor()
        return c, conn

    except mysql.connector.Error as err:
        if err.errno == err.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == err.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    except AttributeError:
        print('unable to connect db')

    else:
       conn.close()