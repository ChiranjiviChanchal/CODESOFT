def calculator():
    # Prompt the user to input two numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    
    # Prompt the user to input the operation choice
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the calculation and display the result
    if operation == '+':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please select a valid operation.")

# Call the calculator function
calculator()

