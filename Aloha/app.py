# Import the dependencies.
import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

print(Base.classes.keys())

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session=Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# List all the available routes
@app.route("/")
def home():
    return (
        f"Aloha! Hawaii Climate Data <br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start> - Start date in YYYY-MM-DD format <br/>"
        f"/api/v1.0/<start>/<end>  - Start and end dates in YYYY-MM-DD format <br/>"
    )

# Return precipation data from the last year

@app.route("/api/v1.0/precipitation")
def precipitation():
    
    # Create a session link from Python to the DB
    session = Session(engine)

    # Calculate the date one year ago from the most recent date in the database
    prev_year = dt.date(2017,8,23) - dt.timedelta(days = 365)

    # Query for the date and precipitation for the last year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()

     # Close session
    session.close()

    # Create a dictionary with date as key and prcp as the value
    precip = {}
    for date, prcp in precipitation:
        precip[date] = prcp

    # Return JSON response
    return jsonify(precip)

# Return a JSON list of stations from the dataset

@app.route("/api/v1.0/stations")
def stations():
    # Create a session link from Python to the DB
    session = Session(engine)

    # Query all stations
    results = session.query(Measurement.station).all()

    # Close session
    session.close()

    # Convert list of tuples 
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)

"""
Query the dates and temperature observations of the most active station
for the previous year of data.
Return a JSON list of temparture observations for the previous year.
"""

@app.route("/api/v1.0/tobs")
def tobs():
    # Create a session link from Python to the DB
    session = Session(engine)

    # Define the station ID for most active station
    station_id = 'USC00519281'

    # Query Measurement for dates and temperature
    results = session.query(
    Measurement.date, Measurement.tobs).\
    filter(Measurement.date >= dt.date(2016, 8, 23)).\
    filter(Measurement.date <= dt.date(2017, 8, 23)).\
    filter(Measurement.station == station_id).all()

    # Close session
    session.close()

    # Convert list of tuples 
    last_12_months_tobs = list(np.ravel(results))

    return jsonify(last_12_months_tobs)

# @app.route("/api/v1.0/<start>")
    # Create a session link from Python to the DB
    # session = Session(engine)   

    # Close session
    # session.close()


# @app.route("/api/v1.0/<start>/<end>")
    # Create a session link from Python to the DB
    # session = Session(engine)   

    # Close session
    # session.close()

if __name__ == "__main__":
    app.run(debug=True)