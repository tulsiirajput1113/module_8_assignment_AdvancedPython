# 7. Inheritance

# Write a Python program to demonstrate the use of super() in inheritance.

class Parent:
    
    def __init__(self):
        print("This is Parent class")


class Child(Parent):
    
    def __init__(self):
        
        # Call parent class constructor
        super().__init__()
        
        print("This is Child class")


# Create object
c1 = Child()