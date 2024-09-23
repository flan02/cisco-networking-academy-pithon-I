
# TODO: TUPLES & DICTIONARIES
""" 
The first and the clearest distinction between lists and tuples is the syntax used to create them - tuples prefer to use parenthesis, whereas lists like to see brackets, although it's also possible to create a tuple just from a set of values separated by commas.
"""
tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125
print(tuple_1)
print(tuple_2)

# - How to create a TUPLE ?
empty_tuple = ()

""" 
if you want to create a tuple containing a single value, you have to remember to put a comma after the value, like this:
"""
single_tuple = (1, )
single_tuple = 1., 
""" 
Removing the commas won't spoil the program in any syntactical sense, but you will instead get two single variables, not tuples.
"""

# - How to use a TUPLE ?
""" 
If you want to get the elements of a tuple in order to read them over, you can use the same conventions to which you're accustomed while using lists.
"""
my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print("Printing from loop...", elem) # 1, 10, 100, 1000

""" 
! The similarities may be misleading − don't try to modify a tuple's contents! It's not a list!
"""

# - What else can tuples do for you ?
""" 
- the len() function accepts tuples, and returns the number of elements contained inside;
- the + operator can join tuples together (we've shown you this already)
- the * operator can multiply tuples, just like lists;
- the in and not in operators work in the same way as in lists.
"""
# ? Example
my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2)) # 9
print(t1)  # (1, 10, 100, 1000, 10000)
print(t2)  # (1, 10, 100, 1, 10, 100, 1, 10, 100)
print(10 in my_tuple) # True
print(-10 not in my_tuple) # True

""" 
TODO: One of the most useful tuple properties is their ability to appear on the left side of the assignment operator. You saw this phenomenon some time ago, when it was necessary to find an elegant tool to swap two variables' values.
"""
var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3) # (2,) (3, 123) (1,)


""" 
? Note: the example presents one more important fact: a tuple's elements can be variables, not only literals. Moreover, they can be expressions if they're on the right side of the assignment operator.
"""
""" 
TODO: EXTRA -> You can also create a tuple using a Python built-in function called tuple(). This is particularly useful when you want to convert a certain iterable (list, string, range, etc.) into a tuple.
"""
my_tuple = tuple((1, 2, "string")) 
print(my_tuple) 

my_list = [2, 4, 6]
print(my_list)    # outputs: [2, 4, 6]
print(type(my_list))    # outputs: <class 'list'>
tup = tuple(my_list)   # | convert the list to a tuple
print(tup)    # outputs: (2, 4, 6)
print(type(tup))    # outputs: <class 'tuple'>







# - DICTIONARIES
""" 
The dictionary is another Python data structure. It's not a sequence type (but can be easily adapted to sequence processing) and it is mutable.

To explain what the Python dictionary actually is, it is important to understand that it is literally a dictionary.
"""

# - How to create a DICTIONARY ?
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}
 
print(dictionary) # {'cat': 'chat', 'dog': 'chien', 'horse': 'cheval'}
print(phone_numbers) # {'boss': 5551234567, 'Suzy': 22657854310}
print(empty_dictionary) # {}
# ? Note: This means that a dictionary is a set of key-value pairs.

""" 
each key must be unique − it's not possible to have more than one key of the same value;
a key may be any immutable type of object: it can be a number (integer or float), or even a string, but not a list;
a dictionary is not a list − a list contains a set of numbered values, while a dictionary holds pairs of values;
the len() function works for dictionaries, too − it returns the number of key-value elements in the dictionary;
a dictionary is a one-way tool − if you have an English-French dictionary, you can look for French equivalents of English terms, but not vice versa.
"""

""" 
! First of all, it's a confirmation that dictionaries are not lists - they don't preserve the order of their data, as the order is completely meaningless (unlike in real, paper dictionaries). The order in which a dictionary stores its data is completely out of your control, and your expectations. That's normal. (*)
"""

# - How to use a DICTIONARY ?
print(dictionary['cat']) # chat
print(phone_numbers['Suzy']) # 22657854310
""" 
if the key is a string, you have to specify it as a string;
keys are case-sensitive: 'Suzy' is something different from 'suzy'.
"""

# ? Example

# $ hanging indent. It's a good practice to use it when you have a long line of code.
dictionary = {
    "cat": "chat", 
    "dog": "chien", 
    "horse": "cheval"
    }
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word]) # cat -> chat, horse -> cheval
    else:
        print(word, "is not in dictionary") # lion is not in dictionary


# - DICTIONARY METHODS AND FUNCTIONS

# ? The keys() method returns a list of all keys in the dictionary.

""" 
Can dictionaries be browsed using the for loop, like lists or tuples?
No and yes.

No, because a dictionary is not a sequence type − the for loop is useless with it.
Yes, because there are simple and very effective tools that can adapt any dictionary to the for loop requirements (in other words, building an intermediate link between the dictionary and a temporary sequence entity).

The first of them is a method named keys(), possessed by each dictionary. The method returns an iterable object consisting of all the keys gathered within the dictionary. Having a group of keys enables you to access the whole dictionary in an easy and handy way.
"""

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key]) # cat -> chat, dog -> chien, horse -> cheval


