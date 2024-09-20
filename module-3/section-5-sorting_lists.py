
# $ The bubble sort
""" 
Now that you can effectively juggle the elements of lists, it's time to learn how to sort them. Many sorting algorithms have been invented so far, which differ a lot in speed, as well as in complexity. We are going to show you a very simple algorithm, easy to understand, but unfortunately not too efficient, either. It's used very rarely, and certainly not for large and extensive lists.

Let's say that a list can be sorted in two ways:

increasing (or more precisely ‒ non-decreasing) ‒ if in every pair of adjacent elements, the former element is not greater than the latter;
decreasing (or more precisely ‒ non-increasing) ‒ if in every pair of adjacent elements, the former element is not less than the latter.
"""

# TODO The bubble sort algorithm (decreasing order) 
my_list = [8, 10, 6, 2, 4]  # list to sort

for i in range(len(my_list) - 1):  # we need (5 - 1) comparisons
    if my_list[i] > my_list[i + 1]:  # compare adjacent elements
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # If we end up here, we have to swap the elements.

print(my_list)  # [8, 6, 2, 4, 10]

# TODO The bubble sort algorithm (increasing order)
my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.

while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list) # [2, 4, 6, 8, 10]

# $ The bubble sort - the final version
"""
The bubble sort algorithm can be optimized a little bit. If we look at the list after the first pass, we can see that the largest element is already at the end of the list. We don't need to compare it anymore. The same goes for the second largest element after the second pass, and so on. We can use this fact to reduce the number of comparisons in each pass. We can also stop the algorithm if no swaps were made in the last pass, as this means that the list is already sorted.
"""

my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.
length = len(my_list) - 1  # We must define the length.

while swapped:
    swapped = False  # no swaps so far
    for i in range(length):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    length -= 1  # the last element is already sorted

print(my_list)  # [2, 4, 6, 8, 10]


# $ The bubble sort – interactive version

my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)

# $ Python's built-in sorting function
""" 
Python provides a built-in function called sorted() which can be used to sort lists. The function takes a list as an argument and returns a new list with the elements sorted in increasing order. The original list remains unchanged.
"""

my_list = [8, 10, 6, 2, 4]  # list to sort
new_list = sorted(my_list)  # ? sorted() returns a new list
print(new_list)  # [2, 4, 6, 8, 10]

# $ Sorting in decreasing order
"""
The sorted() function has an optional argument reverse which can be set to True to sort the list in decreasing order.
"""

my_list = [8, 10, 6, 2, 4]  # list to sort
new_list = sorted(my_list, reverse=True)  # ? sorted() returns a new list
print(new_list)  # [10, 8, 6, 4, 2]


a = 3
b = 1
c = 2

lst = [a, c, b]
lst.sort()

print(lst) # [1, 2, 3]



# $ Sorting strings
lst = [" ", "D", "F", "A", "Z"]
lst.sort() # ? sort() modifies the list in place
print(lst) # [' ', 'A', 'D', 'F', 'Z']

# $ Sorting strings in decreasing order
lst = ["D", "F", "A", "Z"]
lst.sort(reverse=True) # ? sort() modifies the list in place
print(lst) # ['Z', 'F', 'D', 'A']

# $ Sorting strings using the sorted() function
lst = ["D", "F", "A", "Z"]
new_lst = sorted(lst) # ? sorted() returns a new list
print(new_lst) # ['A', 'D', 'F', 'Z']

# $ Sorting strings in decreasing order using the sorted() function
lst = ["D", "F", "A", "Z"]
new_lst = sorted(lst, reverse=True) # ? sorted() returns a new list
print(new_lst) # ['Z', 'F', 'D', 'A']

# $ Sorting lists of lists
lst = [[3, 4], [1, 2], [5, 6]]
lst.sort() # ? sort() modifies the list in place
print(lst) # [[1, 2], [3, 4], [5, 6]]

# $ Sorting lists of lists in decreasing order
lst = [[3, 4], [1, 2], [5, 6]]
lst.sort(reverse=True) # ? sort() modifies the list in place
print(lst) # [[5, 6], [3, 4], [1, 2]]

# $ Sorting lists of lists using the sorted() function
lst = [[3, 4], [1, 2], [5, 6]]
new_lst = sorted(lst) # ? sorted() returns a new list
print(new_lst) # [[1, 2], [3, 4], [5, 6]]

# $ Sorting lists of lists in decreasing order using the sorted() function
lst = [[3, 4], [1, 2], [5, 6]]
new_lst = sorted(lst, reverse=True) # ? sorted() returns a new list
print(new_lst) # [[5, 6], [3, 4], [1, 2]

# $ Sorting lists of lists by the second element
lst = [[3, 4], [1, 2], [5, 6]]
lst.sort(key=lambda x: x[1]) # ? sort() modifies the list in place
print(lst) # [[1, 2], [3, 4], [5, 6]]

# $ Sorting lists of lists by the second element in decreasing order
lst = [[3, 4], [1, 2], [5, 6]]
lst.sort(key=lambda x: x[1], reverse=True) # ? sort() modifies the list in place
print(lst) # [[5, 6], [3, 4], [1, 2]]

# $ Sorting lists of lists by the second element using the sorted() function
lst = [[3, 4], [1, 2], [5, 6]]
new_lst = sorted(lst, key=lambda x: x[1]) # ? sorted() returns a new list
print(new_lst) # [[1, 2], [3, 4], [5, 6]]

# $ Sorting lists of lists by the second element in decreasing order using the sorted() function
lst = [[3, 4], [1, 2], [5, 6]]
new_lst = sorted(lst, key=lambda x: x[1], reverse=True) # ? sorted() returns a new list
print(new_lst) # [[5, 6], [3, 4], [1, 2]


