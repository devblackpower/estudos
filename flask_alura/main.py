from flask import Flask
import pymysql


app = Flask(__name__)
app.config.from_pyfile('config.py')

db = pymysql.connect('config.py')    

from views import * 

if __name__ == "__main__":
    app.run(debug=True)