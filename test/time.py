import datetime

import requests as requests

time = datetime.datetime.now().strftime("%Y")
parameters = {
    "name": "Stefan"
}
r = requests.get("https://api.genderize.io", params=parameters)
r.raise_for_status()
r = r.json()["gender"]
print(r)