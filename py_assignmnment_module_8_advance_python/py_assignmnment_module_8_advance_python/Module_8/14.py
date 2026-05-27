# 5. Exception Handling

# Write a Python program to handle exceptions in a calculator.

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Result =", num1 + num2)

    elif choice == 2:
        print("Result =", num1 - num2)

    elif choice == 3:
        print("Result =", num1 * num2)

    elif choice == 4:
        print("Result =", num1 / num2)

    else:
        print("Invalid choice")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter valid numbers.")

except Exception as e:
    print("Error:", e)