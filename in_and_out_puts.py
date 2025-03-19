# ========================== INPUT & OUTPUT IN PYTHON ==========================

# ========================== STANDARD OUTPUT ==========================

print("Hello, World!")
print("The sum of 5 and 3 is:", 5 + 3)
print("Hello", "Python", sep=", ")
print("Hello", end=" ")
print("World!")

# Formatted Output
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
print("My name is {} and I am {} years old.".format(name, age))
print("My name is %s and I am %d years old." % (name, age))

# Special Characters
print("Line1\nLine2")
print("Tab\tSpace")
print("Backslash \\")
print("Double quote \" and single quote '")

# Using `repr()`
print(repr("Hello\nWorld"))

# ========================== STANDARD INPUT ==========================

user_name = input("Enter your name: ")
print("Hello,", user_name)

user_age = int(input("Enter your age: "))
print("You are", user_age, "years old.")

user_salary = float(input("Enter your salary: "))
print("Your salary is:", user_salary)

x, y = input("Enter two numbers separated by space: ").split()
print("First number:", x, "Second number:", y)

x, y = map(int, input("Enter two numbers separated by space: ").split())
print("Sum:", x + y)

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("List of numbers:", numbers)

numbers = list(map(int, input("Enter numbers separated by commas: ").split(',')))
print("Numbers List:", numbers)

full_line = input("Enter a full sentence: ")
print("You entered:", full_line)

import sys
print("Enter multiple lines (Press Ctrl+D on Linux/macOS, Ctrl+Z on Windows to stop):")
multi_line_input = sys.stdin.read()
print("You entered:\n", multi_line_input)

first_five_chars = input("Enter a string: ")[:5]
print("First 5 characters:", first_five_chars)

while True:
    user_input = input("Enter something (type 'exit' to stop): ")
    if user_input.lower() == "exit":
        break
    print("You entered:", user_input)

# ========================== FILE HANDLING ==========================

with open("output.txt", "w") as file:
    file.write("Hello, File!\n")
    file.write("This is written to a file.\n")

with open("output.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)

lines = ["First Line\n", "Second Line\n", "Third Line\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)

with open("output.txt", "r") as file:
    for line in file:
        print("Read Line:", line.strip())

with open("output.txt", "a") as file:
    file.write("Appending a new line!\n")

# ========================== FORMATTED OUTPUT ==========================

import pprint
data = {"name": "Alice", "age": 25, "city": "New York"}
pprint.pprint(data)

import json
print(json.dumps(data, indent=4))

# ========================== PRINTING TO A FILE ==========================

with open("log.txt", "w") as file:
    print("Logging some output...", file=file)

# ========================== USING SYS MODULE FOR INPUT/OUTPUT ==========================

sys.stdout.write("This is stdout output\n")
sys.stderr.write("This is stderr error message\n")

# ========================== LOGGING OUTPUT ==========================

import logging

logging.basicConfig(filename="app.log", level=logging.INFO)
logging.info("This is an info log message")
logging.warning("This is a warning log message")
logging.error("This is an error log message")

console_logger = logging.getLogger()
console_logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_logger.addHandler(console_handler)
console_logger.debug("Debug message displayed in console")

# ========================== CUSTOM PRINT FUNCTION ==========================

def custom_print(*args, sep=" | ", end="\n", file=sys.stdout):
    file.write(sep.join(map(str, args)) + end)

custom_print("Apple", "Banana", "Cherry")
custom_print("One", "Two", "Three", sep=" - ")

# ========================== END ==========================
