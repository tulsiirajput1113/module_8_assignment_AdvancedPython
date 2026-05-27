# 8. Method Overloading and Overriding

# Write Python programs to demonstrate method overloading and method overriding.

# 1. Method Overloading

class Addition:
    
    def add(self, a, b, c=0):
        print("Addition:", a + b + c)


a1 = Addition()

a1.add(10, 20)
a1.add(10, 20, 30)



# 2. Method Overriding

class Parent:
    
    def show(self):
        print("This is Parent class")

class Child(Parent):
    
    def show(self):
        print("This is Child class")


c1 = Child()

c1.show()