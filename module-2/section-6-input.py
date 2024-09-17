
# TODO input() function

print("Tell me anything...")
anything = input() # * When I run the program, it will wait for me to type something and press enter
print("Hmm...", anything, "... Really?") # * This will print the input from the user

anything = input("Tell me anything...")
print("Hmm...", anything, "...Really?")

anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)

fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")

print("+" + 10 * "-" + "+") # * This will print +----------+

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

string_to_number = str(4)
print(string_to_number)


# TODO -> LAB Simple input and output
""" 
Your task is to complete the code in order to evaluate the results of four basic arithmetic operations.
The results have to be printed to the console.
"""
a = float(input("Enter first value: "))
b = float(input("Enter second value: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("\nThat's all, folks!")

x = 10
y = 1 / (x+1/(x+1/(x+1/x))) # 0.09901951266867294
print("y =", y)

# TODO -> LAB Operators and expressions
""" 
Your task is to prepare a simple code able to evaluate the end time of a period of time, given as a number of minutes (it could be arbitrarily large). The start time is given as a pair of hours (0..23) and minutes (0..59). The result has to be printed to the console.
For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.
"""
hour = int(input("Starting time (hours): ")) # * 12
mins = int(input("Starting time (minutes): ")) # * 17
dura = int(input("Event duration (minutes): ")) # * 59
mins = mins + dura # find a total of all minutes
hour = hour + mins // 60 # find a number of hours hidden in minutes and update the hour
mins = mins % 60 # correct minutes to fall in the (0..59) range
hour = hour % 24 # correct hours to fall in the (0..23) range
print(hour, ":", mins, sep='') # * 13:16