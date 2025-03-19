# ========================== EXCEPTION HANDLING IN PYTHON ==========================

# ========================== BASIC EXCEPTION HANDLING ==========================

try:
    x = 10 / 0  # Division by zero
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# ========================== MULTIPLE EXCEPTIONS ==========================

try:
    lst = [1, 2, 3]
    print(lst[5])  # Index out of range
except (IndexError, ZeroDivisionError) as e:
    print(f"Exception occurred: {e}")

# ========================== EXCEPTION HANDLING WITH ELSE ==========================

try:
    num = int(input("Enter an integer: "))  # User input
except ValueError:
    print("Invalid input! Please enter a valid integer.")
else:
    print("Valid input received:", num)

# ========================== FINALLY BLOCK ==========================

try:
    file = open("sample.txt", "w")
    file.write("Hello, Python!")
except IOError:
    print("File operation failed.")
finally:
    file.close()  # Ensures resource is closed
    print("File closed.")

# ========================== CUSTOM EXCEPTION ==========================

class CustomError(Exception):
    """Custom Exception Example"""
    pass

try:
    raise CustomError("This is a custom error message")
except CustomError as e:
    print(f"Custom Exception Caught: {e}")

# ========================== RAISING EXCEPTIONS ==========================

try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")
    print("Your age is:", age)
except ValueError as e:
    print(f"Invalid Input: {e}")

# ========================== USING TRACEBACK MODULE ==========================

import traceback

try:
    1 / 0  # Division by zero
except ZeroDivisionError as e:
    print("Exception occurred:")
    traceback.print_exc()  # Prints detailed traceback

# ========================== USING SYS.MODULE FOR EXCEPTION INFO ==========================

import sys

try:
    int("invalid")  # Raises ValueError
except ValueError:
    error_type, error_value, error_traceback = sys.exc_info()
    print(f"Exception Type: {error_type.__name__}")
    print(f"Exception Message: {error_value}")

# ========================== LOGGING EXCEPTIONS ==========================

import logging

logging.basicConfig(filename="error.log", level=logging.ERROR)

try:
    result = 10 / 0
except ZeroDivisionError as e:
    logging.error("Error occurred: %s", e)

# ========================== NESTED TRY-EXCEPT BLOCKS ==========================

try:
    try:
        num = int(input("Enter a number: "))
        print(10 / num)
    except ZeroDivisionError:
        print("Cannot divide by zero!")
except ValueError:
    print("Invalid number entered!")

# ========================== ASSERTIONS FOR ERROR CHECKING ==========================

try:
    x = int(input("Enter a positive number: "))
    assert x > 0, "Only positive numbers allowed!"
    print("Valid input:", x)
except AssertionError as e:
    print("AssertionError:", e)

# ========================== END ==========================
