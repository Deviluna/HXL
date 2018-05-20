from flask import Flask,render_template
import os
from tools import sql
# -- coding: utf-8 --

app=Flask(__name__)



@app.route("/")
def index():
	sql_now=sql.sql_tools()
	books=sql_now.get_books()
	sql_now.close()
	return render_template('index.htm',books=books)


if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)
