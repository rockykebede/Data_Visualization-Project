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

# Create Engine and Pass in MySQL Connection
engine = create_engine("mysql://root:Mun&maj@0723@localhost/actvities_db")
conn = engine.connect()

data = pd.read_sql("SELECT * activities_db", conn)


# Save references to each table
#mf_6_to_17 = Base.classes.MF_6_to_17
#mf_under_6 = Base.classes.MF_under_6
#mm_6_to_17 = Base.classes.MM_6_to_17
#mm_under_6 = Base.classes.MM_under_6 


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html"),

if __name__ == "__main__":
    app.run()
