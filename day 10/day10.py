calculating = True


def calc(number1, operator_calc, number2):
    if operator_calc == "+":
        result = number1 + number2
        print(f"{number1} {operator_calc} {number2} = {result}")
    elif operator_calc == "-":
        result = number1 - number2
        print(f"{number1} {operator_calc} {number2} = {result}")
    elif operator_calc == "/":
        result = number1 / number2
        print(f"{number1} {operator_calc} {number2} = {result}")
    elif operator_calc == "*":
        result = number1 * number2
        print(f"{number1} {operator_calc} {number2} = {result}")
    else:
        print("No valid Operator")


while calculating:
    num1 = int(input("What is your first number?"))
    operator = input("Chose an operator:")
    num2 = int(input("What is your second number"))
    calc(num1, operator, num2)




