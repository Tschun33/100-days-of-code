import datetime
import random

import requests as requests

time = datetime.datetime.now().strftime("%Y")
parameters = {
    "name": "Stefan"
}
r = requests.get("https://api.genderize.io", params=parameters)
r.raise_for_status()
r = r.json()["gender"]
print(r)


t_list = ["Hello", "World"]
print(random.choice(t_list))
