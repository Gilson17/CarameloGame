import sqlite3


class DBProxy:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS ranking
                            (
                                id
                                INTEGER
                                PRIMARY
                                KEY
                                AUTOINCREMENT,
                                name
                                TEXT
                                NOT
                                NULL,
                                score
                                INTEGER
                                NOT
                                NULL
                            )
                            ''')
        self.connection.commit()

    def save_score(self, name: str, score: int):
        self.cursor.execute("INSERT INTO ranking (name, score) VALUES (?, ?)", (name, score))
        self.connection.commit()

    def get_top_10(self):
        self.cursor.execute("SELECT name, score FROM ranking ORDER BY score DESC LIMIT 10")
        return self.cursor.fetchall()
