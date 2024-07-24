import sqlite3
connection= sqlite3.connect("library.db")
cursor= connection.cursor()
create_table_sql="""
CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    year INTEGER
);
"""
cursor.execute(create_table_sql)
connection.commit()
def add_book(title,author,year):
    insert_sql="INSERT INTO books(title,author,year)VALUES(?,?,?)"
    cursor.execute(insert_sql,(title,author,year))
    connection.commit()
def get_books():
    query_sql="SELECT * FROM books"
    cursor.execute(query_sql)
    return cursor.fetchall()
def update_book(book_id, title, author, year):
    update_sql = "UPDATE books SET title = ?, author = ?, year = ? WHERE id = ?"
    cursor.execute(update_sql, (title, author, year, book_id))
    connection.commit()
def delete_book(book_id):
    delete_sql="DELETE FROM books WHERE id =?"
    cursor.execute(delete_sql, (book_id,))
    connection.commit()
while True:
    print("\nLibrary Entry System")
    print("\1. Add a book")
    print("2. view all books")
    print("3. update a book")
    print("4. delete a book")
    print("5. quit")
    choice=input("enter your choice:")
    if choice=="1":
        title=input("enter the title:")
        author=input("enter the author:")
        year=input("enter the year:")
        add_book(title,author,year)
        print("book added sucessfully.")
    elif choice=="2":
        books= get_books()
        if not books:
            print("no books in the library.")
        else:
            for book in books:
                print(f"ID: {book[0]},Title: {book[1]}, Author: {book[2]}, year: {book[3]}")
    elif choice=="3":
        book_id=input("enter the book ID to update:")
        title= input("enter the new title:")
        author=input("enter the new author:")
        year=input("enter the new year:")
        update_book(book_id, title, author, year)
        print("book updated sucessfully.")
    elif choice=="4":
        book_id=input("enter the book ID to delete:")
        delete_book(book_id)
        print("book deleted sucessfully.")
    elif choice=="5":
        connection.close()
        print("exiting the program.")
        break
    else:
        print("invalid choice.please choose a valid option.")
    
    print("\nLibrary Entry System")
    
    
