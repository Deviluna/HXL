from tools import sql

sql_now=sql.sql_tools()
#sql.get_books()
while True:
    name=input("book's name:")
    category=input("category:")
    info={"name":name,"category":category}
    sql_now.insert_book(info)
