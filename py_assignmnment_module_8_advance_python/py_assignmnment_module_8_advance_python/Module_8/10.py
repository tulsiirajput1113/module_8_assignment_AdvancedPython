# 4. Reading and Writing Files

# Write a Python program to read a file and print the data on the console

file = open("message.txt", "r")

data = file.read()

print(data)

file.close()