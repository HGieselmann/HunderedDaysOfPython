import pandas as pd

squirrel_data = pd.read_csv("Squirrel_Data.csv")
squirrel_colors = squirrel_data["Primary Fur Color"]
sum_gray = squirrel_colors.str.count('Gray').sum()
sum_cinnamon = squirrel_colors.str.count('Cinnamon').sum()
print(sum_gray)
print(sum_cinnamon)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon"],
    "Count": [sum_gray, sum_cinnamon]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")