#
# ! RESERVED KEYWORDS (it cannot be used as a variable name)
""" 
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""

var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)

var = "3.12.6"
print("Python version: " + var)


var = 100
print(var)
var = var + 1 # Reassigning the value of var
print(var)
var += 1 # Incrementing the value of var
print(var)

var = 100
var = 200 + 300 # Reassigning the value of previous variable var
print(var) # 500

print("Solving simple mathematical problems")
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5 # ? Pythagorean theorem (c = √ a² + b² )
print("c =", c)


# TODO -> Labs 1
""" 
Here is a short story:

Once upon a time in Appleland, John had three apples, Mary had five apples, and Adam had six apples. They were all very happy and lived for a long time. End of story.

Your task is to:

create the variables: john, mary, and adam;
assign values to the variables. The values must be equal to the numbers of fruit possessed by John, Mary, and Adam respectively;
having stored the numbers in the variables, print the variables on one line, and separate each of them with a comma;
now create a new variable named total_apples equal to the addition of the three previous variables.
print the value stored in total_apples to the console;
experiment with your code: create new variables, assign different values to them, and perform various arithmetic operations on them (e.g., +, -, *, /, //, etc.). Try to print a string and an integer together on one line, e.g., "Total number of apples:" and total_apples.
"""

john = 3; adam = 6; mary = 5 # Assigning values to the variables in one line
print(john, mary, adam)
total_apples = john + mary + adam
print("Total number of apples:", total_apples)

# TODO -> Labs 2
""" 
Miles and kilometers are units of length or distance.

Bearing in mind that 1 mile is equal to approximately 1.61 kilometers, complete the program in the editor so that it converts:

miles to kilometers;
kilometers to miles.
Do not change anything in the existing code. Write your code in the places indicated by ###. Test your program with the data we've provided in the source code.

Pay particular attention to what is going on inside the print() function. Analyze how we provide multiple arguments to the function, and how we output the expected data.

Note that some of the arguments inside the print() function are strings (e.g., "miles is", whereas some other are variables (e.g., miles).
"""

kilometers = 12.25
miles = 7.38

miles_to_kilometers = 12.25 * 1.61
kilometers_to_miles = 7.38 / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")


# TODO -> Labs 3
""" 
Take a look at the code in the editor: it reads a float value, puts it into a variable named x, and prints the value of a variable named y. Your task is to complete the code in order to evaluate the following expression:

3x3 - 2x2 + 3x - 1

The result should be assigned to y.
"""

x = 0
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y) #  -1

x = 1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y) #  3

x = -1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y) #  -9  


