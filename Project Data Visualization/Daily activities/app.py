import pymysql
pymysql.install_as_MySQLdb()
import os
import mysqlx
import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
app = Flask(__name__)

engine = create_engine("mysql://root:Mun&maj@0723@localhost:3306/activities_db")
conn = engine.connect()
Base.combined.create_all(conn)
session = Session(bind=engine)

Combined = pd.read_sql("SELECT * FROM combined", conn)
Activities_data=pd.read_sql("SELECT * FROM activities_data", conn)

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/names")
def names():
    """Return list Status."""

    # Use Pandas to perform the sql query
    stmt = session.query(Combined).statement
    df = pd.read_sql_query(pd.read_sql("SELECT Status FROM Combined", conn)

    # Return a list of Status values
    return jsonify(list(df.columns)[2:])
print(names)

@app.route("/combined/<Status>")
def combined(Status):
    """Return the combined for a Status."""
    sel = [
        Combined.Status,
        Combined.Housework,
        Combined.Sleeping,
        Combined.Shopping_goods,
        Combined.Working,
            ]

    results = session.query(*sel).filter(Combined.Status == Status).all()

    # Create a dictionary entry for each row of Combined dataframe
    combined = {}
    for result in results:
        combined["Status"] = result[0]
        combined["Housework"] = result[1]
        combined["Sleeping"] = result[2]
        combined["Shopping_goods"] = result[3]
        combined["Working"] = result[4]
        

    print(combined)
    return jsonify(combined)

@app.route("/samples/<Status>")
def samples(Status):
    """Return `acitivity_IDS, acitivity_labels, sample_values."""
    
    # Filter the data based on Status 
    
    sample_data = pd.read_sql("Select activity_ID activity_label Status From Activities_data", conn)
    # Format the data to send as json
    data = {
        "acitivity_IDS": sample_data.activity_ID.values.tolist(),
        "sample_values": sample_data[Status].values.tolist(),
        "acitivity_lables": sample_data.activity_label.tolist(),
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run()