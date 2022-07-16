from tkinter import *
import datetime
import os

import requests

TOKEN = "dsfhjs343438hjdrh8"
USERNAME="infernus2k"
pixela_endpoint = "https://pixe.la/v1/users"
post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/pushups1"
headers = {
    "X-USER-TOKEN": TOKEN,
}

# r = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(r.text)








def send_data():
    now = datetime.datetime.now()
    date = now.strftime("%Y%m%d")
    quant = amount.get()
    post_parameters = {
        "date": date,
        "quantity": quant,
    }

    r = requests.post(url=post_endpoint, json=post_parameters, headers=headers)
    label_response.config(text=r)


root = Tk()

amount = Entry(widt=10)
amount.grid(column=1, row=0)

label_workout= Label(width=20, text="How many pushups?")
label_workout.grid(column=0, row=0)

label_response= Label(width=20, text="")
label_response.grid(column=0, row=1)

btn_send = Button(width=10, text="Send", command=send_data)
btn_send.grid(column=2, row=0)


root.mainloop()