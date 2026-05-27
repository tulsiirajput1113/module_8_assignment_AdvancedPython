# 7. Inheritance

# Write a Python program to show hybrid inheritance.

# Parent class
class A:
    
    def showA(self):
        print("This is class A")


# Child class of A
class B(A):
    
    def showB(self):
        print("This is class B")


# Another child class of A
class C(A):
    
    def showC(self):
        print("This is class C")


# Child class of B and C
class D(B, C):
    
    def showD(self):
        print("This is class D")


# Create object
d1 = D()

# Access all methods
d1.showA()
d1.showB()
d1.showC()
d1.showD()