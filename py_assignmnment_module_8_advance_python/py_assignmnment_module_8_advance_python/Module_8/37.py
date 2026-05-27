# 10. Search and Match Functions

# Write a Python program to match a word in a string using re.match().

import re

string = "Python is powerful"

# Match word from beginning
result = re.match("Python", string)

if result:
    print("Word matched")
else:
    print("Word not matched")