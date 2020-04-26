from app.models import InitModel
from app.models.Connection import Connection


class HashtagModel():

    def __init__(self):
        self.init_model = InitModel()
        self.sql = self.init_model.sql

    def create_hashtag(
            self,
            hashtag
    ):
        try:
            connection_obj = Connection()
            conn = connection_obj.connection
            cursor = conn.cursor()
            query = getattr(self.sql, "sql_for_insert_hashtag").format(
                hashtag,
                1
            )
            cursor.execute(query)
            conn.commit()

        except Exception as ex:
            print('Error in HashtagModel.create_hashtag(): {}'.format(str(ex)))

        finally:
            conn.close()

    def check_existing_hashtag(self, hashtag):
        try:
            connection_obj = Connection()
            conn = connection_obj.connection
            cursor = conn.cursor()
            query = getattr(self.sql, "sql_for_check_existing_hashtag").format(hashtag)
            row = cursor.execute(query).fetchone()
            if row[0] < 1:
                return False
            else:
                return True

        except Exception as ex:
            print('Error in HashtagModel.check_existing_hashtag(): {}'.format(str(ex)))
            return False
        finally:
            conn.close()

    def activate_hashtag(
            self,
            hashtag
    ):
        try:
            connection_obj = Connection()
            conn = connection_obj.connection
            cursor = conn.cursor()
            query = getattr(self.sql, "sql_for_activate_hashtag").format(hashtag)
            cursor.execute(query)
            conn.commit()

        except Exception as ex:
            print('Error in HashtagModel.activate_hashtag(): {}'.format(str(ex)))
        finally:
            conn.close()

    def deactivate_hashtag(
            self,
            hashtag
    ):
        try:
            connection_obj = Connection()
            conn = connection_obj.connection
            cursor = conn.cursor()
            query = getattr(self.sql, "sql_for_deactivate_hashtag").format(hashtag)
            cursor.execute(query)
            conn.commit()

        except Exception as ex:
            print('Error in HashtagModel.deactivate_hashtag(): {}'.format(str(ex)))
        finally:
            conn.close()

    def get_all_hastags_data(self):
        data = []
        try:
            connection_obj = Connection()
            conn = connection_obj.connection
            cursor = conn.cursor()
            cursor.execute(self.sql.sql_for_get_all_hashtags_data)
            rows = cursor.fetchall()
            for each_row in rows:
                data.append(dict(zip([c[0] for c in cursor.description], each_row)))
            return data

        except Exception as ex:
            print('Error in HashtagModel.get_all_hastags_data(): {}'.format(str(ex)))
            return data
        finally:
            conn.close()