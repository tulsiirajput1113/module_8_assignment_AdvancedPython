# 8. Method Overloading and Overriding

# Write a Python program to show method overriding.


class Animal:
    
    def sound(self):
        print("Animal makes sound")


class Dog(Animal):
    
    # Overriding parent method
    def sound(self):
        print("Dog barks")



d1 = Dog()
d1.sound()