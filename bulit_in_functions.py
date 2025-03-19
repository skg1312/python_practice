# ========================== BUILT-IN FUNCTIONS ==========================

# Numeric Conversions
print(abs(-10))  # Returns the absolute value of a number
print(bin(10))  # Convert to binary
print(oct(10))  # Convert to octal
print(hex(10))  # Convert to hexadecimal

# Character and ASCII Functions
print(ord('A'))  # Get ASCII value of character
print(chr(65))  # Get character from ASCII value

# Boolean Functions
print(bool(0))  # Convert to boolean
print(any([False, 0, "Python"]))  # Check if any element is True
print(all([True, 1, "Python"]))  # Check if all elements are True

# Debugging and Code Execution
breakpoint()  # Enters the debugger at this location
code = "print('Hello from eval!')"
exec(code)  # Executes a string as Python code
print(eval("5 + 10"))  # Evaluates an expression from a string

# Byte and Memory Operations
print(bytearray("hello", "utf-8"))  # Returns a mutable sequence of bytes
print(bytes("hello", "utf-8"))  # Returns an immutable sequence of bytes
print(memoryview(b"hello"))  # Creates a memory view object

# Object Type and Attributes
class Example:
    x = 10

e = Example()
print(hasattr(e, 'x'))  # Check if object has an attribute
setattr(e, 'y', 20)  # Set an attribute
print(getattr(e, 'y'))  # Retrieve an attribute
delattr(e, 'y')  # Delete an attribute

# Type Checking and Conversion
print(type(10))  # Get type of variable
print(isinstance(10, int))  # Check if object is an instance of a class
print(issubclass(Example, object))  # Check if class is a subclass of another

# Sequence Operations
print(len([1, 2, 3]))  # Returns the length of an object
print(list(range(1, 10, 2)))  # Generate list using range
print(sorted([3, 1, 4, 2]))  # Returns a sorted list
print(reversed([1, 2, 3]))  # Returns a reversed iterator
print(slice(1, 5, 2))  # Create a slice object

# Iteration Functions
iterable = iter([1, 2, 3])
print(next(iterable))  # Retrieve next item from iterator
print(list(enumerate(["apple", "banana", "cherry"])))  # Create enumeration object
print(list(map(str.upper, ["hello", "world"])))  # Apply function to all elements
print(list(filter(lambda x: x > 2, [1, 2, 3, 4])))  # Filter elements

# Mathematical Functions
print(pow(2, 3))  # Compute exponentiation (2^3)
print(divmod(10, 3))  # Get quotient and remainder
print(sum([1, 2, 3, 4]))  # Sum of list elements
print(min(3, 1, 4, 2))  # Get minimum value
print(max(3, 1, 4, 2))  # Get maximum value
print(round(3.14159, 2))  # Round number to 2 decimal places

# String and Formatting Functions
print(format(1000, ","))  # Format a number with a thousands separator
print(repr("Hello"))  # Get string representation
print(str(123))  # Convert to string

# File Handling (Commented Out)
# with open("test.txt", "w") as f:
#     f.write("Hello, File!")

# Input and Output
# user_input = input("Enter something: ")  # Reads user input
print(print("Hello, world!"))  # Outputs values to the console

# Global and Local Variables
print(globals())  # Returns the global symbol table
print(locals())  # Returns the local symbol table

# Help and Documentation
print(dir(str))  # List attributes and methods of an object
# print(help(int))  # Show documentation (Uncomment to use)

# Exception Handling
try:
    eval("5 + ")  # Evaluate invalid expression
except SyntaxError as e:
    print("Syntax Error:", e)

# Object and Class Functions
class MyClass:
    def method(self):
        return "Hello!"

obj = MyClass()
print(isinstance(obj, MyClass))  # Check if object is instance of class
print(issubclass(MyClass, object))  # Check if class is subclass of another

# Zip Function
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
print(list(zip(names, ages)))  # Combines lists

# Built-in Exception Classes
try:
    raise KeyboardInterrupt()
except KeyboardInterrupt:
    print("KeyboardInterrupt exception caught!")

try:
    raise SystemExit()
except SystemExit:
    print("SystemExit exception caught!")

# ========================== END ==========================
