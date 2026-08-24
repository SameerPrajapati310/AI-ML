# In this one class is just aware of another calls just for interation but does not ows it 

class Student:
    def __init__ (self,name):
        self.name = name

class Teacher:
    def __init__ (self,name):
        self.name = name
    def teach(self,student):
        print(f"{self.name} teaches {student.name}")

teacher = Teacher("Bob")

student = Student("Alex")
print(teacher.teach(student))