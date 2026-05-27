# 7. Inheritance

#  Write Python programs to demonstrate different types of inheritance (single, multiple, multilevel, etc.)

# 1. Single Inheritance


class Parent:
    
    def show(self):
        print("This is Parent class")


class Child(Parent):
    
    def display(self):
        print("This is Child class")


c1 = Child()

c1.show()
c1.display()


# 2. Multiple Inheritance

'''
class Father:
    
    def money(self):
        print("Father has money")


class Mother:
    
    def care(self):
        print("Mother takes care")


class Child(Father, Mother):
    pass


c1 = Child()

c1.money()
c1.care()

'''

#3. Multilevel Inheritance 

'''
class Grandfather:
    
    def house(self):
        print("Grandfather has a house")


class Father(Grandfather):
    
    def car(self):
        print("Father has a car")


class Son(Father):
    
    def bike(self):
        print("Son has a bike")


s1 = Son()

s1.house()
s1.car()
s1.bike()
'''

# 4. Hierarchical Inheritance

'''
class Parent:
    
    def property(self):
        print("Parent property")


class Child1(Parent):
    pass


class Child2(Parent):
    pass


c1 = Child1()
c2 = Child2()

c1.property()
c2.property()

'''

# 5. Hybrid Inheritance

'''
class A:
    
    def showA(self):
        print("Class A")


class B(A):
    
    def showB(self):
        print("Class B")


class C(A):
    
    def showC(self):
        print("Class C")


class D(B, C):
    pass


d1 = D()

d1.showA()
d1.showB()
d1.showC()
'''