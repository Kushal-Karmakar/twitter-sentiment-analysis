

class SQL():

    sql_for_create_users_table = "CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT NOT NULL, password TEXT NOT NULL, email TEXT, phone TEXT, first_name TEXT NOT NULL, last_name NOT NULL, address TEXT, registration_no TEXT, speciality TEXT,is_admin INT DEFAULT 0)"

    sql_for_create_hashtag_table = "CREATE TABLE IF NOT EXISTS Hashtags (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, hashtag TEXT NOT NULL, is_activated INT DEFAULT 1)"

    sql_for_create_sentiment_analysis_operation_table = "CREATE TABLE IF NOT EXISTS TwitterSentimentAnalysis (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, operation TEXT NOT NULL)"

    sql_for_insert_sentiment_analysis_operation = "INSERT INTO TwitterSentimentAnalysis (operation) VALUES ('OR')"

    sql_to_get_sentiment_analysis_operation = "SELECT * FROM TwitterSentimentAnalysis"

    sql_for_update_sentiment_analysis_operation = "UPDATE TwitterSentimentAnalysis SET operation = '{0}' WHERE id = 1"

    sql_for_check_operation = "SELECT COUNT(*) AS COUNT FROM TwitterSentimentAnalysis"

    sql_for_insert_hashtag = "INSERT INTO Hashtags (hashtag,is_activated) VALUES ('{0}','{1}')"

    sql_for_check_existing_hashtag = "SELECT COUNT(*) AS COUNT FROM Hashtags WHERE hashtag = '{0}'"

    sql_for_activate_hashtag = "UPDATE Hashtags SET is_activated = 1 WHERE hashtag = '{0}'"

    sql_for_deactivate_hashtag = "UPDATE Hashtags SET is_activated = 0 WHERE hashtag = '{0}'"

    sql_for_get_all_hashtags_data = "SELECT * FROM Hashtags"

    sql_for_register_user = "INSERT INTO Users (username,password,email,phone,first_name,last_name,address,registration_no,speciality) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}')"

    sql_for_promote_user = "UPDATE Users SET is_admin = 1 WHERE username = '{0}'"

    sql_for_demote_user = "UPDATE Users SET is_admin = 0 WHERE username = '{0}'"

    sql_for_check_existing_user = "SELECT COUNT(*) AS COUNT FROM Users WHERE username = '{0}'"

    sql_for_select_user = "SELECT * FROM Users WHERE username = '{0}'"

    sql_for_login = "SELECT * FROM Users WHERE username = '{0}' AND  password = '{1}'"

    sql_for_get_all_users_data = "SELECT * FROM Users"