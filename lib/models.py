from . import CONN, CURSOR

class DadJoke:

    def __init__(self, content):
        self.content = content
        self.id = None

    @classmethod
    def create_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS dad_jokes_table (
            id INTEGER PRIMARY KEY,
            content TEXT
        );
        """
        CURSOR.execute(sql)
        CONN.commit()

    def create(self):
        sql = "INSERT INTO dad_jokes_table (content) VALUES ( ? );"

        CURSOR.execute(sql, [self.content])
        CONN.commit()

        last_row_sql = """
        SELECT * FROM dad_jokes_table 
        ORDER BY id DESC 
        LIMIT 1
        """

        last_row_tuple = CURSOR.execute(last_row_sql).fetchone()
        self.id = last_row_tuple[0]


    @classmethod
    def read_all(cls):
        sql = """
        SELECT * FROM dad_jokes_table;
        """

        all_jokes_tuples = CURSOR.execute(sql).fetchall()

        return all_jokes_tuples
    
    @classmethod
    def delete_by_id(cls, id):
        sql = """
        DELETE FROM dad_jokes_table WHERE id = ?;
        """

        CURSOR.execute(sql, [id])
        CONN.commit()