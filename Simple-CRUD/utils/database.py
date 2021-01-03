from typing import List, Tuple # import for type hinting
from utils.database_connection import DatabaseConnection

Book = Tuple[int, str, str, int] # used for type hinting

# Creating the book table
def create_book_table() -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        # SQLite automatically makes `integer primary key` row auto-incrementing
        cursor.execute('CREATE TABLE books (id integer primary key, name text, \
                                            author text, read integer default 0)')

# CREATE - insert book
def insert_book(name: str, author:str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO books (name, author) VALUES (?, ?)', (name, author))

# RETRIEVE - select all books
def get_all_books() -> List[Book]:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books')
        books = cursor.fetchall()
    return books

# UPDATE - update book read status
def mark_book_as_read(name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))

# DELETE - delete a book
def delete_book(name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM books WHERE name=?', (name,))