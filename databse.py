import sqlite3

class DatabaseManager:
    def __init__(self, db_name="passsafe.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS credentials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account TEXT NOT NULL,
            password TEXT NOT NULL
        );
        '''
        self.conn.execute(query)
        self.conn.commit()

    def add_credential(self, account, password):
        query = "INSERT INTO credentials (account, password) VALUES (?, ?)"
        self.conn.execute(query, (account, password))
        self.conn.commit()

    def get_credentials(self):
        query = "SELECT * FROM credentials"
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def close(self):
        self.conn.close()