""" 
TODO: Let's now have a look at a dictionary method called items(). The method returns tuples (this is the first example where tuples are something more than just an example of themselves) where each tuple is a key-value pair.
"""
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for english, french in dictionary.items():
    print(english, "->", french) # cat -> chat, dog -> chien, horse -> cheval


# - How to modify a DICTIONARY ?
""" 
Assigning a new value to an existing key is simple - as dictionaries are fully mutable, there are no obstacles to modifying them.

We're going to replace the value "chat" with "minou", which is not very accurate, but it will work well with our example.
"""
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['cat'] = 'minou' # | replacing the value
print(dictionary) # {'cat': 'minou', 'dog': 'chien', 'horse': 'cheval'}

# ? Do you want it sorted? Just enrich the for loop to get such a form:
for key in sorted(dictionary.keys()):
    print(key, "->", dictionary[key]) # cat -> minou, dog -> chien, horse -> cheval


# - Values method
""" 
There is also a method called values(), which works similarly to keys(), but returns values.
"""
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for french in dictionary.values():
    print(french) # chat, chien, cheval


# - How to add a new key in a DICTIONARY ?
""" 
Adding a new key-value pair to a dictionary is as simple as changing a value – you only have to assign a value to a new, previously non-existent key.

? Note: this is very different behavior compared to lists, which don't allow you to assign values to non-existing indices.
"""
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['swan'] = 'cygne' # | adding a new key-value pair
print(dictionary) # {'cat': 'chat', 'dog': 'chien', 'horse': 'cheval', 'swan': 'cygne'}

# TODO: You can also insert an item to a dictionary by using the update() method.
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary.update({"duck": "canard"}) # - I really prefer this method
print(dictionary)


# - How to remove a key from a DICTIONARY ?
""" 
Can you guess how to remove a key from a dictionary?

Note: removing a key will always cause the removal of the associated value. Values cannot exist without their keys.

This is done with the del instruction.
"""
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

del dictionary['dog'] # | removing an item with a specific key
print(dictionary) # {'cat': 'chat', 'horse': 'cheval'}


# TODO: to remove a last item from a dictionary, you can use the popitem() method.
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary.popitem() # | removing the last item
print(dictionary)    # outputs: {'cat': 'chat', 'dog': 'chien'} 



# TODO: Tuples and Dictionaries can work together
""" 
Let's imagine the following problem:

you need a program to evaluate the students' average scores;
the program should ask for the student's name, followed by her/his single score;
the names may be entered in any order;
entering an empty name finishes the inputting of the data (note 1: entering an empty score will raise the ValueError exception, but don't worry about that now, you'll see how to handle such cases when we talk about exceptions in the second part of the Python Essentials course series)
a list of all names, together with the evaluated average score, should be then emitted.
"""
school_class = {} # | an empty dictionary

while True:
    name = input("Enter the student's name: ")
    if name == '':
        break
    
    score = int(input("Enter the student's score (0-10): "))
    if score not in range(0, 11):
	    break
    
if name in school_class:
        school_class[name] += (score,) # | adding a new score in a tuple
else:
        school_class[name] = (score,) # | adding a new student
        
for name in sorted(school_class.keys()): # | sorting the names
    adding = 0
    counter = 0
    for score in school_class[name]: # | summing up the scores
        adding += score
        counter += 1
    print(name, ":", adding / counter) # outputs: name : average score


# ? Quizzes
my_tup = (1, 2, 3)
print(my_tup[2]) # 3

tup = 1, 2, 3
a, b, c = tup

print(a * b * c) # 6


tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2) # | counting the number of 2s

print(duplicates) # 4


d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    # | merging the dictionaries
    d3.update(item)

print(d3) # {'Adam Smith': 'A', 'Judy Paxton': 'B+', 'Mary Louis': 'A', 'Patrick White': 'C'}



my_list = ["car", "Ford", "flower", "Tulip"]

t = tuple(my_list) # | converting the list to a tuple
print(t) # ('car', 'Ford', 'flower', 'Tulip')


colors = (("green", "#008000"), ("blue", "#0000FF")) # | a tuple of tuples

colors_dictionary = dict(colors) # | converting the tuple to a dictionary
print(colors_dictionary) # {'green': '#008000', 'blue': '#0000FF'}



my_dictionary = {"A": 1, "B": 2}
copy_my_dictionary = my_dictionary.copy() # | copying the dictionary
my_dictionary.clear() # | clearing the dictionary

print(copy_my_dictionary) # {'A': 1, 'B': 2}
print(my_dictionary) # {}



colors = {
    "white": (255, 255, 255),
    "grey": (128, 128, 128),
    "red": (255, 0, 0),
    "green": (0, 128, 0)
    }

for col, rgb in colors.items():
    print(col, ":", rgb) # white : (255, 255, 255), grey : (128, 128, 128), red : (255, 0, 0), green : (0, 128, 0)

