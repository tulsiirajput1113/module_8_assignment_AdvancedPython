# 5. Exception Handling

# Write a Python program to print custom exceptions.

class AgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise AgeError("You are not eligible.")

    print("You are eligible.")

except AgeError as e:
    print("Custom Exception:", e)

except ValueError:
    print("Please enter a valid number.")