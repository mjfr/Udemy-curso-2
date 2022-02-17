# No module used, to work with read data more code would be needed

# with open("weather_data.csv", "r") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# Python inbuilt module to work with csv files

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1].isdigit():
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])
