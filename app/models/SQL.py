

class SQL():

    sql_for_create_users_table = "CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT NOT NULL, password TEXT NOT NULL, email TEXT, phone TEXT, first_name TEXT NOT NULL, last_name NOT NULL, address TEXT, is_admin INT DEFAULT 0)"

    sql_for_create_hashtag_table = "CREATE TABLE IF NOT EXISTS Hashtags (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, hashtag TEXT NOT NULL)"

    sql_for_register_user = "INSERT INTO Users (username,password,email,phone,first_name,last_name,address) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}')"

    sql_for_promote_user = "UPDATE Users SET is_admin = 1 WHERE username = '{0}'"

    sql_for_demote_user = "UPDATE Users SET is_admin = 0 WHERE username = '{0}'"

    sql_for_check_existing_user = "SELECT COUNT(*) AS COUNT FROM Users WHERE username = '{0}'"

    sql_for_select_user = "SELECT * FROM Users WHERE username = '{0}'"

    sql_for_login = "SELECT * FROM Users WHERE username = '{0}' AND  password = '{1}'"

    sql_for_get_all_users_data = "SELECT * FROM Users"