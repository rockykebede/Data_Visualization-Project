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

engine = create_engine("mysql://root:Freehov90@@localhost:3306/activities_db")
conn = engine.connect()

session = Session(bind=engine)

Combined = pd.read_sql("SELECT * FROM combined", conn)
Activities_data=pd.read_sql("SELECT * FROM activities_data", conn)

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/maritalstatus")
def maritalstatus():
<<<<<<< HEAD
    """Return list Mstatus."""

    # Use Pandas to perform the sql query
   
    df = pd.read_sql_query("SELECT MStatus FROM Combined", conn)

    # Return a list of MStatus values
    return jsonify(list(df.columns)[2:])
print(maritalstatus)

@app.route("/combineddata/<MStatus>")
def combineddata(Mstatus):
    """Return the combined for a MStatus."""
=======
    """Return list martiastatus (Mstatus)."""

    # Use Pandas to perform the sql query
    
    df = pd.read_sql_query("SELECT Mstatus FROM Combined", conn)

    # Return a list of Mstatus values
    return jsonify(list(df.columns)[2:])
print(maritalstatus)

@app.route("/combineddata/<Mstatus>")
def combineddata(Mstatus):
    """Return the combined for a Mstatus."""
>>>>>>> bcf855daf8642f10aa33b35d659e18a92a6c8310
    sel = [
        Combined.Mstatus,
        Combined.Housework,
        Combined.Sleeping,
        Combined.Shopping_goods,
        Combined.Working,
            ]

<<<<<<< HEAD
    results = session.query(*sel).filter(Combined.MStatus == MStatus).all()
=======
    results = session.query(*sel).filter(Combined.Mstatus == Mstatus).all()
>>>>>>> bcf855daf8642f10aa33b35d659e18a92a6c8310

    # Create a dictionary entry for each row of Combined dataframe
    combined = {}
    for result in results:
        combined["Mstatus"] = result[0]
        combined["Housework"] = result[1]
        combined["Sleeping"] = result[2]
        combined["Shopping_goods"] = result[3]
        combined["Working"] = result[4]
        

    print(combined)
    return jsonify(combined)

<<<<<<< HEAD
@app.route("/activity_data/<MStatus>")
def acitivity_data(Mstatus):
    """Return `acitivity_IDS, acitivity_labels, Mstatus_values."""
    
    # Filter the data based on MStatus 
    
    sample_data = pd.read_sql("Select activity_ID activity_label MStatus From Activities_data", conn)
    # Format the data to send as json
    data = {
        "acitivity_IDS": sample_data.activity_ID.values.tolist(),
        "Mstatus_values": sample_data[MStatus].values.tolist(),
=======
@app.route("/activity_data/<Mstatus>")
def acitivity_data(MStatus):
    """Return `acitivity_IDS, acitivity_labels, Mstatus_values."""
    
    # Filter the data based on Mstatus 
    
    sample_data = pd.read_sql("Select activity_ID activity_label Mstatus From Activities_data", conn)
    # Format the data to send as json
    data = {
        "acitivity_IDS": sample_data.activity_ID.values.tolist(),
        "Mstatus_values": sample_data[Mstatus].values.tolist(),
>>>>>>> bcf855daf8642f10aa33b35d659e18a92a6c8310
        "acitivity_lables": sample_data.activity_label.tolist(),
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run()