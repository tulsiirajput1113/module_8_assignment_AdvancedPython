# 7. Inheritance

# Write a Python program to show single inheritance


class Animal:
    
    def sound(self):
        print("Animal makes sound")



class Dog(Animal):
    
    def bark(self):
        print("Dog barks")



d1 = Dog()


d1.sound()
d1.bark()