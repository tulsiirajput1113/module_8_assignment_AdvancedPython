# 4. Reading and Writing Files

# Write a Python program to write multiple strings into a file.

file = open("notes.txt", "w")

file.write("Hello Python\n")
file.write("Welcome to File Handling\n")
file.write("This is a sample text file")

file.close()

print("Multiple strings written successfully.")