# sqlalchemy-challenge
Data Analytics Course Module 10

# Task

I will be doing a climate analysis for Honolulu, Hawaii. I will first complete a precipitation analysis that retrieves the 12 most recent months of precipitation data. Next, I'll find the weather station with the greatest number of observations and collect the 12 most recent months of temperature data. Finally, I'll create a Flask API to present the weather data.

# Methodology
## Exploration
I will use Python and SQLAlchemy to do a basic climate analysis and data exploration of the climate database. I'll use SQLAlchemy ORM queries, Pandas, and Matplotlib.

### Preciptiation Exploration
Working in Jupyter Notebook, I saved references to two classes named 'station' and 'measurement'. To get a better sense of the 'measurement' database, I first displayed the rows and columns in a dictionary format and then used an inspector to view the columns and types. I was able to see the data formatand create a query for the most recent date of 2017-08-23 which I used to calculate the date one year prior. Using this 12 month range, I performed a query to retrieve precipitation data.

### Station Exploration
To get a better sense of the 'station' database, I used an inspector to view the columns and types. I queried stations to organize them by level of acitivty and used the most active station (USC00519281), to calculate the minimum, maximum and average temperatures for the same 12 month range as in the precipitation exploration.

## Preciptiation and Station (Temperature) Analysis
The precipitation data graph shows some trends:
- Honolulu can get up to 7 inches of rain at a time.
- Most precipitation values are below 3 inches.
- Each season seems to have outliers or periods of dramatically increased rainfall. This is an area that could use more exploration.

The summary statistics support the graph. The difference between the mean (.18 inches) and the 50%/median (.02 inches) values indicate that there are some extreme outliers.

The temperature observations graph shows that the greatest frequency of values for the most active station in Honolulu occurs around 75 degrees. The histogram skews towards warmer temperatures and are all in the range of approximately 60-85 degrees.

The min/max/avg calucations provide a more specific range:
Lowest Temperature: 54.0°F
Highest Temperature: 85.0°F
Average Temperature: 71.66378066378067°F

## Flask API
The Flask API provides a number of routes for further exploration and the opportunity to query specific dates and ranges. This is useful to get a sense of historical weather trends so one might plan accordingly for desirable conditions.

Aloha! Hawaii Climate Data
Available Routes:
/api/v1.0/precipitation *A JSON list of dates and precipitation values for one year prior to most recent collection date*
/api/v1.0/stations *A JSON list of station data*
/api/v1.0/tobs *A JSON list of temperature data for the most active station (USC00519281)*
/api/v1.0/ - Enter start date YYYY-MM-DD *A dynamic route for users to return temperature statistics for a desired start date*
/api/v1.0// - Enter start YYYY-MM-DD / end YYYY-MM-DD *A dynamic route for users to return temperature statistics for a desired start and end date*

One area I will continue to work on is cleaning up user entries to the dynamic routes and returning a 404 for date formats that don't match YYYY-MM-DD.