calculating = True
still_calculating = "y"


def calc(number1, operator_calc, number2):
    if operator_calc == "+":
        return number1 + number2
    elif operator_calc == "-":
        return number1 - number2
    elif operator_calc == "/":
        return number1 / number2
    elif operator_calc == "*":
        return number1 * number2

    else:
        print("No valid Operator")


while calculating:
    num1 = int(input("What is your first number?"))
    operator = input("Chose an operator:")
    num2 = int(input("What is your second number"))
    result_calc = calc(num1, operator, num2)
    print(f"{num1} {operator} {num2} = {result_calc}")
    still_calculating = input("Continue calculating? Type 'y' or 'n'")
    while still_calculating == "y":
        operator_next = input("Next operator: ")
        num_next = int(input("Next number: "))
        result_next = calc(result_calc, operator_next, num_next)
        print(f"{result_calc} {operator_next} {num_next} = {result_next}")
        result_calc = result_next
        still_calculating = input("Continue calculating? Type 'y' or 'n'")
    if input("Next calculation? Type 'y' or 'n'") == "n":
        calculating = False
    else:
        calculating = True









