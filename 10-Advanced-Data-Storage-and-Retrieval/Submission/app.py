import datetime as dt
import numpy as np
import pandas as pd
from sqlalchemy import create_engine, inspect
from flask import Flask, jsonify
import json

engine = create_engine("sqlite:///Resources/hawaii.sqlite")


inspector = inspect(engine)
print(inspector.get_table_names())

print("Column names in measurement table")
columns = inspector.get_columns("measurement")
for c in columns:
    print(c["name"], c["type"])
print("Column names in measurement station:")
columns = inspector.get_columns("station")
for c in columns:
    print(c["name"], c["type"])

#####################################################

app = Flask(__name__)

@app.route("/")
def home():
    print("Client requested the home page from the server")
    return("<h1>Welcome to my home page!</h1>")

@app.route("/api/v1.0/precipitation")
def get_precipitation():
    query = """
            SELECT
                date,
                prcp
            FROM
                measurement
            """
    conn = engine.connect()
    measurement = pd.read_sql(query, con=conn)
    conn.close()
    return jsonify(json.loads(measurement.to_json(orient="records")))

@app.route("/api/v1.0/stations")
def get_stations():
    query = """
            SELECT
               *
            FROM
                station
            """
    conn = engine.connect()
    station = pd.read_sql(query, con=conn)
    conn.close()
    return jsonify(json.loads(station.to_json(orient="records")))

@app.route("/api/v1.0/tobs")
def tobs():
    query = """
        SELECT
            m.date,
            m.prcp,
            m.tobs,
            s.station,
            s.name
        FROM
            measurement m
            join station s on m.station = s.station
        WHERE
            date >= (
                        SELECT
                        date(MAX(date), '-365 day')
                        FROM
                            measurement
                    )
        ORDER BY
            date
        """
    conn = engine.connect()
    combined = pd.read_sql(query, con=conn)
    conn.close()
    return jsonify(json.loads(combined.to_json(orient="records")))


@app.route("/api/v1.0/<start>/<end>")
def to_date(start,end):
    query = f"""
        SELECT
            MIN(prcp),
            AVG(prcp),
            MAX(prcp)
        FROM
            measurement
        WHERE
            (date >= {start}) and (date <={end})
        """
    conn = engine.connect()
    date = pd.read_sql(query, con=conn)
    conn.close()
    return jsonify(json.loads(date.to_json(orient="records")))

    
if __name__ == "__main__":
    app.run(debug=True)