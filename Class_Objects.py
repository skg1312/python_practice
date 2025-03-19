# ========================== CLASSES & OBJECTS IN PYTHON ==========================

# ========================== BASIC CLASS & OBJECT ==========================

class Person:
    """A simple class example"""
    def __init__(self, name, age):
        """Constructor to initialize attributes"""
        self.name = name
        self.age = age

    def greet(self):
        """Method to print a greeting"""
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an object
p1 = Person("Alice", 25)
p1.greet()

# ========================== CLASS ATTRIBUTES VS INSTANCE ATTRIBUTES ==========================

class Employee:
    company = "TechCorp"  # Class attribute (shared across all instances)

    def __init__(self, name, salary):
        self.name = name  # Instance attribute (unique to each object)
        self.salary = salary

# Creating objects
e1 = Employee("Bob", 50000)
e2 = Employee("Charlie", 60000)

print(e1.name, e1.salary, e1.company)
print(e2.name, e2.salary, e2.company)

# Modifying class attribute
Employee.company = "NewTechCorp"
print(e1.company)  # Affected for all instances

# ========================== CLASS METHOD & STATIC METHOD ==========================

class MathOperations:
    """Class demonstrating class and static methods"""
    
    @classmethod
    def class_method_example(cls):
        print("This is a class method. Can access class attributes.")

    @staticmethod
    def static_method_example():
        print("This is a static method. No access to class or instance attributes.")

MathOperations.class_method_example()
MathOperations.static_method_example()

# ========================== INHERITANCE ==========================

class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        return "Bark"

d = Dog()
print("Dog says:", d.speak())

# ========================== METHOD OVERRIDING ==========================

class Parent:
    def show(self):
        print("Parent class method")

class Child(Parent):
    def show(self):
        print("Child class method (overridden)")

c = Child()
c.show()  # Calls the overridden method

# ========================== MULTIPLE INHERITANCE ==========================

class A:
    def method_a(self):
        return "Method from class A"

class B:
    def method_b(self):
        return "Method from class B"

class C(A, B):  # Multiple Inheritance
    def method_c(self):
        return "Method from class C"

obj = C()
print(obj.method_a(), obj.method_b(), obj.method_c())

# ========================== ENCAPSULATION (PRIVATE & PROTECTED MEMBERS) ==========================

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute (cannot be accessed directly)

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print("Balance:", account.get_balance())

# print(account.__balance)  # This would raise an AttributeError (private variable)

# ========================== POLYMORPHISM ==========================

class Cat:
    def speak(self):
        return "Meow"

animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())  # Polymorphism: different implementations of `speak()`

# ========================== ABSTRACT CLASSES & INTERFACES ==========================

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car engine started.")

car = Car()
car.start()

# ========================== OPERATOR OVERLOADING ==========================

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Overloading + operator"""
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2  # Uses __add__
print(f"Point coordinates: ({p3.x}, {p3.y})")

# ========================== DESTRUCTOR METHOD ==========================

class Sample:
    def __init__(self, name):
        self.name = name
        print(f"Object {self.name} created.")

    def __del__(self):
        print(f"Object {self.name} destroyed.")

obj = Sample("TestObj")
del obj  # Manually invoking the destructor

# ========================== PROPERTY DECORATOR (GETTERS & SETTERS) ==========================

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self._price = value

product = Product(100)
print("Product price:", product.price)
product.price = 150
print("Updated price:", product.price)

# ========================== METACLASSES (ADVANCED TOPIC) ==========================

class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)

class CustomClass(metaclass=Meta):
    pass

# ========================== END ==========================
