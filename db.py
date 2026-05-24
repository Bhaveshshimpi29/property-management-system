import mysql.connector  

def connect_db():

    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database="property_management"
    )

    return conn