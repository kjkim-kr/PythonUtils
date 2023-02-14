import pymysql


class MysqlDBModule:
    def __init__(self, db_id, db_pw, db_path,
                 db_name='',
                 db_port=3306,
                 db_encoding='UTF8'):
        self.db = pymysql.connect(host=db_path, user=db_id,
                                  password=db_pw,
                                  db=db_name,
                                  port=db_port,
                                  charset=db_encoding)
        self.cursor = self.db.cursor()
        pass

    def close(self):
        if self.db:
            self.db.close()

    def run_query(self, query):
        try:
            self.cursor.execute(query)
            keys = [k[0] for k in self.cursor.description]
            return self.cursor.fetchall(), keys

        except pymysql.MySQLError:
            pass

        return None
