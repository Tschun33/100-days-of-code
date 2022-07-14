import smtplib
import time
import requests
from datetime import datetime

MY_LAT = 52.375893  # Your latitude
MY_LONG = 9.732010  # Your longitude


# Check if the ISS is within +5 or -5 degrees from your location
def is_near():
    """returns true if the ISS is near the current location"""
    r = requests.get(url="http://api.open-notify.org/iss-now.json")
    r.raise_for_status()
    data = r.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    else:
        return False

# Check if its night at the current location
def is_night():
    """"return true if it is night at the current location"""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    r = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    r.raise_for_status()
    data = r.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now <= sunrise or time_now >= sunset:
        return True
    else:
        return False

# Then send me an email to tell me to look up.
# while True:
#     time.sleep(60)
#     if is_night() and is_night():
#         connection = smtplib.SMTP("smtp.gamil.com")
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=MY_EMAIL,
#             msg="Subject: Look UP\\The ISS is above"
#         )
#         pass
