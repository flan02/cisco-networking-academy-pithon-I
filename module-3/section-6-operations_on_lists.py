
# $ OPERATIONS IN LISTS
"""
Now we want to show you one important, and very surprising, feature of lists, which strongly distinguishes them from ordinary variables.

We want you to memorize it ‒ it may affect your future programs, and cause severe problems if forgotten or overlooked. 
"""
list_1 = [1]        # ? list_1 is a list with one element
list_2 = list_1     # ? list_2 is a reference to list_1
list_1[0] = 2       # ? list_1 is modified
print(list_2) # [2] # ? list_2 is also modified

""" 
The surprising part is the fact that the program will output: [2], not [1], which seems to be the obvious solution.

Lists (and many other complex Python entities) are stored in different ways than ordinary (scalar) variables.
"""

# $ You could say that:
# $ the name of an ordinary variable is the name of its content;
# $ the name of a list is the name of a memory location where the list is stored.

""" 
The assignment: list_2 = list_1 copies the name of the array, not its contents. In effect, the two names (list_1 and list_2) identify the same location in the computer memory. Modifying one of them affects the other, and vice versa.
"""

# TODO How do you cope with that?
# $ POWERFUL SLICES
""" 
Fortunately, the solution is at your fingertips ‒ it's called a slice.
A slice is an element of Python syntax that allows you to make a brand new copy of a list, or parts of a list.
It actually copies the list's contents, not the list's name.
"""

list_1 = [1]
list_2 = list_1[:] # slice creates a new list [:]
list_1[0] = 2
print(list_2)

""" 
One of the most general forms of the slice looks as follows:
my_list[start:end]

start is the index of the first element included in the slice;
end is the index of the first element not included in the slice.
"""

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3] # Take elements from index 1 to 3 (exclusive)
# ? end - start = 3 - 1 = 2. Two elements will be taken
print(new_list) # [8, 6]


# TODO Copying the entire list.
print("Copying the entire list.")
list_1 = [1]
list_2 = list_1[:] # ? list_2 is a copy of list_1
list_1[0] = 2 # ? list_1 is modified but list_2 is not
print(list_2) # [1]

# TODO Copying some part of the list.
print("Copying some part of the list.")
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3] # ? new_list is a copy of the elements from index 1 to 3 (exclusive)
print(new_list) # [8, 6]


# $ Slices - negative indices
# This is how negative indices work with the slice
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1] # ? new_list is a copy of the elements from index 1 to -1 (exclusive)
print("Slices - negative indices")
print(new_list) # [8, 6, 4]


my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1] 
print(new_list) # [] # ? empty list because -1 is greater than 1


""" 
If you omit the start in your slice, it is assumed that you want to get a slice beginning at the element with index 0.
In other words, the slice of this form:

my_list[:end]
"""

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3] # Take elements from index 0 to 3 (exclusive)
print(new_list) # [10, 8, 6] # ? new_list is a copy of the elements from index 0 to 3 (exclusive)

"""
Similarly, if you omit the end in your slice, it is assumed that you want the slice to end at the element with the index len(my_list).
In other words, the slice of this form:

my_list[start:] 
"""

my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:] # Take elements from index 3 to the end [len(my_list)]
print(new_list) # [4, 2] # ? new_list is a copy of the elements from index 3 to the end

""" 
As we've said before, omitting both start and end makes a copy of the whole list [:]
"""
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(new_list) # [10, 8, 6, 4, 2] # ? new_list is a copy of the whole list

# $ MORE ABOUT DEL INSTRUCTION
my_list = [10, 8, 6, 4, 2]
del my_list[1:3] # In this case the slice doesn't produce any new list
print(my_list) # [10, 4, 2] # ? delete elements from index 1 to 3 (exclusive)

# Deleting all the elements at once is possible too
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list) # [] # ? delete all elements


# $ The IN and NOT IN operators
""" 
Python offers two very powerful operators, able to look through the list in order to check whether a specific value is stored inside the list or not.
"""

""" 
IN: The first of them (in) checks if a given element (its left argument) is currently stored somewhere inside the list (the right argument) ‒ the operator returns True in this case.

NOT IN: The second (not in) checks if a given element (its left argument) is absent in a list ‒ the operator returns True in this case.
"""

my_list = [0, 3, 12, 8, 2]
print("number 5 is in my_list", 5 in my_list) # ? False
print("number 5 is not in my_list", 5 not in my_list) # ? True
print("number 12 is in my_list", 12 in my_list) # ? True


# $ Lists - some simple programs

# TODO The first of them tries to find the greater value in the list.
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest) # * 17

# ? Same concept but using FOR loop
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i

print(largest) # * 17

# If you need to save computer power, you can use a slice:
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list[1:]:
    if i > largest:
        largest = i

print(largest)


# TODO Now let's find the location of a given element inside a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Element found at index", i) # * Element found at index 4
else:
    print("absent") # * absent


# TODO Lottery
""" 
Let's assume that you've chosen the following numbers in the lottery: 3, 7, 11, 42, 34, 49.
The numbers that have been drawn are: 5, 11, 9, 42, 3, 49.
The question is: how many numbers have you hit?
"""

drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits) # * 4


# TODO Labs Operating with lists
""" 
Imagine a list ‒ not very long, not very complicated, just a simple list containing some integer numbers. Some of these numbers may be repeated, and this is the clue. We don't want any repetitions. We want them to be removed.

Your task is to write a program which removes all the number repetitions from the list. The goal is to have a list in which all the numbers appear not more than once.

Note: assume that the source list is hard-coded inside the code ‒ you don't have to enter it from the keyboard. Of course, you can improve the code and add a part that can carry out a conversation with the user and obtain all the data from her/him.

Hint: we encourage you to create a new list as a temporary work area ‒ you don't need to update the list in situ.

We've provided no test data, as that would be too easy. You can use our skeleton instead.
"""
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9] # | Skeleton provided
unique_list = [] # | Create a new list to store unique elements

# Iterate over the list
for number in my_list:
    if number not in unique_list: # If the number is not in the unique_list, add it
        unique_list.append(number)

print("The list with unique elements only:")
print(unique_list) # | [1, 2, 4, 6, 9]


# ? Quizzes

# Question 1: What is the output of the following snippet?
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[0]

print(list_3) # | ["C"]

# Question 2: What is the output of the following snippet?
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0] # This will remove the first element from list_1
del list_2 # This will remove the reference to list_1 but list_3 still has a reference to list_1 with the first element removed

print(list_3) # | ["B", "C"]


# Question 3: What is the output of the following snippet?
list_1 = ["A", "B", "C"]
list_2 = list_1 # list_2 is a reference to list_1
list_3 = list_2 # list_3 is a reference to list_2
 
del list_1[0] # This will remove the first element from list_1
del list_2[:] # This will remove all elements from list_2
 
print(list_3) # | []


# Question 4: What is the output of the following snippet?
list_1 = ["A", "B", "C"]
list_2 = list_1[:] # list_2 is a copy of list_1
list_3 = list_2[:] # list_3 is a copy of list_2

del list_1[0] # This will remove the first element from list_1
del list_2[0] # This will remove the first element from list_2

print(list_3) # | ["A", "B", "C"]


# Question 5: Insert in or not in instead of ??? so that the code outputs the expected result.

my_list = [1, 2, "in", True, "ABC"]

print(1 in my_list)  # outputs True
print("A" not in my_list)  # outputs True
print(3 not in my_list)  # outputs True
print(False not in my_list)  # outputs False

