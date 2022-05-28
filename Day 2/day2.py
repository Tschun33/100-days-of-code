print("Welcome to the tip calculator!")
bill = int(input("How much was the bill?\n"))
people = int(input("How many people split the bill?\n"))
tip = int(input("What percentage tip would you like to give?\n"))
tip = tip / 100
total = (bill * (1+tip)) / people
total = round(total, 2)
print(f"Each person should pay: $ {total}")

