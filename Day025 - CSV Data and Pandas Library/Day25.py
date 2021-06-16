"""
with open("weather_data.csv") as file:
    data = file.readlines()

print(data)
"""

"""
import csv
with open("weather_data.csv") as file:
    data = csv.reader(file)
    temps = []
    for row in data:
        temps.append(row[1])
"""

import pandas
data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])

"""
the type of data we get back from reading can be series of a dataFrame
in the above data would be a dataFrame and data["temp"] would be a series
dataframe is like the whole table and a series would be a column of that table
"""

dataDict = data.to_dict()
print(dataDict)

tempList = data["temp"].to_list()
print(tempList)


avgTemp = sum(tempList) / len(tempList)
print(avgTemp)

print(data["temp"].mean())

print(data["temp"].max())


## how to get data from a row 
# data["colName"]
# or data.colName

## how to get data from a row
print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])



print( int( data[data.day == "Monday"].temp ) )


# Create a DataFrame from scratch
dict = {
    "students": ["Amy", "Bob", "Carl"],
    "scores":[76, 56, 65]
}

data = pandas.DataFrame(dict)

print(data)

data.to_csv("studentGrades.csv")