    
# ===============================================================
# Pandas module library
# ===============================================================
import pandas
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

