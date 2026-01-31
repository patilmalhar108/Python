class Student:
    grade = 8
    name = 'John'
def intro(self):
    print("Hi, I am a student")
def detail(self):
    print("My name is", self.name)
    print("My grade is", self.grade)
ob = Student()
#ob.intro()
ob.detail()