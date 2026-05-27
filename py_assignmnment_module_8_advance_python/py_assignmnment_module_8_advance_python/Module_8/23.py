# 7. Inheritance

# Write a Python program to show multilevel inheritance.


class Grandparent:
    
    def house(self):
        print("Grandparent has a house")


class Parent(Grandparent):
    
    def car(self):
        print("Parent has a car")


class Child(Parent):
    
    def bike(self):
        print("Child has a bike")

c1 = Child()

c1.house()
c1.car()
c1.bike()