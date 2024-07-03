while True:
    num1 = float(input('\nenter num1: '))
    num2 = float(input('enter num2: '))
    operator = input("choose operator + - * /: ")

    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2)
    else:
        print(f"operator '{operator}' not supported")