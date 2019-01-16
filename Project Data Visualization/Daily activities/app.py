import os

import pandas as pd
import numpy as np
import pandas as pd


from sqlalchemy import create_engine


import pymysql
pymysql.install_as_MySQLdb()

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################
db = pymysql.connect("localhost", "root", "Freehov90@", "activities_db")

app = Flask(__name__)

@app.route('/')
def someName():
   cursor = db.cursor()
   sql = "SELECT sleeping FROM mf_under_6"
   cursor.execute(sql)
   results = cursor.fetchall()
   #return render_template('index.h, results=results)
   return jsonify(results)
if __name__ == '__main__':
 app.run(debug=True)

