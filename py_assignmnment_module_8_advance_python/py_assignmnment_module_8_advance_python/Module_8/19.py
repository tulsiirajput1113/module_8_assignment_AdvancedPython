# 6. Class and Object (OOP Concepts)
# Write a Python program to create a class and access the properties of the class using an object.

# Create a class
class Car:
    
    # Constructor
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


# Create an object
c1 = Car("Toyota", "Fortuner")

# Access class properties using object
print("Car Brand:", c1.brand)
print("Car Model:", c1.model)