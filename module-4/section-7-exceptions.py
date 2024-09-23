
# - Errors
# ? When data is not what it should be
value = int(input('Enter a natural number: '))
print('The reciprocal of', value, 'is', 1/value) # ? ZeroDivisionError: division by zero

type(value) is int # ? True


# - The try-except branch
""" 
In the Python world, there is a rule that says: "It’s better to beg for forgiveness than to ask for permission".

Let's stop here for a moment. Don't get us wrong – we don't want you to apply the rule in your everyday life. Don't take anyone's car without permission in the hope that you can be so convincing that you will avoid conviction. The rule is about something else.

Actually, the rule reads: "it's better to handle an error when it happens than to try to avoid it".

"Okay," you may say now, 'but how should I beg for forgiveness when the program is terminated and there is nothing left that can be done?" This is where the exception comes on the scene.
"""
try:
	# It's a place where you can do something without asking for permission.
  {}
except:
	# It's a spot dedicated to solemnly begging for forgiveness.
  {}

try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except:
    print('I do not know what to do.')


# - Implementing more than one except branch
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError: 
    print('I do not know what to do.')    
except ZeroDivisionError: 
    print('Division by zero is not allowed in our Universe.') 
except: # | Default except must be at the end.
    print('Something strange has happened here... Sorry!')


# ? Some useful exceptions
#  ZeroDivisionError
#  ValueError
#  TypeError
#  NameError
#  IndexError
#  AttributeError
#  SyntaxError

# - Bug vs Debugging
# ? Bug: An error in a program that makes it do something unexpected.
# ? Debugging: The process of finding and fixing bugs.
# TODO Know more about the IDLE debugger: https://docs.python.org/3/library/idle.html


# - Unit testing – a higher level of coding
""" 
There is also one important and widely used programming technique that you will have to adopt sooner or later during your developer career – it's called unit testing. The name may a bit confusing, as it's not only about testing the software, but also (and most of all) about how the code is written.

To make a long story short – unit testing assumes that tests are inseparable parts of the code and preparing the test data is an inseparable part of coding. This means that when you write a function or a set of cooperating functions, you're also obliged to create a set of data for which your code's behavior is predictable and known.

Moreover, you should equip your code with an interface that can be used by an automated testing environment. In this approach, any amendment made to the code (even the least significant) should be followed by the execution of all the unit tests accompanied by your source.

To standardize this approach and make it easier to apply, Python provides a dedicated module named unittest. We're not going to discuss it here – it's a broad and complex topic.

Therefore, we’ve prepared a separate course and certification path for this subject. It is called “Testing Essentials with Python”, and we invite you to participate in it.
"""