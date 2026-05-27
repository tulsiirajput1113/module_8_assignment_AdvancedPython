# 8. Method Overloading and Overriding

# Write a Python program to show method overloading.

class Message:
    
    def display(self, name=None):
        
        # Without argument
        if name == None:
            print("Hello User")
        
        # With argument
        else:
            print("Hello", name)


m1 = Message()

m1.display()
m1.display("Jinal")