# 4. Reading and Writing Files

# Write a Python program to create a file and print the string into the file.

file = open("message.txt", "w")

file.write("Python is easy to learn.")

file.close()

print("String written into the file successfully.")