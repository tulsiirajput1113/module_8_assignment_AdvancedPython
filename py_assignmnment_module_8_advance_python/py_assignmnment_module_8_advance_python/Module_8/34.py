# 10. Search and Match Functions

# Write a Python program to search for a word in a string using re.search().

import re

text = "Python is easy to learn"

# Search word
result = re.search("easy", text)

if result:
    print("Word found")
else:
    print("Word not found")