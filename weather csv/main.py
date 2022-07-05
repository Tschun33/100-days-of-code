import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     i = 1
#     for row in data:
#         try:
#             new_temp = (int(row[1]))
#         except:
#             continue
#         temperatures.append(new_temp)
from statistics import mean

import pandas

data = pandas.read_csv("weather_data.csv")

data_dict = data.to_dict()

print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)
print(round(mean(temp_list), 2))

print(data["temp"].max())
print(data.temp.max())

print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])