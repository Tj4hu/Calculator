#Day 6
while True:  # Infinite loop to keep asking for operations
    operation = input("Enter operation (e.g., +, -, *, /): ")

    if operation == "+":
        def addition():
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            result = num1 + num2
            print(f"The result is: {result}")
        addition()

    elif operation == "-":
        def subtraction():
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            result = num1 - num2
            print(f"The result is: {result}")
        subtraction()

    elif operation == "*":
        def multiplication():
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            result = num1 * num2
            print(f"The result is: {result}")
        multiplication()

    elif operation == "/":
        def division():
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            if num2 == 0:
                print("Division by zero is not allowed!")
            else:
                result = num1 / num2
                print(f"The result is: {result}")
        division()

    else:
        print("Unknown operation! Please enter +, -, * or /.")

    # Ask if the user wants to calculate again
    again = input("Do you want to calculate again? (Y/N): ").lower()
    if again != "y":
        print("Thank you for using the calculator!")
        break