# 7. Inheritance

# Write a Python program to show multiple inheritance.

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