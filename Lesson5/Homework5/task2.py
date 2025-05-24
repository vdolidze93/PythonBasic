DECISION_CONTINUE = "y"


while DECISION_CONTINUE == "y":
    first_number = int(input("Please enter the first number: "))
    second_number = int(input("Please enter the second number: "))
    operation = input("Please enter the operation: ")

    match operation:
        case "+":
            result = first_number + second_number
            print(f"{first_number} + {second_number} = {result}")
        case "-":
            result = first_number - second_number
            print(f"{first_number} - {second_number} = {result}")
        case "*":
            result = first_number * second_number
            print(f"{first_number} * {second_number} = {result}")
        case "/":
            if second_number == 0:
                print("You cannot divide by zero")
            else:
                result = first_number / second_number
                print(f"{first_number} / {second_number} = {result}")
    DECISION_CONTINUE = input("Do you wish to do another operation y/n: ")
    while DECISION_CONTINUE != "y" and DECISION_CONTINUE != "n":
        DECISION_CONTINUE = input("Incorrect input. Do you wish to do another operation y/n: ")

