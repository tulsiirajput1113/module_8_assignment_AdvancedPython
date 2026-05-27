# 4. Reading and Writing Files

# Write a Python program to read the contents of a file and print them on the console.

file = open("data.txt", "r")

content = file.read()

print(content)

file.close()