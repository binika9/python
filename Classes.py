class Person:
    age = 32
    print(age)
p1 = Person()#OBJECT
print(p1.age)
class Student():
    Grade = 'A'
    print(Grade)
Student1 = Student()
Student2 = Student()
print(Student1.Grade)
print(Student2.Grade)

class Employees():
    def __init__(self,name,age):
        self.name = name
        self.age = age
Employee1 = Employees(name='John',age=88)
Employee2 = Employees(name='Kamau',age=90)
print(Employee1)
print(Employee2)


class University():
    def __init__(self,name,location):
        self.name = name
        self.location = location
University1 = University(name='Kenyatta',location='San Francisco')
University2 = University(name='Nairobi',location='Kenya')
print(University1)
print(University2)

class Student():
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
    def display(self):
        print('My name is',self.name+ 'and' 'I am',self.age,'years with marks',self.marks)
s1 = Student(name='John',age=88,marks=78)
s2 = Student(name='Kamau',age=77, marks=80)
print(s1.display())

# create a class parent with properties
# first name,last name,age,gender.
# then use it as a blueprint for 4 more
# parents

class Parents():
    def __init__(self,first_name,last_name,age,gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

        def display1(self):
            print('My name is',self.first_name, last_name,'and I am a',self.gender,'with ',self.age,'years')
p1 = Parents(first_name='Albert',last_name='Mwamboko',age=22,gender='Male')
p2 = Parents(first_name='Rose',last_name='Kaari',age=28,gender='Female')
p3 = Parents(first_name='John',last_name='Kinyua',age=38,gender='Male')
p4 = Parents(first_name='Moana',last_name='Yuri',age=77,gender='Female')
print(p1.display1())


