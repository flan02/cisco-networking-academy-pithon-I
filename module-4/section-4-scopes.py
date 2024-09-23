
# - Scopes in Python

# def scope_test():
#    x = 123

# scope_test()
# print(x) # NameError: name 'x' is not defined. x is not defined outside the function (out of scope)

def my_function():
    print("Do I know that variable?", var)


var = 1 # ! a variable existing outside a function has scope inside the function's body.
my_function() # | Do I know that variable? 1
print(var) # In this case, the variable is defined outside the function, so it's in the global scope


# ? This rule has a very important exception. Let's try to find it.
def my_function():
    var = 2 # ! a variable defined inside a function has a local scope has more priority than a global scope
    print("Do I know that variable?", var)


var = 1
my_function() # | Do I know that variable? 2
print(var) # | 1


# - Functions and scopes: the global keyword
def my_function():
    global var # ! the global keyword allows you to modify a global variable from within a function
    var = 2
    print("Do I know that variable?", var)


var = 1 # ? the global keyword is used to modify the global variable
my_function() # | Do I know that variable? 2
print(var) # | 2


# - How the function interacts with its arguments
def my_function(n):
    print("I got", n)
    n += 1
    print("I have", n)


var = 1
my_function(var) # | I got 1, I have 2
print(var) # | 1


# - Functions behavior using lists
def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2) # | Print #1: [2, 3], Print #2: [2, 3], Print #3: [0, 1], Print #4: [2, 3]
print("Print #5:", my_list_2) # | Print #5: [2, 3]



def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]  # TODO Pay attention to this line.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2) # | Print #1: [2, 3], Print #2: [2, 3], Print #3: [3], Print #4: [3]
print("Print #5:", my_list_2) # | Print #5: [3]
# ! The del instruction doesn't create a new list, it modifies the existing one.
