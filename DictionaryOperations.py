# ========================== DICTIONARY CREATION ==========================  
dict1 = {"name": "Alice", "age": 25, "city": "New York"}  # Standard dictionary
dict2 = dict(name="Bob", age=30, city="Los Angeles")  # Using dict() constructor
dict3 = {1: "one", 2: "two", 3: "three"}  # Integer keys
dict4 = {}  # Empty dictionary
dict5 = dict([(1, "one"), (2, "two")])  # From list of tuples

print(dict1)
print(dict2)
print(dict3)
print(dict4)
print(dict5)

# ========================== ACCESSING ELEMENTS ==========================  
print(dict1["name"])  # Access value using key
print(dict1.get("age"))  # Access value using get() (returns None if key is missing)
print(dict1.get("salary", "Not Available"))  # Get with default value

# ========================== MODIFYING DICTIONARY ==========================  
dict1["age"] = 26  # Update existing key
dict1["country"] = "USA"  # Add new key-value pair
print(dict1)

# ========================== DELETING ELEMENTS ==========================  
del dict1["city"]  # Delete specific key
print(dict1)

dict1.pop("country")  # Remove key and return its value
print(dict1)

dict1.popitem()  # Remove last key-value pair
print(dict1)

dict1.clear()  # Remove all elements
print(dict1)

# ========================== DICTIONARY METHODS ==========================  

# ---------- Adding & Updating ----------  
dict1 = {"name": "Alice", "age": 25}
dict1.update({"city": "New York", "age": 26})  # Update multiple keys
print(dict1)

# ---------- Copying Dictionary ----------  
dict2 = dict1.copy()  # Shallow copy
print(dict2)

# ---------- Keys, Values & Items ----------  
print(dict1.keys())  # Get all keys
print(dict1.values())  # Get all values
print(dict1.items())  # Get all key-value pairs

# ========================== CHECKING ELEMENT EXISTENCE ==========================  
print("name" in dict1)  # Check if key exists
print("salary" not in dict1)  # Check if key does not exist

# ========================== ITERATING THROUGH DICTIONARY ==========================  
for key in dict1:
    print(key, dict1[key])  # Loop through keys and values

for key, value in dict1.items():
    print(f"{key}: {value}")  # Loop using items()

# ========================== BUILT-IN DICTIONARY FUNCTIONS ==========================  
print(len(dict1))  # Get dictionary size

# ========================== DEFAULT DICTIONARY VALUES ==========================  
from collections import defaultdict
ddict = defaultdict(int)  # Default value of int (0)
ddict["a"] += 1  # Increments without KeyError
print(ddict)

# ========================== MERGING DICTIONARIES (Python 3.9+) ==========================  
dictA = {"a": 1, "b": 2}
dictB = {"b": 3, "c": 4}

merged_dict = dictA | dictB  # Merges dictionaries (Python 3.9+)
print(merged_dict)

# ========================== DICTIONARY COMPREHENSION ==========================  
squared = {x: x ** 2 for x in range(1, 6)}  # Create dict with squares
print(squared)

# ========================== CONVERTING BETWEEN DATA TYPES ==========================  
list_of_tuples = [("name", "Alice"), ("age", 25)]
dict_from_tuples = dict(list_of_tuples)  # Convert list of tuples to dict
print(dict_from_tuples)

keys = ["name", "age", "city"]
default_value = "Unknown"
dict_from_keys = dict.fromkeys(keys, default_value)  # Create dict with default values
print(dict_from_keys)

# ========================== NESTED DICTIONARIES ==========================  
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}
print(nested_dict["person1"]["name"])  # Access nested value

# ========================== SORTING A DICTIONARY ==========================  
unsorted_dict = {"b": 2, "c": 3, "a": 1}
sorted_by_key = dict(sorted(unsorted_dict.items()))  # Sort by key
print(sorted_by_key)

sorted_by_value = dict(sorted(unsorted_dict.items(), key=lambda item: item[1]))  # Sort by value
print(sorted_by_value)

# ========================== FILTERING A DICTIONARY ==========================  
original_dict = {"a": 10, "b": 20, "c": 5, "d": 30}
filtered_dict = {k: v for k, v in original_dict.items() if v > 10}
print(filtered_dict)

# ========================== FINDING MAX, MIN, SUM ==========================  
num_dict = {"a": 10, "b": 20, "c": 5}
print(max(num_dict, key=num_dict.get))  # Key with max value
print(min(num_dict, key=num_dict.get))  # Key with min value
print(sum(num_dict.values()))  # Sum of values

# ========================== INVERTING A DICTIONARY (KEYS ↔ VALUES) ==========================  
inverted_dict = {v: k for k, v in num_dict.items()}
print(inverted_dict)

# ========================== USING DICTIONARY IN FUNCTIONS ==========================  
def print_dict(d):
    for k, v in d.items():
        print(f"{k}: {v}")

print_dict({"name": "Alice", "age": 25})

# ========================== CHECKING IF DICTIONARY IS EMPTY ==========================  
empty_dict = {}
print(len(empty_dict) == 0)  # Check if empty
print(bool(empty_dict))  # False if empty, True otherwise
