# with open("weather_data.csv") as our_csv:
# #     data = our_csv.readlines()
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     header = next(data)
#     temperatures = []
#     if header != None:
#         for row in data:
#             temperatures.append(int(row[1]))
#         print(temperatures)

import pandas
# data = pandas.read_csv("weather_data.csv")
# # data_dic = data.to_dict()
# #
# # temp_list = data['temp'].to_list()
# # res = round(sum(temp_list)/len(temp_list))
# # res_2 = data['temp'].mean()
# # print(res, round(res_2))
#
# max_temp = data['temp'].max()
# print(data[data.temp == max_temp])

#Get Data in a whole row

# monday = data[data.day == "Monday"]
# print(monday.temp*9/5+32)
#How to create a DataFrame from scratch

# data_dic = {
#     "students": ["Amy", "Emily", "Ivan"],
#     "scores": [46, 78, 99]
# }
# data = pandas.DataFrame(data_dic )
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data (1).csv")
new_data = data['Primary Fur Color']
our_list = new_data.to_list()
our_dic = {}
new_list = []
fur_list = []
for index in ['Gray', 'Cinnamon', 'Black']:
    new_list.append(our_list.count(index))
    fur_list.append(index)
our_dic['Fur Color'] = fur_list
our_dic['Count'] = new_list
print(our_dic)
data = pandas.DataFrame(our_dic)
data.to_csv("squirrel_count.csv")


