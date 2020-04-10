import os

from app.models.SQL import SQL


class InitModel():

    def __init__(self):
        self.sql = SQL()
        self.filename = "app\database\TwitterDB.db"
        self.db_location = os.path.join(os.getcwd(), self.filename)
        print(self.db_location)

