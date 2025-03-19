# ========================== SET CREATION ==========================  
set1 = {1, 2, 3, 4, 5}  # Standard set
set2 = {"apple", "banana", "cherry"}  # Set of strings
set3 = set([10, 20, 30])  # Convert list to set
set4 = set()  # Empty set (note: {} creates an empty dictionary)

print(set1)
print(set2)
print(set3)
print(set4)

# ========================== ADDING ELEMENTS ==========================  
set1.add(6)  # Add a single element
print(set1)

set1.update([7, 8, 9])  # Add multiple elements
print(set1)

# ========================== REMOVING ELEMENTS ==========================  
set1.remove(3)  # Remove an element (raises KeyError if not found)
print(set1)

set1.discard(10)  # Remove element if exists (no error if missing)
print(set1)

popped_value = set1.pop()  # Remove and return an arbitrary element
print(popped_value)
print(set1)

set1.clear()  # Remove all elements
print(set1)

# ========================== SET OPERATIONS ==========================  
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

print(setA | setB)  # Union (Combine elements from both sets)
print(setA & setB)  # Intersection (Common elements)
print(setA - setB)  # Difference (Elements in setA but not in setB)
print(setB - setA)  # Difference (Elements in setB but not in setA)
print(setA ^ setB)  # Symmetric Difference (Elements in either set, but not both)

# ========================== IN-PLACE SET OPERATIONS ==========================  
setA |= setB  # In-place Union
print(setA)

setA &= setB  # In-place Intersection
print(setA)

setA -= setB  # In-place Difference
print(setA)

setA ^= setB  # In-place Symmetric Difference
print(setA)

# ========================== CHECKING ELEMENT EXISTENCE ==========================  
setC = {10, 20, 30, 40}
print(10 in setC)  # Check if element exists
print(50 not in setC)  # Check if element does not exist

# ========================== SET METHODS ==========================  

# ---------- Copying ----------  
setD = setC.copy()  # Copy set
print(setD)

# ---------- Finding Subset & Superset ----------  
setX = {1, 2}
setY = {1, 2, 3, 4}

print(setX.issubset(setY))  # Check if setX is a subset of setY
print(setY.issuperset(setX))  # Check if setY is a superset of setX

# ---------- Checking Disjoint Sets ----------  
setM = {1, 2, 3}
setN = {4, 5, 6}

print(setM.isdisjoint(setN))  # Check if sets have no common elements

# ========================== SET BUILT-IN FUNCTIONS ==========================  
setE = {5, 10, 15, 20, 25}

print(len(setE))  # Get set size
print(max(setE))  # Get max value
print(min(setE))  # Get min value
print(sum(setE))  # Sum of all elements

# ========================== CONVERTING BETWEEN DATA TYPES ==========================  
list1 = [1, 2, 2, 3, 4, 4, 5]
tuple1 = (6, 7, 7, 8, 9)

print(set(list1))  # Convert list to set (removes duplicates)
print(set(tuple1))  # Convert tuple to set

# ========================== ITERATING THROUGH SETS ==========================  
setF = {"Python", "Java", "C++"}

for item in setF:
    print(item)  # Loop through elements

# ========================== FROZEN SET (IMMUTABLE SET) ==========================  
frozen_set1 = frozenset([1, 2, 3, 4])
print(frozen_set1)

# frozen_set1.add(5)  # ❌ This will cause an error (frozen sets are immutable)

# ========================== FILTERING A SET ==========================  
original_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
filtered_set = {x for x in original_set if x % 2 == 0}  # Keep only even numbers
print(filtered_set)

# ========================== FINDING COMMON ELEMENTS BETWEEN MULTIPLE SETS ==========================  
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {4, 5, 6, 7}

common_elements = set1 & set2 & set3  # Find common elements in all sets
print(common_elements)

# ========================== MERGING MULTIPLE SETS ==========================  
merged_set = set1.union(set2, set3)
print(merged_set)

# ========================== CHECKING IF A SET IS EMPTY ==========================  
empty_set = set()
print(len(empty_set) == 0)  # Check if empty
print(bool(empty_set))  # False if empty, True otherwise
