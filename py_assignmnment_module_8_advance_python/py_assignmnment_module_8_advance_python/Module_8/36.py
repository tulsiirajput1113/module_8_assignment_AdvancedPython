# 10. Search and Match Functions

# Write a Python program to search for a word in a string using re.search()

import re

string = "Python programming is easy"

# Search word in string
result = re.search("programming", string)

if result:
    print("Word found")
else:
    print("Word not found")