import datetime
import pandas as pd

data = pd.read_csv("data.csv")
print(data)
df = pd.DataFrame(data)
print(df)
day = datetime.datetime.now().day
month = datetime.datetime.now().month

for index, row in data.iterrows():
    if row["month"] == month and row["day"] == day:
        name = row["name"]
        print(f"Today is {name}s Birthday!")

