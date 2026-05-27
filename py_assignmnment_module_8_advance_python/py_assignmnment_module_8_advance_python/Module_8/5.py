# 3. Opening and Closing Files

# Write a Python program to open a file in write mode, write some text, and then close it.

file = open("sample.txt", "w")

file.write("Hello, this is a text file.")

file.close()

print("Data written successfully.")