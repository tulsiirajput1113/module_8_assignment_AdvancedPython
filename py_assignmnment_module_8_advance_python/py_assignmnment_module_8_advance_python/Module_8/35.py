# 10. Search and Match Functions

# Write a Python program to match a word in a string using re.match().

import re

text = "Python is easy"

# Match word at beginning
result = re.match("Python", text)

if result:
    print("Word matched")
else:
    print("Word not matched")