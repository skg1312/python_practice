# ========================== STRING CREATION ==========================  
s1 = "Hello, Python!"
s2 = 'Single quotes also work'
s3 = """Triple quotes allow multi-line strings"""  

print(s1)
print(s2)
print(s3)

# ========================== STRING FUNCTIONS ==========================  
print(len(s1))  # Get length of string
print(type(s1))  # Get type of object
print(str(123))  # Convert number to string

# ========================== STRING METHODS ==========================  

# ---------- Case Changing Methods ----------  
print(s1.lower())  # Convert to lowercase
print(s1.upper())  # Convert to uppercase
print(s1.title())  # Convert to title case
print(s1.capitalize())  # Capitalize first letter
print(s1.swapcase())  # Swap uppercase & lowercase  

# ---------- Searching and Finding ----------  
print(s1.count("o"))  # Count occurrences of 'o'
print(s1.find("Python"))  # Find index of first occurrence
print(s1.index("P"))  # Find index of character (raises error if not found)
print(s1.rfind("o"))  # Find last occurrence index
print(s1.rindex("o"))  # Find last occurrence index (raises error if not found)  

# ---------- Checking String Properties ----------  
print(s1.startswith("Hello"))  # Check if string starts with substring
print(s1.endswith("!"))  # Check if string ends with substring
print(s1.isalpha())  # Check if all characters are letters
print(s1.isdigit())  # Check if all characters are digits
print(s1.isalnum())  # Check if all characters are alphanumeric
print(s1.isspace())  # Check if string contains only spaces
print(s1.islower())  # Check if all letters are lowercase
print(s1.isupper())  # Check if all letters are uppercase
print(s1.istitle())  # Check if string is title case  

# ---------- String Modification Methods ----------  
print(s1.strip())  # Remove leading & trailing spaces
print(s1.lstrip())  # Remove leading spaces
print(s1.rstrip())  # Remove trailing spaces
print(s1.replace("Python", "Java"))  # Replace substring

# ---------- Splitting and Joining ----------  
print(s1.split())  # Split string by spaces
print(s1.split(","))  # Split using comma as delimiter
print(s1.rsplit("o"))  # Split from the right side
print(s1.partition(","))  # Split into three parts (before, separator, after)
print(s1.rpartition("o"))  # Split from the right side into three parts
print("-".join(["Hello", "World"]))  # Join list elements into a string  

# ---------- String Alignment ----------  
print(s1.center(30, "*"))  # Center align with padding
print(s1.ljust(30, "-"))  # Left align with padding
print(s1.rjust(30, "-"))  # Right align with padding
print(s1.zfill(30))  # Pad with leading zeros  

# ---------- Encoding and Decoding ----------  
encoded_s1 = s1.encode("utf-8")  # Encode string to bytes
print(encoded_s1)
decoded_s1 = encoded_s1.decode("utf-8")  # Decode bytes to string
print(decoded_s1)

# ========================== STRING FORMATTING ==========================  

# ---------- Old Formatting ( % Operator ) ----------  
name = "Alice"
age = 25
print("My name is %s and I am %d years old." % (name, age))

# ---------- New Formatting ( format() method ) ----------  
print("My name is {} and I am {} years old.".format(name, age))
print("My name is {0} and I am {1} years old.".format(name, age))  # Positional arguments
print("My name is {name} and I am {age} years old.".format(name="Bob", age=30))  # Named placeholders  

# ---------- f-Strings (Python 3.6+) ----------  
print(f"My name is {name} and I am {age} years old.")  

# ========================== ESCAPE SEQUENCES ==========================  
print("Hello\nWorld")  # Newline
print("Hello\tWorld")  # Tab
print("Hello\\World")  # Backslash
print("Hello \"World\"")  # Double quote inside string
print('Hello \'World\'')  # Single quote inside string
print("Hello\bWorld")  # Backspace  

# ========================== STRING ITERATION ==========================  
for char in s1:
    print(char, end=" ")  # Iterate through each character
print()

# ========================== STRING COMPARISON ==========================  
print("apple" == "banana")  # Equality check
print("apple" != "banana")  # Inequality check
print("apple" < "banana")  # Lexicographic comparison
print("apple" > "banana")  # Lexicographic comparison  

# ========================== STRING CONCATENATION & REPETITION ==========================  
s4 = "Hello" + " " + "World"  # Concatenation
print(s4)

s5 = "Python " * 3  # Repeat string 3 times
print(s5)

# ========================== STRING SLICING ==========================  
s6 = "PythonProgramming"

print(s6[0])  # First character
print(s6[-1])  # Last character
print(s6[0:6])  # Substring (0 to 5)
print(s6[:6])  # First 6 characters
print(s6[6:])  # From index 6 to end
print(s6[::2])  # Step slicing (every 2nd character)
print(s6[::-1])  # Reverse the string  

# ========================== STRING METHODS THAT RETURN BOOLEAN VALUES ==========================  
print(s1.isidentifier())  # Check if valid identifier
print(s1.isprintable())  # Check if all characters are printable  

# ========================== STRING BYTE OPERATIONS ==========================  
byte_str = b"Hello"  # Byte string
print(byte_str)
print(byte_str.decode())  # Decode to string

# ========================== UNICODE & ASCII OPERATIONS ==========================  
print(ord("A"))  # Get ASCII value
print(chr(65))  # Get character from ASCII value  

# ========================== CHECKING CHARACTER EXISTENCE ==========================  
print("P" in s1)  # Check if character exists in string
print("Python" not in s1)  # Check if substring does not exist  

# ========================== USING MAP & FILTER WITH STRINGS ==========================  
s7 = "hello123"
print("".join(filter(str.isalpha, s7)))  # Remove digits from string
print("".join(map(str.upper, s7)))  # Convert all letters to uppercase  

