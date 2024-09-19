
# TODO Operators
# ? AND, OR, NOT 

var = 1
# Example 1:
print(var > 0) # True
print(not (var <= 0)) # True


# Example 2:
print(var != 0) # True
print(not (var == 0)) # True

# ? Bitwise Operators
""" 
& (ampersand). bitwise conjunction;
| (bar). bitwise disjunction;
~ (tilde). bitwise negation;
^ (caret). bitwise exclusive or (xor).
"""

# TODO Logical vs Bit operations
""" 
x = x & y  ->  x &= y  # * logical AND
x = x | y  ->  x |= y  # * logical OR
x = x ^ y  ->  x ^= y  # * logical XOR
"""

# TODO Shift operators
""" 
<<  # * left shift
>>  # * right shift
"""
var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right) # 17 68 8

# 17 >> 1 → 17 // 2 (17 floor-divided by 2 to the power of 1) → 8 (shifting to the right by one bit is the same as integer division by two)

# 17 << 2 → 17 * 4 (17 multiplied by 2 to the power of 2) → 68 (shifting to the left by two bits is the same as integer multiplication by four)

# TODO Section summary
""" 
 Python supports the following logical operators:

and → if both operands are true, the condition is true, e.g., (True and True) is True,
or → if any of the operands are true, the condition is true, e.g., (True or False) is True,
not → returns false if the result is true, and returns true if the result is false, e.g., not True is False.
2. You can use bitwise operators to manipulate single bits of data. The following sample data:

x = 15, which is 0000 1111 in binary,
y = 16, which is 0001 0000 in binary.
will be used to illustrate the meaning of bitwise operators in Python. Analyze the examples below:

& does a bitwise and, e.g., x & y = 0, which is 0000 0000 in binary,
| does a bitwise or, e.g., x | y = 31, which is 0001 1111 in binary,
˜  does a bitwise not, e.g., ˜ x = 240*, which is 1111 0000 in binary,
^ does a bitwise xor, e.g., x ^ y = 31, which is 0001 1111 in binary,
>> does a bitwise right shift, e.g., y >> 1 = 8, which is 0000 1000 in binary,
<< does a bitwise left shift, e.g., y << 3 = 128, which is 1000 0000 in binary.
* -16 (decimal from signed 2's complement)
"""

# ? Quiz 1
x = 1
y = 0

z = ((x == y) and (x == y)) or not(x == y)
print(not(z)) # $ False


# ? Quiz 2
x = 4
y = 1

a = x & y
b = x | y
c = ~x  # tricky!
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f) # $ 0 5 -5 1 1 16
