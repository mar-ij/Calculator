while True:
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))

    operation = input("Choose your calculating operation (/, *, +, -, **, //, %) or type 'exit' to quit: ")

    if operation.lower() == "exit":
        print("Calculator exiting. Goodbye!")
        break  # لوپ ختم کردے گا

    if operation == "/":
        print(a / b if b != 0 else "Error: Division by zero is not allowed.")
    elif operation == "*":
        print(a * b)
    elif operation == "+":
        print(a + b)
    elif operation == "-":
        print(a - b)
    elif operation == "**":
        print(a ** b)
    elif operation == "//":
        print(a // b if b != 0 else "Error: Division by zero is not allowed.")
    elif operation == "%":
        print(a % b if b != 0 else "Error: Modulo by zero is not allowed.")
    else:
        print("Invalid input. Please choose a valid operation.")


