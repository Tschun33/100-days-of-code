import tkinter

window = tkinter.Tk()
window.title("New Tkinter Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text="Label", font=("Arial", 24, "bold"))
my_label.grid(column=1, row=1)

my_label["text"] = "New Text"
my_label.config(text="New Text")


# Button
def button_clicked():
    new_text = input.get()
    my_label["text"] = new_text


button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=2)

button_2 = tkinter.Button(text="Click Me", command=button_clicked)
button_2.grid(column=3, row=1)
# Entry
input = tkinter.Entry(widt=10)
input.grid(column=4, row=3)





window.mainloop()