# 6. Class and Object (OOP Concepts)
# Write a Python program to create a class and access its properties using an object.

class Student:
    
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Create an object
s1 = Student("Jinal", 21)

# Access properties using object
print("Student Name:", s1.name)
print("Student Age:", s1.age)