import csv
from statistics import correlation
import numpy as np

import plotly.express as px
with open("cups of coffee vs hours of sleep.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x = "Coffee in ml", y = "sleep in hours")
    fig.show()

def findCorelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between Cups of coffee and sleep in hours is:- \n--->", correlation[0, 1])


def getDataSource(data_path):
    cups = []
    sleep = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            cups.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
    return{"x":cups,"y":sleep}


def setup():
    data_path = "cups of coffee vs hours of sleep.csv"
    datasource = getDataSource(data_path)
    findCorelation(datasource)

setup()