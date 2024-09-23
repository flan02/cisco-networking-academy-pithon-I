
# TODO Funtions environment communications

def message(what, number):
    print("Enter", what, "number", number)

message("telephone", 11)
message("price", 5)
message("number", "number")

def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction("Luke", "Skywalker") # order matters
introduction(last_name = "Skywalker", first_name = "Luke") # order doesn't matter

def introduction(first_name, last_name="Smith"): # default value in case no value is passed
     print("Hello, my name is", first_name, last_name)

introduction("John", "Doe") # if 2nd parameter is passed, it will override the default value

def add_numbers(a, c, b=2): # default value should be at the end
    print(a + b + c) # 1 + 2 + 3 = 6

add_numbers(a=1, c=3)
