import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")

image = "day25states.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("day25states.csv")
states = data["state"].to_list()
total_states = len(states)
found = []

while len(found) < total_states:
    entry = screen.textinput(title=f"Guess the State ({len(found)}/{total_states})", prompt="What's another state?").title().strip()
    if entry in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        x = int(data[data["state"] == entry]["x"])
        y = int(data[data["state"] == entry]["y"])
        t.goto(x, y)
        t.write(entry)
        states.remove(entry)
        found.append(entry)

turtle.mainloop()

# practice stuff below

# with open("day25weatherdata.csv") as f:
#     data = [line.rstrip() for line in f.readlines()]
# print(data)

# import csv
# with open("day25weatherdata.csv") as data_file:
#     data = csv.reader(data_file)
#     temps = []
#     for row in data:
#         try:
#             temp = int(row[1])
#         except ValueError:
#             continue
#         else:
#             temps.append(temp)
#     print(f"{temps=}")

# import pandas
# data = pandas.read_csv("day25weatherdata.csv")
#
# data_dict = data.to_dict()
# print(f"{data_dict=}")
#
# temp_list = data["temp"].to_list()
# print(f"{temp_list=}")
#
# avg_temp = data["temp"].mean()
# print(f"{avg_temp=}")
#
# max_temp = data["temp"].max()
# print(f"{max_temp=}")
#
# hottest_day = data[data["temp"] == max_temp]
#
# def temp_c_to_f(temp):
#     return temp * 9/5 + 32
#
# monday = data[data.day == "Monday"]
# monday_temp_in_f = temp_c_to_f(int(monday.temp))
# print(f"{monday_temp_in_f=}")
#

# import pandas
#
# squirrels = pandas.read_csv("day25squirreldata.csv")
# blacks = squirrels[squirrels["Primary Fur Color"] == "Black"]["Primary Fur Color"].count()
# grays = squirrels[squirrels["Primary Fur Color"] == "Gray"]["Primary Fur Color"].count()
# reds = squirrels[squirrels["Primary Fur Color"] == "Cinnamon"]["Primary Fur Color"].count()
# fur_colors = {
#     "colors": ["Black", "Gray", "Red"],
#     "counts": [blacks, grays, reds]
# }
# pandas.DataFrame(fur_colors).to_csv("day25furcolors.csv")
