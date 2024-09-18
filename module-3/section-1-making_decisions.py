# TODO Conditionals

# Conditionals are used to make decisions in Python. The most common conditional statement is the if statement.
a = b = 5 # Assigning 5 to a and b
a == b # True

var = 0  # Assigning 0 to var
print(var == 0)

var = 1  # Assigning 1 to var
print(var == 0)

var = 0  # Assigning 0 to var
print(var != 0)
 
var = 1  # Assigning 1 to var
print(var != 0)

# TODO LABS ->
""" 
Using one of the comparison operators in Python, write a simple two-line program that takes the parameter n as input, which is an integer, and prints False if n is less than 100, and True if n is greater than or equal to 100.

Don't create any if blocks (we're going to talk about them very soon). Test your code using the data we've provided for you.
"""

n = int(input("Enter a number: "))
print(n >= 100)

# TODO Extra examples of Conditionals
# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Print the result
print("The larger number is:", larger_number)

# TODO Extra example -> get max number using if conditional
# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

largest_number = number1

if number2 > largest_number:
    largest_number = number2

if number3 > largest_number:
    largest_number = number3

# Print the result
print("The largest number is:", largest_number)

# $ Python built-in function: max() | min()  These functions obtains min and max values
# Read three numbers.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.

largest_number = max(number1, number2, number3)
shortest_number = min(number1, number2, number3)

# Print the result.
print("The largest number is:", largest_number)
print("The shortest number is:", shortest_number)

# TODO Essentials of the if-else statement
"""
if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was what they called tax relief).

if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.
"""
income = float(input("Enter the annual income: "))

if income < 85528:
	tax = income * 0.18 - 556.02
else:
	tax = (income - 85528) * 0.32 + 14839.02

if tax < 0.0:
	tax = 0.0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")

# TODO Essentials of the if-elif-else statement
""" 
if the year number isn't divisible by four, it's a common year;
otherwise, if the year number isn't divisible by 100, it's a leap year;
otherwise, if the year number isn't divisible by 400, it's a common year;
otherwise, it's a leap year.
"""
year = int(input("Enter a year: "))

if year < 1582:
	print("Not within the Gregorian calendar period")
else:
	if year % 4 != 0:
		print("Common year")
	elif year % 100 != 0:
		print("Leap year")
	elif year % 400 != 0:
		print("Common year")
	else:
		print("Leap year")
		

# TODO Elif reasoning
x = 10

if x == 10: # * True
    print("x == 10")

if x > 15: # * False
    print("x > 15")

elif x > 10: # * False
    print("x > 10")

elif x > 5: # * True
    print("x > 5")

else:
    print("else will not be executed")


# TODO Nested conditionals

x = 10

if x > 5: # * True
    if x == 6: # * False
        print("nested: x == 6")
    elif x == 10: # * True
        print("nested: x == 10")
    else:
        print("nested: else")
else:
    print("else")


# ? Quiz
x, y, z = 5, 10, 8
 
print(x > z)
print((y - 5) == x)


# ? Quiz II
x = "1"
 
if x == 1:
    print("one")
elif x == "1":
    if int(x) > 1:
        print("two")
    elif int(x) < 1:
        print("three")
    else:
        print("four") # * answer one
if int(x) == 1:
    print("five") # * answer two
else:
    print("six") 

# ? Quiz III

x = 1
y = 1.0
z = "1"
 
if x == y:
    print("one") # * answer one
if y == int(z):
    print("two") # * answer two
elif x == y:
    print("three")
else:
    print("four")