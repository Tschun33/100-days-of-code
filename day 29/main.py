from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    new_password = password_symbols+password_letter+password_numbers

    # for char in range(1, nr_symbols+1):
    #     new_password.append(random.choice(symbols))
    #
    # for char in range(1, nr_letters+1):
    #     new_password.append(random.choice(letters))
    #
    # for char in range(1, nr_numbers):
    #     new_password.append(random.choice(numbers))

    random.shuffle(new_password)
    password = ''.join(new_password)
    input_password.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search_login():
    website = input_website.get()
    with open("data.json", "r") as data_file:
        data_logins = json.load(data_file)
        try:
            website_to_display = data_logins[website]
            email = website_to_display["email"]
            password = website_to_display["password"]
        except KeyError:
            messagebox.showinfo(title="No Entry Found", message="No Entry Found")
        else:
            messagebox.showinfo(title="Field Empty", message=f"Email: {email}\n Password: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    print("clicked")
    website = input_website.get()
    username = input_username.get()
    password = input_password.get()
    new_data = {
        website: {
            "email": username,
            "password": password
        }
    }
    print(website)
    if website == "" or password == "":
        messagebox.showinfo(title="Field Empty", message="At least one field is empty")
    else:
        if messagebox.askokcancel(title=website, message=f"Email: {username}\n Password: {password}\n Is it ok to save?"):
            with open("data.json", "r") as password_file:
                # read old data as data
                try:
                    data = json.load(password_file)
                    # update (append) the new data to the existing data
                    data.update(new_data)
                except:
                    data = new_data
            with open("data.json", "w") as password_file:
                # save the whole data (new and old)
                json.dump(data, password_file, indent=4)
                input_website.delete(0, END)
                input_password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

logo_png = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_png)
canvas.grid(column=1, row=0)

label_website = Label()
label_website.config(text="Website:")
label_website.grid(column=0, row=1)

label_username = Label()
label_username.config(text="Email/Username:")
label_username.grid(column=0, row=2)

label_password = Label()
label_password.config(text="Password:")
label_password.grid(column=0, row=3)

# Entry
input_website = Entry(width=35)
input_website.grid(column=1, row=1, columnspan=2)
input_website.focus()

input_username = Entry(width=35)
input_username.grid(column=1, row=2, columnspan=2)
input_username.insert(0, "StefanBaltschun@web.de")

input_password = Entry(width=21)
input_password.grid(column=1, row=3)

# Button
btn_add = Button(text="Add", width=30, command=save_data)
btn_add.grid(column=1, row=4, columnspan=2)

btn_generate = Button(text="Generate Password", command=generate_password)
btn_generate.grid(column=2, row=3)

btn_search = Button(text="Search", command=search_login)
btn_search.grid(column=2, row=1)

window.mainloop()
