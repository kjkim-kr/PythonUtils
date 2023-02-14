import cx_Oracle


class OracleDBModule:
    def __init__(self, db_id, db_pw, db_path, db_encoding='UTF-8'):
        self.db = cx_Oracle.connect(db_id, db_pw, db_path, encoding=db_encoding)
        self.cursor = self.db.cursor()
        pass

    def close(self):
        if self.db:
            self.db.close()

    def run_query(self, query):
        try:
            res = self.cursor.execute(query)
        except cx_Oracle.DatabaseError:
            return None

        if self.cursor.description:
            keys = [d[0] for d in self.cursor.description]
        else:
            keys = []

        return res, keys
