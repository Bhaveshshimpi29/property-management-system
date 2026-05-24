from db import connect_db


def login():

    conn = connect_db()

    cursor = conn.cursor()

    username = input("Enter Username: ")

    password = input("Enter Password: ")

    query = """
    SELECT * FROM users
    WHERE user_name = %s AND user_password = %s
    """

    values = (username, password)

    cursor.execute(query, values)

    user = cursor.fetchone()

    conn.close()

    if user:

        print("\n✅ Login Successful!")

        return user

    else:

        print("\n❌ Invalid Username or Password")

        return None