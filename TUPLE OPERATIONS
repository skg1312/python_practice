# ========================== TUPLE CREATION ==========================  
tuple1 = (1, 2, 3, 4, 5)  # Tuple of integers
tuple2 = ("apple", "banana", "cherry")  # Tuple of strings
tuple3 = (1, "hello", 3.14, True)  # Mixed data types
tuple4 = tuple([10, 20, 30])  # Convert list to tuple
tuple5 = (50,)  # Single-element tuple (comma needed!)

print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)
print(tuple5)

# ========================== ACCESSING ELEMENTS ==========================  
print(tuple1[0])  # First element
print(tuple1[-1])  # Last element
print(tuple1[1:4])  # Slicing (index 1 to 3)
print(tuple1[:3])  # First 3 elements
print(tuple1[2:])  # From index 2 to end
print(tuple1[::-1])  # Reverse tuple

# ========================== TUPLE ITERATION ==========================  
for item in tuple2:
    print(item, end=" ")  # Iterate through elements
print()

# ========================== TUPLE METHODS ==========================  

# ---------- Counting & Searching ----------  
tuple6 = (1, 2, 3, 3, 4, 5, 3)
print(tuple6.count(3))  # Count occurrences of 3
print(tuple6.index(3))  # Find index of first occurrence of 3

# ========================== TUPLE OPERATIONS ==========================  
tupleA = (1, 2, 3)
tupleB = (4, 5, 6)

print(tupleA + tupleB)  # Concatenation
print(tupleA * 3)  # Repeat tuple 3 times

# ========================== CHECKING ELEMENT EXISTENCE ==========================  
print(3 in tuple1)  # Check if 3 is in tuple
print(100 not in tuple1)  # Check if 100 is not in tuple

# ========================== BUILT-IN TUPLE FUNCTIONS ==========================  
print(len(tuple1))  # Get length of tuple
print(max(tuple1))  # Get max value (for numeric tuples)
print(min(tuple1))  # Get min value
print(sum(tuple1))  # Get sum of elements (for numeric tuples)

# ========================== CONVERTING OTHER TYPES TO TUPLE ==========================  
list1 = [10, 20, 30]
set1 = {40, 50, 60}
string1 = "hello"

print(tuple(list1))  # Convert list to tuple
print(tuple(set1))  # Convert set to tuple
print(tuple(string1))  # Convert string to tuple (each char as item)

# ========================== UNPACKING TUPLE ELEMENTS ==========================  
a, b, c = (10, 20, 30)  # Unpack values into variables
print(a, b, c)

first, *middle, last = (1, 2, 3, 4, 5)
print(first, middle, last)

# ========================== USING TUPLE IN FUNCTIONS ==========================  
def sum_tuple(tpl):
    return sum(tpl)

print(sum_tuple((1, 2, 3, 4, 5)))

# ========================== NESTED TUPLES (2D TUPLES) ==========================  
nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(nested_tuple[0])  # First row
print(nested_tuple[1][2])  # Element at row 1, col 2

# ========================== TUPLE ZIP FUNCTION ==========================  
names = ("Alice", "Bob", "Charlie")
ages = (25, 30, 35)

zipped = tuple(zip(names, ages))  # Pair elements from two tuples
print(zipped)

# ========================== TUPLE COMPREHENSION (GENERATOR EXPRESSIONS) ==========================  
squares = tuple(x ** 2 for x in range(1, 6))  # Generate squares
print(squares)

evens = tuple(x for x in range(10) if x % 2 == 0)  # Filter even numbers
print(evens)

# ========================== CONVERTING LIST TO TUPLE AND VICE VERSA ==========================  
tuple_to_list = list(tuple1)  # Convert tuple to list
list_to_tuple = tuple(list1)  # Convert list to tuple
print(tuple_to_list)
print(list_to_tuple)

# ========================== FINDING COMMON ELEMENTS BETWEEN TWO TUPLES ==========================  
tupleX = (1, 2, 3, 4, 5)
tupleY = (4, 5, 6, 7, 8)

common = tuple(set(tupleX) & set(tupleY))
print(common)

# ========================== CHECKING IF A TUPLE IS EMPTY ==========================  
empty_tuple = ()
print(len(empty_tuple) == 0)  # Check if empty

# ========================== SPLITTING A TUPLE INTO CHUNKS ==========================  
def chunk_tuple(tpl, size):
    return tuple(tpl[i:i + size] for i in range(0, len(tpl), size))

print(chunk_tuple((1, 2, 3, 4, 5, 6, 7, 8), 3))

# ========================== FLATTENING A NESTED TUPLE ==========================  
nested_tuple = ((1, 2), (3, 4), (5, 6))
flat_tuple = tuple(item for subtuple in nested_tuple for item in subtuple)
print(flat_tuple)

# ========================== ROTATING A TUPLE ==========================  
def rotate_tuple(tpl, k):
    return tpl[-k:] + tpl[:-k]

print(rotate_tuple((1, 2, 3, 4, 5), 2))  # Rotate right by 2
