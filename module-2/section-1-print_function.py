print("Hello, world!")

print("The itsy spider climbed up the waterspout.")
print("Down came the rain and washed the spider out.")


print("My name is", "Python.", end=" ")  # ? end=" " will keep the cursor on the same line
print("Monty Python.")

print("My", "name", "is", "Monty", "Python.", sep="-")  # ? sep="-" will separate the words with a hyphen

print("My", "name", "is", sep="_", end="*") # ? sep="_" will separate the words with an underscore
print("Monty", "Python.", sep="*", end="*\n") # ? sep="*" will separate the words with an asterisk

# Expected Output:
# * Programming***Essentials***in...Python
print("Programming","Essentials","in", sep="***", end="...")
print("Python")

print("Programming", "\n", "in", "\n", "Python")

# Expected Output: Upper Arrow (avoiding to use many print statements)
print("    *\n   * *\n  *   *\n *     *\n***   ***")
print("  *   *\n  *   *\n  *****")