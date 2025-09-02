import pymysql

def connect():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="hotel_system2",
        cursorclass=pymysql.cursors.DictCursor
    )
