from flask import Flask,render_template
import os
from tools import sql
# -- coding: utf-8 --

app=Flask(__name__)
type_map={"computer":"计算机","math":"数学","foreign":"外文","master":"名著"}


@app.route("/")
def index():
	sql_now=sql.sql_tools()
	books=sql_now.get_books()
	sql_now.close()
	return render_template('index.htm',books=books)

@app.route("/category/<type_in>")
def category(type_in):
    if type_in not in type_map.keys():
        return "no such category:"+type_in
    sql_now=sql.sql_tools()
    books=sql_now.get_books_with_category(type_map[type_in])
    sql_now.close()
    return render_template('index.htm',books=books)


if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)
