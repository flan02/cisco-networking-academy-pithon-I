my_list = [1, 2]

for v in range(2):
    my_list.insert(-1, my_list[v])

print(my_list) # [1, 1, 1, 2]

nums = [1, 2, 3]
vals = nums 
print(vals == nums) # True

""" 
def function_1(a):
    return None


def function_2(a):
    return function_1(a) * function_1(a) # Error


print(function_2(2)) # None
"""

print(1 // 2) # 0

def func(a, b):
    return b ** a


# print(func(b=2, 2)) ERROR

z = 0
y = 10
x = y < z and z > y or y < z and z < y # False

my_list =  [x * x for x in range(5)]


def fun(lst):
    del lst[lst[2]]
    return lst


print(fun(my_list)) # [0, 1, 4, 9]

x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z

print(x, y, z) # 1 1 2

a = 1
b = 0
a = a ^ b # 1
b = a ^ b # 1
a = a ^ b # 0

print(a, b) # 0 1


def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 2


print(fun(fun(2))) # 2

nums = [1, 2, 3]
vals = nums # [1, 2, 3]
del vals[:] # []
print(nums) # []
print(vals) # []

x = int(input(3))
y = int(input(2))
x = x % y # 1
x = x % y # 1
y = y % x # 0
print(y) # 0

y = input("3")
x = input("6")
print(x + y) # 63

print("a", "b", "c", sep="sep") # asepbsepc

x = 1 // 5 + 1 / 5 
print(x) # 0.2

""" 
my_tuple = (1, 2, 3)
my_tuple[1] = my_tuple[1] + my_tuple[0] # Error
"""

x = float(input(2)) # 2
y = float(input(4)) # 4
print(y ** (1 / x)) # (4 ** (1 / 2) = 2.0) _Seria como resolver la raiz cuadrada de 4

dct = {
    'one': 'two', 
    'three': 'one', 
    'two': 'three'
    }
v = dct['three'] # one

for k in range(len(dct)):
    v = dct[v] # dct['one'] = two

print(v) # two

lst = [i for i in range(-1, -2)] 
print(lst) # []


def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y-1) 


print(fun(0, 3)) # 0

""" 
i = 0
while i < i + 2 : 
    i += 1
    print("*") # star will be printed infinitely
else:
    print("*") 
"""


tup = (1, 2, 4, 8)
tup = tup[-2:-1] # (4,)
tup = tup[-1] # 4
print(tup) # 4

dd = {
    "1": "0", 
    "0": "1"
    }
""" 
for x in dd.vals():
    print(x, end="") # Error
"""

dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)

for x in dct.keys():
    print(dct[x][1], end="") # 21

def fun(inp=2, out=3):
    return inp * out


print(fun(out=2)) # 4

lst = [[x for x in range(3)] for y in range(3)] # [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

for r in range(3): 
    for c in range(3):
        if lst[r][c] % 2 != 0: 
            print("#") 

try:
    value = input("Enter a value: ")
    print(int(value)/len(value)) # 0/1 = 0.0
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input...")
except TypeError:
    print("Very very bad input...")
except:
    print("Booo!")

""" 
try:
    {}
except:
    print("Sorry, something went wrong...")
except (ValueError, ZeroDivisionError):
    print("Too bad...")
"""

foo = (1, 2, 3)
foo.index(0) # Error. Which type of error? ... ValueError

""" 
print(Hello, World!) # Error. Which type of error? ... SyntaxError
"""

