# 4. Reading and Writing Files

# Write a Python program to check the current position of the file cursor using tell().

file = open("sample.txt", "r")

position = file.tell()

print("Current file cursor position is:", position)

file.close()