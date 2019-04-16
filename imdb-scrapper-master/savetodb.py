import sys
import mysql.connector as mc

try:
    connection = mc.connect(host="localhost",
                            user="root",
                            passwd="*******",
                            )
except mc.Error as e:
    print("Error %d: %s" % (e.args[0], e.args[1]))
    sys.exit(1)


def savetomysqldb(query_s, email):
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS tvseries")
    cursor.execute("use tvseries")
    # delete
    sql_command = """
    CREATE TABLE IF NOT EXISTS imdbinfo ( 
    email NVARCHAR(70) PRIMARY KEY,
    tv_series NVARCHAR(70)
    );"""
    cursor.execute(sql_command)
    q_sql = (email, query_s)

    format_str = """INSERT INTO imdbinfo (email,tv_series)
    VALUES (%s,%s);"""

    cursor.execute(format_str, q_sql)

    connection.commit()
    cursor.close()
    connection.close()
