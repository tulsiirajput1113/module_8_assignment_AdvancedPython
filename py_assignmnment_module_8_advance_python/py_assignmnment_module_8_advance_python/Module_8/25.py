# 7. Inheritance

# Write a Python program to show hierarchical inheritance


class Parent:
    
    def property(self):
        print("Parent has property")


class Child1(Parent):
    
    def bike(self):
        print("Child1 has a bike")


class Child2(Parent):
    
    def car(self):
        print("Child2 has a car")


# Create objects
c1 = Child1()
c2 = Child2()

# Access methods
c1.property()
c1.bike()

c2.property()
c2.car()