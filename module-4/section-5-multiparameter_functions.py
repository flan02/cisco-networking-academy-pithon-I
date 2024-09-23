
# - MULTIPARAMETER FUNCTIONS

# ? Let's get started on a function to evaluate the Body Mass Index (BMI)
def bmi(weight, height):
    return weight / height ** 2

print(bmi(70, 1.75)) # | 22.857142857142858

# ? Evaluating BMI and converting imperial units to metric units
def bmi(weight, height, system="metric"):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200: # ! The backslash (\) allows you to continue the code on the next line
        return None
    if system == "imperial":
        return 703 * weight / height ** 2
    else:
        return weight / height ** 2
    
print(bmi(52.5, 1.65)) # | 22.857142857142858
print(bmi(10, 1.95)) # | None

def lb_to_kg(lb):
    return lb * 0.45359237

print(lb_to_kg(1)) # | 0.45359237

def ft_to_m(ft): 
    return ft * 0.3048

print(ft_to_m(1)) # | 0.3048

def ft_and_inch_to_m(ft, inch):
    return ft * 0.3048 + inch * 0.0254

print(ft_and_inch_to_m(1, 1)) # | 0.3302
print(ft_and_inch_to_m(6, 0)) # | 1.8288

def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254


print(ft_and_inch_to_m(6))

print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7))) # | 27.5


# - Sample functions: Triangles...
""" 
Let's play with triangles now. We'll start with a function to check whether three sides of given lengths can build a triangle.

We know from school that the sum of two arbitrary sides has to be longer than the third side.

It won't be a hard challenge. The function will have three parameters ‒ one for each side.

It will return True if the sides can build a triangle, and False otherwise. In this case, is_a_triangle is a good name for such a function.
"""
def is_a_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

print(is_a_triangle(1, 1, 1)) # | True
print(is_a_triangle(1, 1, 3)) # | False

# ? Can we make it more compact? It looks a bit wordy. Let's try to simplify it.
def is_a_triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True

print(is_a_triangle(1, 1, 1)) # | True
print(is_a_triangle(1, 1, 3)) # | False

# ? Can we compact it even more?
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

print(is_a_triangle(1, 1, 1)) # | True
print(is_a_triangle(1, 1, 3)) # | False



# - Sample functions Factorials
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1

    product = 1
    for i in range(2, n + 1):
        product *= i
    return product


for n in range(1, 6):  # testing
    print(n, factorial_function(n))


factorial_function(30) # | 265252859812191058636308480000000
factorial_function(-1) # | None
factorial_function(2) # | 2
factorial_function(5) # | 120


# - Sample functions Fibonacci numbers
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1): 
        the_sum = elem_1 + elem_2 
        elem_1, elem_2 = elem_2, the_sum
    return the_sum 


for n in range(1, 10):  # testing
    print(n, "->", fib(n))

fib(1) # | 1
fib(2) # | 1
fib(3) # | 2
fib(4) # | 3
fib(5) # | 5


# ? Quizzes

def factorial(n):
    return n * factorial(n - 1)


print(factorial(4)) # | RecursionError: maximum recursion depth exceeded in comparison




def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)


print(fun(25)) # | 56

