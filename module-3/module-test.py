x = 1
x = x == x # x == x is True

i = 0
while i <= 3 :
    i += 2
    print("*") # prints * 2 times

i = 0
while i <= 5 :
    i += 1
    if i % 2 == 0:
      break
    print("*") # prints * 1 time

for i in range(1):
    print("#") # prints #
else:
    print("#") # prints #

var = 0
while var < 6:
    var += 1
    if var % 2 == 0: 
        continue
    print("#") # prints # 3 times

var = 1
while var < 10:
    print("#")  # prints # 4 times
    var = var << 1  

z = 10
y = 0
x = y < z and z > y or y > z and z < y
print(x) # prints True

a = 1
b = 0
c = a & b
d = a | b
e = a ^ b
print(c + d + e) # prints 1

my_list = [3, 1, -2]
print(my_list[my_list[-1]]) # prints 1

my_list = [1, 2, 3, 4]
print(my_list[-3:-2]) # prints [2]

vals = [0, 1, 2]
vals[0], vals[2] = vals[2], vals[0] # vals = [2, 1, 0]. Reverse the list

vals = [0, 1, 2]
vals.insert(0, 1) # vals = [1, 0, 1, 2]
del vals[1] # vals = [1, 1, 2]
# sum of the list = 4


my_list_1 = [1, 2, 3]
my_list_2 = []
for v in my_list_1:
    my_list_2.insert(0, v) # inserts the value at the beginning of the list
print(my_list_2) # prints [3, 2, 1]


my_list = [1, 2, 3]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
print(my_list) # prints [1, 1, 1, 1, 2, 3]

my_list = [i for i in range(-1, 2)]
print(my_list) # prints [-1, 0, 1]

t = [[3-i for i in range (3)] for j in range (3)] # t = [[3, 2, 1], [3, 2, 1], [3, 2, 1]]
s = 0
for i in range(3): 
    s += t[i][i] # sum of the diagonal elements of the matrix [3+2+1]
print(s) # prints 6

my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list[2][0]) # prints IndexError: list index out of range

