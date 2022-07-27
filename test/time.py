import datetime
import random

import requests as requests


parameters = {
    "name": "Stefan"
}
r = requests.get("https://api.genderize.io", params=parameters)
r.raise_for_status()
r = r.json()["gender"]



t_list = ["Hello", "World"]

time = datetime.datetime.now()

print(f"{time.strftime('%B')} {time.day}, {time.year}")