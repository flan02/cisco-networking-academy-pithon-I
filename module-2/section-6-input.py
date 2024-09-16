
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

