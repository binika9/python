class employees:

    def __init__(self,first_name,last_name,pay):#init constructor/method
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@gmail.com'
    def full_name(self):
        return '{} {}'.format(self.first_name,self.last_name)
    def apply_raise(self):
        self.pay = float(self.pay * 1.05)

emp1 = employees('felix','smith',123456)
emp2 = employees('george','Njihia',23000)
print(emp1.first_name)
print(emp2.first_name)
print(emp1.email)
print(emp2.email)
print(f'{emp1.first_name} {emp1.last_name}salary is {emp1.pay}')
print(f'{emp2.first_name} {emp2.last_name}salary is {emp2.pay}')
print(emp1.full_name())
print(emp2.full_name())
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

class employees:
    raise_amount = 1.5

    def __init__(self,first_name,last_name,pay):#init constructor/method
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@gmail.com'
    def full_name(self):
        return '{} {}'.format(self.first_name,self.last_name)
    def apply_raise(self):
        self.pay = float(self.pay * self.raise_amount)
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount
class developer(employees):#child class
    def __init__(self,first_name,last_name,pay,language):
        super().__init__(first_name,last_name,pay)#inheritance from parent class
        self.language = language

class watchman(employees):
    def __init__(self,first_name,last_name,pay,gender):
        super().__init__(first_name,last_name,pay)
        self.gender = gender

emp1 = employees('felix','smith',123456)
emp2 = employees('george','Njihia',23000)
print(emp1.first_name)
print(emp2.first_name)
print(emp1.email)
print(emp2.email)
print(f'{emp1.first_name} {emp1.last_name}salary is {emp1.pay}')
print(f'{emp2.first_name} {emp2.last_name}salary is {emp2.pay}')
print(emp1.full_name())
print(emp2.full_name())
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
employees.raise_amount=2.05
print(employees.raise_amount)
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
employees.set_raise_amount(1.23)
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
dev1 = developer('John','Kigotho',20000,'python')
dev2 = developer('Felix','Kegode',30000,'java')
print(dev1.language)
print(dev2.language)
wat1 = watchman('John','Kigotho',8000,'male')
print(wat1.gender)

#create a parent class colors then implement two child classes of that parent class

class colors:
    




