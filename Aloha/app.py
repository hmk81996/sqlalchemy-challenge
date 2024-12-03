# Import the dependencies.
import numpy as np
import pandas as pd

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

# Load the precipitation data into a DataFrame
prcp_data = pd.read_sql("SELECT * FROM climate_starter", engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# List all the availble routes
@app.route("/")
def home():
    return (f"Aloha! Hawaii Climate Data <br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

# Convert the query results from precipitation analysis to a dictionary 
# Use date as the key and prcp as the value
@app.route("/api/v1.0/precipitation", methods=['GET'])
def get_data():
    # Convert existing DataFrame to a dictionary
    data = prcp_data.set_index('Date')['Precipitation'].to_dict()

    # Return JSON response
    return jsonify(data)

# @app.route("/api/v1.0/stations")

# @app.route("/api/v1.0/tobs")

# @app.route("/api/v1.0/<start>")

# @app.route("/api/v1.0/<start>/<end>")


if __name__ == "__main__":
    app.run(debug=True)