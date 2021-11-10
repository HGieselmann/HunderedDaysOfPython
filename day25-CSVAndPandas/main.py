import csv
import pandas

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     print(data)
#     temperatures = []
#     for row in data:
#         try:
#             temperatures.append(int(row[1]))
#         except:
#             pass
#
#     print(temperatures)


import pandas as pd

data = pd.read_csv("weather_data.csv")
print(data[" temperature"])

data_list = data[" temperature"].to_list()
avg_temp = sum(data_list)/ len(data_list)
print(avg_temp)
print(data[" temperature"].max())

print(data[data.day == "Monday"]) #prints a row
