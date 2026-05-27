# 5. Exception Handling

# Write a Python program to handle file exceptions and use the finally block for closing the file.

try:
    file = open("sample.txt", "r")

    content = file.read()

    print(content)

except FileNotFoundError:
    print("Error: File does not exist.")

except Exception as e:
    print("Error:", e)

finally:
    try:
        file.close()
        print("File closed successfully.")
    except:
        print("File was not opened.")