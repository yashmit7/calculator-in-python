num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Select one: add, subtract, multiply, divide, remainder: ").lower()

if operation == "add":
    print("Result:", num1 + num2)
elif operation == "subtract":
    print("Result:", num1 - num2)
elif operation == "multiply":
    print("Result:", num1 * num2)
elif operation == "divide":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero")
elif operation == "remainder":
    if num2 != 0:
        print("Result:", num1 % num2)
    else:
        print("Cannot find remainder with zero")
else:
    print("Invalid operation")


























 
  

















