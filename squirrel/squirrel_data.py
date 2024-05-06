import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census.csv")
data.to_excel("2018_Central.xlsx")
Gray_Squirrel = data[data["Primary Fur Color"] == 'Gray']
Count_Gray = len(Gray_Squirrel)
Cinnamon_Squirrel = data[data["Primary Fur Color"] == 'Cinnamon']
Count_Cinnamon = len(Cinnamon_Squirrel)
Black_Squirrel = data[data["Primary Fur Color"] == 'Black']
Count_Black = len(Black_Squirrel)

data_dict = {
    "Fur_Color": ["Gray", "Cinnamon", "Black"],
    "Count": [Count_Gray, Count_Cinnamon, Count_Black],
}

print(data_dict)

df = pandas.DataFrame(data_dict)
print(df)

df.to_csv("Squirrel_count.csv")
df.to_json("Squirrel_count.json")
df.to_excel("Squirrel.xlsx")