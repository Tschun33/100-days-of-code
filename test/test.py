import logging

my_list = [1, 3, 5, 7, 9]
my_iterator = iter(my_list)

print(my_iterator)
next(my_iterator)
print(next(my_iterator))
print(next(my_iterator))
next(my_iterator)
print(next(my_iterator))

try:
    value = int(input("Number:"))
    result = str(5 / value)
    print("5 divided by " + str(value) + " = " + result)
except ZeroDivisionError:
    print("You tried to divide by zero!")
print("End")

logging.basicConfig(filename="mylog.log", filemode="w", level=logging.DEBUG)

logging.debug("Debugging is the lowest level of severity")