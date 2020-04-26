import json

from app.models import InitModel
from app.models.Connection import Connection
from werkzeug.security import generate_password_hash, check_password_hash


class UserModel():

    def __init__(self):
        self.init_model = InitModel()
        self.sql = self.init_model.sql

    def create_user(
            self,
            username,
            password,
            email,
            phone,
            first_name,
            last_name,
            address,
            registration_no,
            speciality
    ):
        try:
            connection_obj = Connection()
            conn = connection_obj.connection
            cursor = conn.cursor()
            query = getattr(self.sql, "sql_for_register_user").format(
                username,
                generate_password_hash(password),
                email,
                phone,
                first_name,
                last_name,
                address,
                registration_no,
                speciality
            )
            cursor.execute(query)
            conn.commit()

        except Exception as ex:
            print('Error in UserModel.create_user(): {}'.format(str(ex)))

        finally:
            conn.close()

    def promote_user(
            self,
            username
    ):
        try:
            connection_obj = Connection()
            conn = connection_obj.connection
            cursor = conn.cursor()
            query = getattr(self.sql, "sql_for_promote_user").format(username)
            cursor.execute(query)
            conn.commit()

        except Exception as ex:
            print('Error in UserModel.promote_user(): {}'.format(str(ex)))
        finally:
            conn.close()

    def demote_user(
            self,
            username
    ):
        try:
            connection_obj = Connection()
            conn = connection_obj.connection
            cursor = conn.cursor()
            query = getattr(self.sql, "sql_for_demote_user").format(username)
            cursor.execute(query)
            conn.commit()

        except Exception as ex:
            print('Error in UserModel.demote_user(): {}'.format(str(ex)))
        finally:
            conn.close()

    def check_existing_user(self, username):
        try:
            connection_obj = Connection()
            conn = connection_obj.connection
            cursor = conn.cursor()
            query = getattr(self.sql, "sql_for_check_existing_user").format(username)
            row = cursor.execute(query).fetchone()
            if row[0] < 1:
                return False
            else:
                return True

        except Exception as ex:
            print('Error in UserModel.check_existing_user(): {}'.format(str(ex)))
            return False
        finally:
            conn.close()

    def login(
            self,
            username,
            password
    ):
        try:
            connection_obj = Connection()
            conn = connection_obj.connection
            cursor = conn.cursor()
            query = getattr(self.sql, "sql_for_select_user").format(username)
            user = cursor.execute(query).fetchone()
            user_details = dict(zip([c[0] for c in cursor.description], user))
            password_verified = check_password_hash(user_details["password"],password)

            if (password_verified):
                query = getattr(self.sql, "sql_for_login").format(username, user_details["password"])
                row = cursor.execute(query).fetchone()
                return dict(zip([c[0] for c in cursor.description], row))
            else:
                return None

        except Exception as ex:
            print('Error in UserModel.login(): {}'.format(str(ex)))
        finally:
            conn.close()

    def get_all_users_data(self):
        data = []
        try:
            connection_obj = Connection()
            conn = connection_obj.connection
            cursor = conn.cursor()
            cursor.execute(self.sql.sql_for_get_all_users_data)
            rows = cursor.fetchall()
            for each_row in rows:
                data.append(dict(zip([c[0] for c in cursor.description], each_row)))
            return data

        except Exception as ex:
            print('Error in UserModel.sql_for_get_all_users_data(): {}'.format(str(ex)))
            return data
        finally:
            conn.close()



