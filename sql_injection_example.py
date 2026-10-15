import sqlite3


def get_user_profile(user_id):
    connection = sqlite3.connect("app.db")
    cursor = connection.cursor()
    query = f"SELECT * FROM users WHERE id = {user_id};"
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    return result


if __name__ == "__main__":
    print(get_user_profile("1 OR 1=1"))
