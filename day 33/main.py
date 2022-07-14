import datetime

import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# response = response.json()
# long = response["iss_position"]["longitude"]
# print(f"The ISS is at Longitude:{long}")

# r = requests.get(url="https://api.kanye.rest")
# r = r.json()
# print(r)

MY_LAT = 52.375893
MY_LONG = 9.732010

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,

}

r = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
r.raise_for_status()
r = r.json()["results"]["sunrise"]
print(r)
print(datetime.datetime.now())