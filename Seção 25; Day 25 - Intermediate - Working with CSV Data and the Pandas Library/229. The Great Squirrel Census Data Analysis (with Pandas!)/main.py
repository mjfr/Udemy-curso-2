import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Primary Fur Color
color_list = data["Primary Fur Color"].to_list()

gray_color = color_list.count("Gray")
red_color = color_list.count("Cinnamon")
black_color = color_list.count("Black")

color_count_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_color, red_color, black_color]
}

csv_export = pandas.DataFrame(color_count_dict)
csv_export.to_csv("squirrel_count.csv")
