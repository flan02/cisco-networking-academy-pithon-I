
# TODO Lists !
numbers = [10, 5, 7, 2, 1]
print(numbers) # [10, 5, 7, 2, 1]
print(numbers[0]) # 10

numbers[0] = 111
print(numbers) # [111, 5, 7, 2, 1]

numbers[1] = numbers[4]
print(numbers) # [111, 1, 7, 2, 1] 

# ? Copies values between two indexes
numbers[1:3] = [55, 66]
print(numbers) # [111, 55, 66, 2, 1]

# ? Copies of list
numbers_copy = numbers.copy()
print(numbers_copy) # [111, 5, 7, 2, 1]

len(numbers) # 6
print("Total amount of elements: ", len(numbers)) # 6

# ? List slicing
print(numbers[1:]) # [5, 7, 2, 1]

# ? Removing elements form a list
numbers.pop() # Removes the last element
del numbers[1] # Removes the element at index 1
print(numbers) # [111, 7, 2]


numbers = [111, 7, 2, 1]
print(numbers[-1]) # 1 --> Last element
print(numbers[-2]) # 2 --> Second to last element


# TODO Adding elements to a list using methods
print("Adding elements to a list using methods")
# $ append() - Adds an element to the end of the list
# $ insert() - Adds an element at a specific index
# $ extend() - Adds multiple elements to the end of the list
# $ remove() - Removes the first occurrence of a value
# $ clear() - Removes all elements from the list
# $ index() - Returns the index of the first occurrence of a value
# $ count() - Returns the number of occurrences of a value
# $ sort() - Sorts the list in ascending order

# ? append()
numbers.append(4) # * Add 4 to the end of the list
print(numbers) # [111, 7, 2, 1, 4]

# ? insert()
numbers.insert(1, 55) # * Insert 55 at index 1
print(numbers) # [111, 55, 7, 2, 1, 4]

# ? extend()
numbers.extend([33, 44]) # * Add 33 and 44 to the end of the list
print(numbers) # [111, 55, 7, 2, 1, 4, 33, 44]

# ? remove()
numbers.remove(33) # * Remove the first occurrence of 33
print(numbers) # [111, 55, 7, 2, 1, 4, 44]

# ? clear()
numbers.clear() # * Remove all elements
print(numbers) # []

# ? index()
numbers = [111, 55, 7, 2, 1, 4, 44] 
print(numbers.index(7)) # 2 --> index of value 7

# ? count()
print(numbers.count(7)) # 1 --> 7 appears once in the list

# ? sort()
numbers.sort()
print(numbers) # [1, 2, 4, 7, 44, 55, 111]

# ? reverse()
numbers.reverse() # * Reverse the list
print(numbers) # [111, 55, 44, 7, 4, 2, 1]

# ? List filled using a loop
numbers = []
for i in range(5):
    numbers.append(i) # Appending elements to the list.
print(numbers) # [0, 1, 2, 3, 4]

my_list = []  # Creating an empty list.
 
for i in range(5):
    my_list.insert(0, i + 1) # Inserting elements at index 0.
 
print(my_list)  # [5, 4, 3, 2, 1]

# ? Making use of lists
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)): 
    total += my_list[i] #  Adding each element to the total

print(total) # 27

# ? The second aspect of the FOR loop
my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list: #  Iterating through the list
    total += i # Adding each element to the total

print(total) # 27

# ? Swapping elements in a list without using a temporary variable
my_list = [10, 1, 8, 3, 5]
my_list[0], my_list[1] = my_list[1], my_list[0]
print(my_list) # [1, 10, 8, 3, 5]

length = len(my_list)
for i in range(length // 2): # Iterating through the first half of the list
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i] # Swapping elements

print(my_list) # [5, 3, 8, 10, 1]



# TODO Section Summary


my_list = [1, None, True, "I am a string", 256, 0]

print(my_list[3])  # outputs: I am a string
print(my_list[-1])  # outputs: 0

my_list[1] = '?'
print(my_list)  # outputs: [1, '?', True, 'I am a string', 256, 0]

my_list.insert(0, "first")
my_list.append("last")
print(my_list)  # outputs: ['first', 1, '?', True, 'I am a string', 256, 0, 'last']

my_list = [1, 'a', ["list", 64, [0, 1], False]] # nested list

my_list = [1, 2, 3, 4]
del my_list[2] # deletes the element at index 2
print(my_list)  # outputs: [1, 2, 4]

del my_list  # deletes the whole list

my_list = ["white", "purple", "blue", "yellow", "green"]

for color in my_list:
    print(color)

# ? Quiz 1
lst = [1, 2, 3, 4, 5]
lst.insert(1, 6) # inserts 6 at index 1 not replacing the element at index 1
del lst[0] # deletes the element at index 0
lst.append(1) # appends 1 to the end of the list

print(lst) # outputs: [6, 2, 3, 4, 5, 1]

# ? Quiz 2
lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0

for number in lst:
    add += number # adds the elements of the list
    lst_2.append(add) # adds the sum of the elements to the new list

print(lst_2) # outputs: [1, 3, 6, 10, 15]

# ? Quiz 3
lst = [1, [2, 3], 4]
print(lst[1]) # outputs: [2, 3]
print(len(lst))  # outputs: 3


""" 
A typical function invocation looks as follows: result = function(arg), while a typical method invocation looks like this:result = data.method(arg).
"""
