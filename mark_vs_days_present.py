import csv
from statistics import correlation
import numpy as np

import plotly.express as px
with open("Student Marks vs Days Present.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x = "Marks In Percentage", y = "Days Present")
    fig.show()

def findCorelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between Marks In Pecentage and Days present of Student is:- \n--->", correlation[0, 1])


def getDataSource(data_path):
    mark = []
    dp = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            mark.append(float(row["Marks In Percentage"]))
            dp.append(float(row["Days Present"]))
    return{"x":mark,"y":dp}


def setup():
    data_path = "Student Marks vs Days Present.csv"
    datasource = getDataSource(data_path)
    findCorelation(datasource)

setup()