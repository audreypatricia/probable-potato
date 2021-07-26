# with open("weather_data.csv") as file:
#     data = file.readlines()
#
# print(data)

# using the csv import to read and use the csv data
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file) # will create a csv data object reader
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))  # panda dataFrame object - like an excel sheet ( the whole table)
# print(data)
print(data["temp"])  # here you are specifying the column name
# print(type(data["temp"]))  # panda series object - a column is a series

data_dict = data.to_dict()  # changes it into a dictionary
print(data_dict)

temp_list = data["temp"].to_list()  # changes it to a list
# length = len(temp_list)
# sum_temp = sum(temp_list)
# average = sum_temp / length
# print(round(average, 2))
print(data["temp"].mean())  # wow!

max_temp = data["temp"].max()
print(max)

# Get data in columns
print(data["condition"])  # the string has to match the string name exactly, or you can do
print(data.condition)

# Get Data in rows
print(data[data.day == 'Monday'])  # this returns the row you want, pass the specific condition you are searching for


# print the row of data which had the highest temperature
print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
print(monday.condition)

monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# create a dataframe from scratch
data_dict = {
    "student" : ["Amy", "James", "Angela"],
    "score": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")