# ========================== LOOPS & CONDITIONALS IN PYTHON ==========================

# ========================== CONDITIONAL STATEMENTS (if, elif, else) ==========================

num = int(input("Enter a number: "))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")

# Using if with multiple conditions (and, or, not)
age = int(input("Enter your age: "))

if age >= 18 and age <= 60:
    print("You are eligible to work.")
elif age < 18:
    print("You are too young to work.")
else:
    print("You may be retired.")

# Nested if
x = int(input("Enter a number: "))

if x > 0:
    if x % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")
else:
    print("Non-positive Number")

# Ternary Operator (Shorthand if-else)
num = int(input("Enter a number: "))
result = "Even" if num % 2 == 0 else "Odd"
print("Number is:", result)

# ========================== FOR LOOP ==========================

print("For loop example:")
for i in range(1, 6):  # Loops from 1 to 5
    print(i)

# Iterating over a list
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# Iterating over a string
for char in "Python":
    print(char)

# Using range(start, stop, step)
for num in range(10, 0, -2):  # Counting down by 2
    print(num)

# Iterating with enumerate()
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(f"Index {index}: {name}")

# Iterating multiple lists using zip()
subjects = ["Math", "Science", "English"]
marks = [90, 85, 88]

for subject, mark in zip(subjects, marks):
    print(f"{subject}: {mark}")

# ========================== WHILE LOOP ==========================

print("While loop example:")
count = 5
while count > 0:
    print(count)
    count -= 1

# Taking user input in while loop
while True:
    word = input("Enter a word (or type 'exit' to stop): ")
    if word.lower() == "exit":
        break
    print("You entered:", word)

# ========================== LOOP CONTROL STATEMENTS ==========================

# Break: Stops the loop
print("Using break:")
for num in range(1, 10):
    if num == 5:
        print("Stopping at 5")
        break
    print(num)

# Continue: Skips the current iteration
print("Using continue:")
for num in range(1, 10):
    if num == 5:
        print("Skipping 5")
        continue
    print(num)

# Pass: Placeholder (does nothing)
print("Using pass:")
for num in range(1, 10):
    if num == 5:
        pass  # Placeholder for future code
    print(num)

# ========================== NESTED LOOPS ==========================

print("Nested loop example:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})", end=" ")
    print()

# Printing a pattern using nested loops
print("Pattern Printing:")
for i in range(1, 6):
    print("*" * i)

# ========================== LIST COMPREHENSIONS ==========================

# List of squares using list comprehension
squares = [x ** 2 for x in range(1, 6)]
print("Squares:", squares)

# List of even numbers using list comprehension
evens = [x for x in range(1, 11) if x % 2 == 0]
print("Even numbers:", evens)

# Nested list comprehension (Multiplication Table)
multiplication_table = [[x * y for y in range(1, 6)] for x in range(1, 6)]
print("Multiplication Table:", multiplication_table)

# ========================== DICTIONARY COMPREHENSION ==========================

# Creating a dictionary with squares
square_dict = {x: x**2 for x in range(1, 6)}
print("Square Dictionary:", square_dict)

# ========================== WHILE-ELSE & FOR-ELSE ==========================

# Using while-else
count = 3
while count > 0:
    print("Counting down:", count)
    count -= 1
else:
    print("Loop ended without break.")

# Using for-else
for num in range(1, 5):
    print(num)
else:
    print("Loop finished normally.")

# ========================== END ==========================
