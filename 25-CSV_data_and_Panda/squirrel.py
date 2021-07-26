import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_fur_count = len(data[data["Primary Fur Color"] == 'Gray'])
red_fur_count = len(data[data["Primary Fur Color"] == 'Cinnamon'])
black_fur_count = len(data[data["Primary Fur Color"] == 'Black'])

fur_dictionary = {
    "Fur Color": ['grey', 'red', 'black'],
    "Count": [gray_fur_count, red_fur_count, black_fur_count],
}

print(fur_dictionary)
data = pandas.DataFrame(fur_dictionary)
data.to_csv("squirrel_fur_data.csv")
