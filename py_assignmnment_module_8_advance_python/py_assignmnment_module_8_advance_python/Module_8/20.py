# 6. Class and Object (OOP Concepts)

#  Write a Python program to demonstrate the use of local and global variables in a class.

# Global variable
college = "LJ University"

class Student:
    
    def show(self):
        
        # Local variable
        name = "tulsi"
        
        print("Student Name:", name)
        print("College Name:", college)



s1 = Student()
s1.show()
