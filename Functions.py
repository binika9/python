print('this')
print('this')

def my_function():
    text = 'this'
    print(text)
    print(text)
    print(text)
my_function()

def number_one():
    number = input('Enter your name')
    print(number)
number_one()

def number_two():#argument
    number = input('Enter your weight')#variable
    print(number)
number_two()

def number_three(number):
    print(number)
number_three(5)

def name(firstname):
    print(firstname)
name('gg')
name('ann')

# def student_name(firstname, lastname):
#     print(firstname + ' ' + lastname)
# student_name(firstname:'Francis', lastname:'Pope')

# def mountain(name,height,location)
#     print(location+''+name+''height) error find

def salutation(name):
    print(name + 'Goodmorning')
salutation('George')

def salutation1(firstname,lastname):
    print(firstname + lastname + 'Goodmorning')
salutation1(firstname='George',lastname='Njihia')
salutation1(firstname='Alex',lastname='Mwata')

# def school_age(firstname,age):
#     if age<10:
#         print(firstname + 'you are young')
#     elif age>10:
#         print(firstname + 'you are middle aged')
#     else:
#         print(firstname + 'you are older')
# school_age(firstname:'George', age:9)
# school_age(firstname:'George', age:9)
# school_age(firstname:'George', age:9)

def add_age(age):
    new_age = age + 10
    return new_age
future_age = add_age(20)
print(future_age)
#or print(add_age(20))



# def performance(english,math):
#     total = english + math
#     return total
# print(performance(english=21,math=45)
#
# def performance1(*marks):#asterix use?
#     total = sum(marks)
#     return total
# print(performance1(*marks 45,66,78))
# print(performance1(*marks 34,14,90))
# print(performance1(*marks 75,25,90))




def country(nchi = 'Kenya')
    return nchi
print(country('Norway'))
print(country('China'))
print(country('Japan'))
print(country())


