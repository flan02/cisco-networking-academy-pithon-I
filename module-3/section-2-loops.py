
# TODO While conditional
""" 
A program that reads a sequence of numbers
and counts how many numbers are even and how many are odd.
The program terminates when zero is entered.
"""

odd_numbers = 0 # impar
even_numbers = 0 # par

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number: # ? number != 0:
    # Check if the number is odd.
    if number % 2: # ? number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)


# TODO Loop with a counter
counter = 5
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)


# TODO Lab -> Guess the secret number
secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

user_number = int(input("Which is the secret number: "))
while user_number != secret_number:
    user_number = int(input("Try again. Which is the number? : "))
print("You got the correct number!")


# TODO Looping your code with FOR
i = 0
while i < 10:  # * While way
    print("hello ollie")
    i += 1

for i in range(10): # * For way
    print("The value of i is currently", i)

for i in range(2, 8): # * Range fc is equipped with two arguments [from 2, to 8] 
    print("The value of i is currently", i) 

for i in range(2, 8, 3): # * this fc also accept three args [from 2, to 8, amount of increment]
    print("The value of i is currently", i)
# $ NOTE Second arg must be greater that First arg in Range fc.


# TODO Doing operations at each loop
power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2


# TODO Mississippi
for i in range(5):
    print(i+1, "Mississippi")
print("Ready of not, here I come!")


# TODO Break and Continue statement

# ? break - example
print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")

# ? continue - example
print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")


# TODO Lab -> get the largest number
largest_number = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to end the program: "))

if counter:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")


# TODO While - Else branch
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i) # returns "else 5"

for i in range(5):
    print(i) # returns 0,1,2,3,4
else:
    print("else:", i) # returns "else 4"
