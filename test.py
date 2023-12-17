# Jon Whitmer

print("Simple Calculator")

def expression(initial, initialFilled):
    if initialFilled:
        operand1 = initial
        print("First Operand: " + str(operand1))
    else:
        operand1 = float(input("Enter the first operand: "))

    operator = input("Enter an operator: ")

    while operator not in "+-*/%^":
        print("Invalid Operator.  Try Again.")
        operator = input("Enter an operator: ")

    operand2 = float(input("Enter the second operand: "))

    print("Press Enter to Calculate: " + str(operand1) + " " + operator + " " + str(operand2))
    input()

    return calculate(operand1, operator, operand2)

def calculate(operand1, operator, operand2):
    match operator:
        case "+":
            return operand1 + operand2
        case "-":
            return operand1 - operand2
        case "*":
            return operand1 * operand2
        case "/":
            return operand1 / operand2
        case "%":
            return operand1 % operand2
        case "^":
            return operand1 ** operand2

option = 2

while option != 3:

    match option:
        case 1: 
            result = expression(result, True)
            print("Result: " + str(result))
        case 2: 
            result = expression(0, False)
            print("Result: " + str(result))

    print("1) Additional Operation {Last Value: " + str(result) + "}")
    print("2) Clear Calculator")
    print("3) Turn Off Calculator")

    option = int(input("Choose next step: "))

    while option not in (1, 2, 3):
        print("Invalid Option.  Try Again.")

        print("1) Additional Operation {Last Value: " + str(result) + "}")
        print("2) Clear Calculator")
        print("3) Turn Off Calculator")

        option = int(input("Choose next step: "))

    if option == 3:
        print("Shutting Down...")
        exit(0)