# ========================== NUMERIC TYPES ==========================  
a = 10           # Integer
b = 10.5        # Float
c = 3 + 4j      # Complex Number

print(type(a))  # Check type
print(type(b))
print(type(c))

# ========================== BASIC ARITHMETIC OPERATIONS ==========================  
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division (returns float)
print(a // b)  # Floor division (integer division)
print(a % b)  # Modulus (remainder)
print(a ** 2)  # Exponentiation (Power)

# ========================== BUILT-IN NUMERIC FUNCTIONS ==========================  
print(abs(-10))  # Absolute value
print(pow(2, 3))  # Exponentiation (2^3)
print(round(10.678, 2))  # Round to 2 decimal places
print(divmod(10, 3))  # Returns (quotient, remainder)

# ========================== MIN, MAX, SUM ==========================  
nums = [1, 5, 3, 9, 2]
print(min(nums))  # Minimum value
print(max(nums))  # Maximum value
print(sum(nums))  # Sum of elements

# ========================== TYPE CONVERSIONS ==========================  
print(int(10.9))  # Convert float to int
print(float(10))  # Convert int to float
print(complex(2))  # Convert int to complex
print(complex(2, 3))  # Create complex number

# ========================== MATH MODULE FUNCTIONS ==========================  
import math

print(math.sqrt(16))  # Square root
print(math.factorial(5))  # Factorial (5!)
print(math.gcd(48, 18))  # Greatest common divisor
print(math.lcm(48, 18))  # Least common multiple (Python 3.9+)
print(math.fabs(-10.5))  # Absolute value (float)
print(math.exp(2))  # e^x (Exponential function)
print(math.log(10))  # Natural log (ln(x))
print(math.log10(100))  # Log base 10
print(math.log2(8))  # Log base 2
print(math.ceil(4.2))  # Round up
print(math.floor(4.9))  # Round down
print(math.trunc(4.9))  # Truncate (remove decimal part)
print(math.copysign(10, -1))  # Copy sign from another number
print(math.isfinite(10))  # Check if number is finite
print(math.isinf(float('inf')))  # Check if number is infinite
print(math.isnan(float('nan')))  # Check if number is NaN (Not-a-Number)

# ========================== TRIGONOMETRIC FUNCTIONS ==========================  
print(math.sin(math.radians(30)))  # Sine of 30 degrees
print(math.cos(math.radians(60)))  # Cosine of 60 degrees
print(math.tan(math.radians(45)))  # Tangent of 45 degrees
print(math.asin(0.5))  # Inverse Sine
print(math.acos(0.5))  # Inverse Cosine
print(math.atan(1))  # Inverse Tangent
print(math.degrees(math.pi))  # Convert radians to degrees
print(math.radians(180))  # Convert degrees to radians

# ========================== RANDOM MODULE FUNCTIONS ==========================  
import random

print(random.randint(1, 10))  # Random integer between 1 and 10
print(random.uniform(1, 10))  # Random float between 1 and 10
print(random.random())  # Random float between 0 and 1
print(random.choice([1, 2, 3, 4, 5]))  # Random choice from list
print(random.sample(range(1, 10), 3))  # Get 3 unique random numbers
random.shuffle(nums)  # Shuffle list randomly
print(nums)

# ========================== DECIMAL MODULE (For Precision Arithmetic) ==========================  
from decimal import Decimal, getcontext

getcontext().prec = 5  # Set precision to 5 digits
d1 = Decimal("10.12345")
d2 = Decimal("3.6789")
print(d1 + d2)  # Precise decimal addition

# ========================== FRACTIONS MODULE ==========================  
from fractions import Fraction

f1 = Fraction(1, 3)  # Create fraction 1/3
f2 = Fraction(3, 4)  # Create fraction 3/4
print(f1 + f2)  # Fraction addition
print(float(f1))  # Convert fraction to float
print(f1.limit_denominator(10))  # Simplify fraction

# ========================== COMPLEX NUMBER OPERATIONS ==========================  
c1 = complex(3, 4)
c2 = complex(1, -2)

print(c1 + c2)  # Complex addition
print(c1 - c2)  # Complex subtraction
print(c1 * c2)  # Complex multiplication
print(c1 / c2)  # Complex division

print(c1.real)  # Get real part
print(c1.imag)  # Get imaginary part
print(abs(c1))  # Get magnitude
print(c1.conjugate())  # Get complex conjugate

# ========================== BITWISE OPERATIONS (Only for Integers) ==========================  
x = 5  # Binary: 101
y = 3  # Binary: 011

print(x & y)  # AND operation (001 -> 1)
print(x | y)  # OR operation (111 -> 7)
print(x ^ y)  # XOR operation (110 -> 6)
print(~x)  # NOT operation (Two's complement)
print(x << 1)  # Left shift (1010 -> 10)
print(x >> 1)  # Right shift (10 -> 2)

# ========================== NUMBER REPRESENTATION FUNCTIONS ==========================  
print(bin(10))  # Convert to binary (0b1010)
print(oct(10))  # Convert to octal (0o12)
print(hex(10))  # Convert to hexadecimal (0xa)

# ========================== CHECKING NUMBER PROPERTIES ==========================  
print(isinstance(10, int))  # Check if int
print(isinstance(10.5, float))  # Check if float
print(isinstance(3 + 4j, complex))  # Check if complex

# ========================== FLOAT SPECIAL CASES ==========================  
print(float('inf'))  # Positive Infinity
print(float('-inf'))  # Negative Infinity
print(float('nan'))  # Not-a-Number (NaN)

# ========================== USING MAP & FILTER WITH NUMBERS ==========================  
nums = [1, 2, 3, 4, 5]
print(list(map(lambda x: x * 2, nums)))  # Double each number
print(list(filter(lambda x: x % 2 == 0, nums)))  # Filter even numbers
