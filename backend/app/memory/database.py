import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

DB_PATH = BASE_DIR / "memory.db"


class Database:

    def __init__(self):
        self.connection = sqlite3.connect(
            DB_PATH,
            check_same_thread=False
        )

        self.create_tables()


    def create_tables(self):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
                solution TEXT,
                result TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        self.connection.commit()


    def add_memory(
        self,
        task: str,
        solution: str,
        result: str
    ):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO memories
            (task, solution, result)

            VALUES (?, ?, ?)
            """,
            (
                task,
                solution,
                result
            )
        )

        self.connection.commit()



    def search_memory(
        self,
        keyword: str
    ):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT task, solution, result
            FROM memories
            WHERE task LIKE ?
            ORDER BY id DESC
            LIMIT 5
            """,
            (
                f"%{keyword}%",
            )
        )


        return cursor.fetchall()
