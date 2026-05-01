# ===============================================================
# Open, Read and Write
# ===============================================================
"""
Working Directory - csv-file/weather_dat.csv

Absolute Path - "/Python/python-angela/csv-file/weather_data.csv"
Relative Path - "../python-angela/csv-file/weather_data.csv" or
                "./csv-file/weather_data.csv"
"""
# with open("./csv-file/weather_data.csv") as data_file:
    
#     # string = file.read()
#     # print(string)

#     data = data_file.readlines()
#     print(data)

# ===============================================================
# CSV module
# ===============================================================
# import csv  

# with open("./csv-file/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     # temperature.remove("temp")
#     # temperature.pop(0)
#     # del temperatures[0]
#     # del temperature[start:end]
#     print(temperatures)
    
# ===============================================================
# Pandas module library
# ===============================================================
# import pandas
# import statistics
# import numpy

# data = pandas.read_csv("weather_data.csv")

# print(data)
# print(data["temp"])

# # Data Frame
# print(type(data))
# # Series
# print(type(data["temp"]))

# # Conversions
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# print(temp_list)

# # Average Temperature
# average = round(sum(temp_list) / len(temp_list), 2)
# print(f"The average temperature is: {average}")
#
# average = round(statistics.mean(temp_list),  2)
# print(f"The average temperature is: {average}")
#
# # average = round(numpy.average(temp_list), 2)
# average = round(numpy.mean(temp_list), 2)
# print(f"The average temperature is: {average}")

# average = round(data["temp"].mean(), 2)
# print(f"The average temperature is: {average}")

# # Maximum Temperature
# max_temp = max(temp_list)
# print(f"The Maximum Temperature is: {max_temp}")
#
# max_temp = data["temp"].max()
# print(f"The Maximum Temperature is: {max_temp}")

# # Get Data in Columns
# print(data["condition"])
# print(data.condition)

# # Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# # Get specific value from the table
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# celsius = monday.temp
# fahrenheit = (celsius * 1.8) + 3
# print(fahrenheit)


# # Create a dataframe from scratch
# data_dict = {
#     "student": ["Amy", "James", "Angela", "Frank"],
#     "scores": [76, 56, 65, 60]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# ===============================================================
# 2018 Central Park Squirrel Census Data Analysis
# ===============================================================

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260328.csv")
black_color_squirrels = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_color_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
gray_color_squirrels = len(data[data["Primary Fur Color"] == "Gray"])

color_count_dict = {
    "Colors" : ["Black", "Cinnamon", "Gray"],
    "Count": [black_color_squirrels, cinnamon_color_squirrels, gray_color_squirrels]
}

df = pandas.DataFrame(color_count_dict)
df.to_csv("squirrel_count.csv")




