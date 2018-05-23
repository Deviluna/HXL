from tools import sql

sql_now=sql.sql_tools()
#sql.get_books()
user_input=input('(1).add a new book\n(2).delte a book by id\n')


if user_input=='1':
    while True:
        name=input("book's name:")
        category=input("category:")
        info={"name":name,"category":category}
        sql_now.insert_book(info)
elif user_input=='2':
    book_id=input('input the id of the book to delete:')
    sql_now.delete_book_by_id(book_id)
