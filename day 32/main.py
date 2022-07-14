import datetime
import pandas as pd

data = pd.read_csv("data.csv")
day = datetime.datetime.now().day
month = datetime.datetime.now().month
birthday_tuple = (month, day)

for index, row in data.iterrows():
    if row["month"] == month and row["day"] == day:
        name = row["name"]
        print(f"Today is {name}s Birthday!")


birthday_dic = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
if birthday_tuple in birthday_dic:
    birthday_person = birthday_dic[birthday_tuple]
    print(f"Today is {birthday_person.name}s birthday! Yeah")


