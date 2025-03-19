# ========================== LIST CREATION ==========================  
list1 = [1, 2, 3, 4, 5]  # List of integers
list2 = ["apple", "banana", "cherry"]  # List of strings
list3 = [1, "hello", 3.14, True]  # Mixed data types
list4 = list((10, 20, 30))  # Create list from tuple

print(list1)
print(list2)
print(list3)
print(list4)

# ========================== ACCESSING ELEMENTS ==========================  
print(list1[0])  # First element
print(list1[-1])  # Last element
print(list1[1:4])  # Slicing (index 1 to 3)
print(list1[:3])  # First 3 elements
print(list1[2:])  # From index 2 to end
print(list1[::-1])  # Reverse list

# ========================== LIST ITERATION ==========================  
for item in list2:
    print(item, end=" ")  # Iterate through elements
print()

# ========================== LIST METHODS ==========================  

# ---------- Modifying Lists ----------  
list1.append(6)  # Append element at the end
print(list1)

list1.insert(2, 99)  # Insert at index 2
print(list1)

list1.extend([7, 8, 9])  # Extend list with another list
print(list1)

list1[1] = 50  # Update value at index 1
print(list1)

# ---------- Removing Elements ----------  
list1.pop()  # Remove last element
print(list1)

list1.pop(2)  # Remove element at index 2
print(list1)

list1.remove(50)  # Remove first occurrence of value 50
print(list1)

del list1[1]  # Delete element at index 1
print(list1)

list1.clear()  # Remove all elements
print(list1)

# ---------- Searching & Counting ----------  
list1 = [1, 2, 3, 3, 4, 5, 3]
print(list1.index(3))  # Find index of first occurrence of 3
print(list1.count(3))  # Count occurrences of 3

# ---------- Sorting & Reversing ----------  
list1.sort()  # Sort list in ascending order
print(list1)

list1.sort(reverse=True)  # Sort list in descending order
print(list1)

list1.reverse()  # Reverse list
print(list1)

# ========================== LIST OPERATIONS ==========================  
listA = [1, 2, 3]
listB = [4, 5, 6]

print(listA + listB)  # Concatenation
print(listA * 3)  # Repeat list 3 times

# ========================== LIST COMPREHENSION ==========================  
squares = [x ** 2 for x in range(1, 6)]  # Generate squares
print(squares)

evens = [x for x in range(10) if x % 2 == 0]  # Filter even numbers
print(evens)
 
# ========================== CHECKING ELEMENT EXISTENCE ==========================  
print(3 in list1)  # Check if 3 is in list
print(100 not in list1)  # Check if 100 is not in list

# ========================== COPYING A LIST ==========================  
listC = listA.copy()  # Copy list
print(listC)

# ========================== BUILT-IN LIST FUNCTIONS ==========================  
print(len(list1))  # Get length of list
print(max(list1))  # Get max value
print(min(list1))  # Get min value
print(sum(list1))  # Get sum of elements

# ========================== CONVERTING OTHER TYPES TO LIST ==========================  
tuple1 = (10, 20, 30)
set1 = {40, 50, 60}
string1 = "hello"

print(list(tuple1))  # Convert tuple to list
print(list(set1))  # Convert set to list
print(list(string1))  # Convert string to list (each char as item)

# ========================== UNPACKING LIST ELEMENTS ==========================  
a, b, c = [10, 20, 30]  # Unpack values into variables
print(a, b, c)

first, *middle, last = [1, 2, 3, 4, 5]
print(first, middle, last)

# ========================== USING LIST IN FUNCTIONS ==========================  
def sum_list(lst):
    return sum(lst)

print(sum_list([1, 2, 3, 4, 5]))

# ========================== NESTED LISTS (2D LISTS) ==========================  
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0])  # First row
print(matrix[1][2])  # Element at row 1, col 2

# ========================== MAP & FILTER WITH LISTS ==========================  
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))  # Double each number
print(doubled)

evens = list(filter(lambda x: x % 2 == 0, numbers))  # Filter even numbers
print(evens)

# ========================== LIST ZIP FUNCTION ==========================  
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

zipped = list(zip(names, ages))  # Pair elements from two lists
print(zipped)

# ========================== SPLITTING A LIST INTO CHUNKS ==========================  
def chunk_list(lst, size):
    return [lst[i:i + size] for i in range(0, len(lst), size)]

print(chunk_list([1, 2, 3, 4, 5, 6, 7, 8], 3))

# ========================== FLATTENING A NESTED LIST ==========================  
nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)

# ========================== ROTATING A LIST ==========================  
def rotate(lst, k):
    return lst[-k:] + lst[:-k]

print(rotate([1, 2, 3, 4, 5], 2))  # Rotate right by 2

# ========================== FINDING COMMON ELEMENTS BETWEEN TWO LISTS ==========================  
listX = [1, 2, 3, 4, 5]
listY = [4, 5, 6, 7, 8]

common = list(set(listX) & set(listY))
print(common)

# ========================== REMOVING DUPLICATES FROM A LIST ==========================  
unique_list = list(set([1, 2, 2, 3, 3, 4, 5]))
print(unique_list)
