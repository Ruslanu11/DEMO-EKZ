import sqlite3
from src.set import BASE_PATH, SCRIPTS_PATH
import os


class DBmanager():
    def __init__(self, db_path: str):
        self.db_path = db_path

    def check_base(self):
        return os.path.exists(self.db_path)

    def connect_base(self):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        return conn, cur

    def cr_base(self, scripts_path: str):
        if not self.check_base():
            conn, cur = self.connect_base()
            cur.executescript(open(scripts_path).read())
            conn.commit()
            conn.close()

    def execute(self, query: str, args=(), many: bool = True):
        conn, cur = self.connect_base()
        res = cur.execute(query, args)
        result = res.fetchall() if many else res.fetchone()
        conn.commit()
        return result

    def initialize(self):
        if not self.check_base():
            from fill_data import DataFiller
            self.cr_base(SCRIPTS_PATH)
            DataFiller.fill_gender()
            DataFiller.fill_patient()
            DataFiller.fill_user()
            DataFiller.fill_staff()
            DataFiller.fill_role()


base_manager = DBmanager(BASE_PATH)


