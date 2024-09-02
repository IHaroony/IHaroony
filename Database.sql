// database // SQL 

-- Create tables for the Library Management System

-- Table for Authors
CREATE TABLE IF NOT EXISTS authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

-- Table for Books
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author_id INTEGER,
    publication_year INTEGER,
    genre TEXT,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);

-- Table for Borrowers
CREATE TABLE IF NOT EXISTS borrowers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);

-- Table for Loans
CREATE TABLE IF NOT EXISTS loans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER,
    borrower_id INTEGER,
    loan_date TEXT,
    return_date TEXT,
    FOREIGN KEY (book_id) REFERENCES books(id),
    FOREIGN KEY (borrower_id) REFERENCES borrowers(id)
);


import sqlite3

DATABASE = 'library.db'

def connect_db():
    return sqlite3.connect(DATABASE)

def create_tables():
    with connect_db() as conn:
        cursor = conn.cursor()
        with open('library_schema.sql', 'r') as f:
            cursor.executescript(f.read())
        conn.commit()

def add_author(name):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (name,))
        conn.commit()

def add_book(title, author_id, publication_year, genre):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO books (title, author_id, publication_year, genre) VALUES (?, ?, ?, ?)', 
                       (title, author_id, publication_year, genre))
        conn.commit()

def add_borrower(name, email):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO borrowers (name, email) VALUES (?, ?)', (name, email))
        conn.commit()

def loan_book(book_id, borrower_id, loan_date):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO loans (book_id, borrower_id, loan_date) VALUES (?, ?, ?)', 
                       (book_id, borrower_id, loan_date))
        conn.commit()

def return_book(loan_id, return_date):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE loans SET return_date = ? WHERE id = ?', (return_date, loan_id))
        conn.commit()

def list_books():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT books.id, books.title, authors.name AS author, books.publication_year, books.genre
            FROM books
            JOIN authors ON books.author_id = authors.id
        ''')
        return cursor.fetchall()

def list_borrowers():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM borrowers')
        return cursor.fetchall()

def list_loans():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT loans.id, books.title, borrowers.name AS borrower, loans.loan_date, loans.return_date
            FROM loans
            JOIN books ON loans.book_id = books.id
            JOIN borrowers ON loans.borrower_id = borrowers.id
        ''')
        return cursor.fetchall()

if __name__ == '__main__':
    create_tables()  # Create tables if they don't exist

    # Example usage
    add_author('J.K. Rowling')
    add_book('Harry Potter and the Sorcerer\'s Stone', 1, 1997, 'Fantasy')
    add_borrower('John Doe', 'john@example.com')
    loan_book(1, 1, '2024-01-15')

    print('Books in the library:')
    for book in list_books():
        print(book)

    print('\nBorrowers:')
    for borrower in list_borrowers():
        print(borrower)

    print('\nLoans:')
    for loan in list_loans():
        print(loan)

python library_system.py
