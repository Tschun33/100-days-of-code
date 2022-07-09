import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=150)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label()
my_label.grid(column=1, row=2)
my_label.config(text="0")

label_km = tkinter.Label()
label_km.grid(column=2, row=2)
label_km.config(text="Km")

label_miles = tkinter.Label()
label_miles.grid(column=2, row=1)
label_miles.config(text="Miles")


# Button
def button_clicked():
    miles = int(input.get())
    km = round(miles * 1.60934, 2)
    my_label["text"] = f"{km}"


button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=3)

# Entry
input = tkinter.Entry(widt=10)
input.grid(column=1, row=1)





window.mainloop()