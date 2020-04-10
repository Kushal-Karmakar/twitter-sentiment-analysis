import sqlite3

from app.models import InitModel


class Connection():

    def __init__(self):
        try:
            self.init_model = InitModel()
            self.sql = self.init_model.sql
            self.db_location = self.init_model.db_location
            self.connection = sqlite3.connect(database=self.db_location)
            self.create_tables()

        except Exception as ex:
            print('Error in Connection(): {}'.format(str(ex)))

    def create_tables(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute(self.sql.sql_for_create_users_table)
            cursor.execute(self.sql.sql_for_create_hashtag_table)
            self.connection.commit()

        except Exception as ex:
            print('Error in Connection.create_tables(): {}'.format(str(ex)))
