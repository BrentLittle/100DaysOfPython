import pandas

data = pandas.read_csv("NYC Central Park Squirels.csv")

grayCount = len(data[data["Primary Fur Color"] == "Gray"])
cinnamonCount = len(data[data["Primary Fur Color"] == "Cinnamon"])
blackCount = len(data[data["Primary Fur Color"] == "Black"])

dict = {
    "Fur Color":["Gray", "Cinnamon", "Black"],
    "Count":[grayCount, cinnamonCount, blackCount]
}

data = pandas.DataFrame(dict)

data.to_csv("SquirrelCountByFurColor.csv")