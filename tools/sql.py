import sqlite3
# -- coding:utf-8 --
class sql_tools:
	def __init__(self):
		self.conn=sqlite3.connect('tools/library.db')
		self.cursor=self.conn.cursor()

	def create_database(self):
		self.cursor.execute('''
			create table books(
				id integer primary key autoincrement,
				name text not null,
				category text not null);''')
		self.cursor.commit()


	def insert_book(self,book_info):
		self.conn.execute('''
			insert into books (name,category) values (" '''+book_info['name']+'","'+book_info['category']+'''");
			''')
		self.conn.commit()

	def get_books(self):
		self.cursor.execute('select * from books')
		values=self.cursor.fetchall()
		print(values)
		return values

	def get_books_with_category(self,category):
		self.cursor.execute('select * from books where category="'+category+'"')
		values=self.cursor.fetchall()
		print(values)
		return values

	def delete_book_by_id(self,book_id):
		book=self.cursor.execute('select * from books where id="'+book_id+'"')
		values=self.cursor.fetchall()
		user_input=input('Input "yes" to delete the book'+str(values[0]))
		if user_input!="yes":
			pirnt("quit")
			return
		self.conn.execute('delete from books where id ="'+book_id+'"')
		self.conn.commit()

	def close(self):
		self.conn.close()
