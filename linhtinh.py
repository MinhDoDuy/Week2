class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person('Minh', 25)
print(p1.name)
print(p1.age)
print("---------------------")

class Person:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

p2 = Person('Manh', 30, 'Hanoi', 'Vietnam')
print(p2.name)
print(p2.age)
print(p2.city)
print(p2.country)
print("---------------------")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
p3 = Person('Lan', 28)
p3.greet()
print("---------------------")

class Person:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

p1 = Person('Long')
p2 = Person('Hoa')

p1.print_name()
p2.print_name()
print("---------------------")

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car('Toyota', 'Corolla')
car2 = Car('Honda', 'Civic')
print(car1.brand, car1.model)
print(car2.brand, car2.model)

print("---------------------")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Lanh', 25)
print(p1.name,p1.age)

p1.age = 26
print(p1.name,p1.age)
print("---------------------")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Kinh', 29)
del p1.age
print(p1.name)
print("---------------------")

class Person:
    species = 'MinhDoo'

    def __init__(self, name):
        self.name = name

p1 = Person('Duc')
p2 = Person('Hieu')

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)
print("---------------------")

class Person:
    lastname = ' '
    def __init__(self, name):
        self.name = name
p1 = Person('Quang')
p2 = Person('Thao')
Person.lastname = 'Longggg'

print(p1.lastname)
print(p2.lastname)
print("---------------------")

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}.")

p1 = Person("Minh")
p1.greet()
print("---------------------")

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy birthday! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()
print("---------------------")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

p1 = Person("An", 22)
print(p1)
print("---------------------")

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student('Mike', 'Olsen', 2024)
x.welcome()
print("---------------------")