# 5. Exception Handling

# Write a Python program to handle multiple exceptions (e.g., file not found, division by zero).

try:
    file = open("data.txt", "r")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result =", result)

    content = file.read()
    print("File Content:", content)

    file.close()

except FileNotFoundError:
    print("Error: File not found.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid integers.")

except Exception as e:
    print("Some other error occurred:", e)

finally:
    print("Program ended.")