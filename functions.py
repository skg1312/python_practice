# ========================== FUNCTIONS IN PYTHON ==========================

# ========================== BASIC FUNCTION DEFINITION ==========================

def greet():
    """Simple function without parameters"""
    print("Hello, Welcome to Python Functions!")

greet()  # Calling the function

# ========================== FUNCTION WITH PARAMETERS ==========================

def greet_user(name):
    """Function with a parameter"""
    print(f"Hello, {name}!")

greet_user("Alice")

# ========================== FUNCTION WITH RETURN VALUE ==========================

def add(a, b):
    """Function that returns a value"""
    return a + b

result = add(5, 3)
print("Sum:", result)

# ========================== DEFAULT PARAMETERS ==========================

def power(base, exponent=2):
    """Function with default argument"""
    return base ** exponent

print("Power (default exponent 2):", power(5))   # 5^2
print("Power with custom exponent:", power(5, 3))  # 5^3

# ========================== VARIABLE-LENGTH ARGUMENTS (*args, **kwargs) ==========================

# *args (Accepts multiple positional arguments)
def sum_all(*numbers):
    """Function with variable-length arguments"""
    return sum(numbers)

print("Sum of numbers:", sum_all(1, 2, 3, 4, 5))

# **kwargs (Accepts multiple keyword arguments)
def user_info(**kwargs):
    """Function with variable keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

user_info(name="Alice", age=25, city="New York")

# ========================== LAMBDA FUNCTIONS ==========================

square = lambda x: x ** 2
print("Square using lambda:", square(4))

add_nums = lambda x, y: x + y
print("Addition using lambda:", add_nums(3, 7))

# Lambda inside a function
def multiplier(n):
    """Function that returns a lambda"""
    return lambda x: x * n

double = multiplier(2)
print("Double of 5:", double(5))

# ========================== RECURSION ==========================

def factorial(n):
    """Recursive function to calculate factorial"""
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

# ========================== HIGHER-ORDER FUNCTIONS ==========================

def apply_operation(x, y, func):
    """Function that takes another function as an argument"""
    return func(x, y)

print("Addition using higher-order function:", apply_operation(5, 3, lambda a, b: a + b))

# ========================== FUNCTION CLOSURE ==========================

def outer_function(text):
    """Closure example"""
    def inner_function():
        print(text)  # inner function captures 'text'
    return inner_function

closure_func = outer_function("Hello from closure!")
closure_func()  # Calls the inner function

# ========================== FUNCTION DECORATORS ==========================

def decorator(func):
    """A simple decorator"""
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def say_hello():
    print("Hello, world!")

say_hello()

# ========================== GENERATORS (USING YIELD) ==========================

def countdown(n):
    """Generator function"""
    while n > 0:
        yield n
        n -= 1

countdown_gen = countdown(5)
print("Countdown values:", list(countdown_gen))

# ========================== FUNCTION ANNOTATIONS ==========================

def multiply(a: int, b: int) -> int:
    """Function with type hints"""
    return a * b

print("Multiplication with type hints:", multiply(4, 3))

# ========================== BUILT-IN FUNCTIONS (map, filter, reduce) ==========================

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map() - Apply function to all elements
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared numbers using map():", squared_numbers)

# filter() - Filter elements based on condition
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using filter():", even_numbers)

# reduce() - Reduce elements to a single value
sum_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum using reduce():", sum_numbers)

# ========================== PARTIAL FUNCTIONS (functools.partial) ==========================

from functools import partial

def multiply(x, y):
    return x * y

double = partial(multiply, 2)  # Fixing one argument
print("Double of 6 using partial:", double(6))

# ========================== END ==========================
