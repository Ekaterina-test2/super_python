from sqlalchemy import create_engine, text
import config


class ForBase():
    __scripts = {
        "select": "SELECT * FROM subject WHERE subject_id = :id",
        "delete": "DELETE FROM subject WHERE subject_id = :id",
        "insert_new": "INSERT INTO subject (\"subject_id\", \"subject_title\") VALUES (:subject_id, :subject_title)",
        "update_new": "UPDATE subject SET subject_title = (:newtitle) WHERE subject_id=:id",
        "max_id": "SELECT MAX(subject_id) FROM subject"
    }

    def __init__(self, db_connection_string):
        self.db = create_engine(db_connection_string)

    def insert_subject(self):
        connection = self.db.connect()
        transaction = connection.begin()
        k = text(self.__scripts["insert_new"])
        connection.execute(k, config.old_subject)
        transaction.commit()
        connection.close()

    def select_subject(self, Myid):
        connection = self.db.connect()
        result = connection.execute(text(self.__scripts["select"]), {"id": Myid})
        connection.close()
        return result

    def get_max_id(self):
        connection = self.db.connect()
        maxid = connection.execute(text(self.__scripts["max_id"])).mappings().all()[0]['max']
        connection.close()
        return maxid

    def delete(self, delid):
        connection = self.db.connect()
        transaction = connection.begin()
        connection.execute(text(self.__scripts["delete"]), {"id": delid})
        transaction.commit()
        connection.close()

    def update_subject(self, upid):
        connection = self.db.connect()
        transaction = connection.begin()
        k = text(self.__scripts["update_new"])
        connection.execute(k, {"id": upid, "newtitle": config.update_data})
        transaction.commit()
        connection.close()
