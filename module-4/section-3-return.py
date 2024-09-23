
# TODO The RETURN instruction

# ? RETURN without a value
def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return # return exits the function

    print("Happy New Year!")

happy_new_year() # prints the countdown and the wishes
happy_new_year(wishes = False) # only prints the countdown

# ? RETURN with a value
def boring_function():
    return 123

x = boring_function()

print("The boring_function has returned its result. It's:", x)


def boring_function():
    print("'Boredom Mode' ON.")
    return 123

print("This lesson is interesting!")
boring_function() # ! the function is called, but the return value is not used because it's not assigned to a variable
print("This lesson is boring...")


# - NONE
""" 
Let us introduce you to a very curious value (to be honest, a none value) named None.
Its data doesn't represent any reasonable value ‒ actually, it's not a value at all; hence, it mustn't take part in any expressions.
"""
# print(None + 2) # TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

# ! NONE is a keyword, not a value

value = None
if value is None:
    print("Sorry, you don't carry any value") 


def strange_function(n):
    if(n % 2 == 0):
        return True

print(strange_function(2)) # True
print(strange_function(1)) # None (it may be the symptom of a subtle mistake inside the fc)


# TODO Effects and results: Lists and functions

def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s

print(list_sum([5, 4, 3])) # 12
print(list_sum([5])) # 

def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5)) # [4, 3, 2, 1, 0]


# ? LAB 1 - A leap year: writing your own fc
def is_year_leap(year):
    if year % 4 != 0: # if the year is not divisible by 4
        return False
    elif year % 100 != 0: # if the year is not divisible by 100
        return True
    elif year % 400 != 0: # if the year is not divisible by 400
        return False
    else:
        return True

test_data = [1900, 2000, 2016, 1988]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr) # | Calling your function
    if result == test_results[i]:
        print("OK") # if the result is as expected
    else:
        print("Failed") # if the result is not as expected



# ? LAB 2 - How many days: writing and using your own fc
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year,month):
    if year < 1582 or month < 1 or month > 12: # if the year is less than 1582 or the month is less than 1 or greater than 12
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days[month - 1]
    if month == 2 and is_year_leap(year): # if the month is February and the year is a leap year
        res = 29
    return res

test_years = [1900, 2000, 2016, 1987] 
test_months = [ 2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr,mo,"-> ",end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")


# ? LAB 3 - Day of the year: writing and using your own fc
def is_year_leap(year): # function to check if the year is a leap year
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month): # function to get the number of days in a month
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res

def day_of_year(year, month, day): # function to get the day of the year
    days = 0
    for m in range(1, month):
        md = days_in_month(year, m) # get the number of days in the month
        if md == None:
            return None
        days += md
    md = days_in_month(year, month) # get the number of days in the month
    if day >= 1 and day <= md:
        return days + day # return the day of the year
    else:
        return None

print(day_of_year(2000, 12, 31))



# ? LAB 4 - The calculator: writing and using your own fc
def calculator(operation, x, y):
    if operation == '+':
        return x + y
    elif operation == '-':
        return x - y
    elif operation == '*':
        return x * y
    elif operation == '/':
        if y != 0:
            return x / y
        else:
            return None
    else:
        return None
    
print(calculator('*', 2, 3)) # 6
print(calculator('/', 2, 0)) # None
print(calculator('+', 2, 3)) # None


# ? LAB 5 - Prime numbers - how to find them
def is_prime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print() # 2 3 5 7 11 13 17 19


# ? LAB 6 - Converting fuel consumption
# 1 American mile = 1609.344 metres
# 1 American gallon = 3.785411784 litres

def liters_100km_to_miles_gallon(litres):
    gallons = litres / 3.785411784
    miles = 100 * 1000 / 1609.344
    return miles / gallons

def miles_gallon_to_liters_100km(miles):
    km100 = miles * 1609.344 / 1000 / 100
    litres = 3.785411784
    return litres / km100

print(liters_100km_to_miles_gallon(3.9)) # 60.31143162393162
print(liters_100km_to_miles_gallon(7.5)) # 31.36194444444444
print(liters_100km_to_miles_gallon(10.)) # 23.52145833333333
print(miles_gallon_to_liters_100km(60.3)) # 3.9007393587617467
print(miles_gallon_to_liters_100km(31.4)) # 7.490910297239916
print(miles_gallon_to_liters_100km(23.5)) # 10.009131205673757