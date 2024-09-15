# TODO Operators

# $    + | - | * | / | // | % | **

print(2 + 2)
print(2. ** 5) # 32.0
print(5 ** 3.) # 125.0

print(2 * 3) # 6
print(2 * 3.) # 6.0

print(6 / 3) # 2.0
print(6 / 3.) # 2.0

print(6 // 4) # 1 (rounding always goes to the lesser integer)
print(6. // 4) # 1.0

print(6 / 4) # 1.5
print(6. / 4) # 1.5

print(-6 // 4) # -2
print(6. // -4) # -2.0

print(14 % 4) # 2 (remainder of the division)
print(12 % 4.5) # 3.0 (remainder of the division)

print(-4 + 4) # 0
print(-4. + 8) # 4.0

print(2 + 3 * 5) # 17 (multiplication first and then addition)

print(9 % 6 % 2) # 1 (9 % 6 = 3 and 3 % 2 = 1)

print(2 ** 2 ** 3) # 256 (2 ** 8 = 256)

print(-3 ** 2) # -9
print(-2 ** 3) # -8
print(-(3 ** 2)) # -9

print(2 * 3 % 5) # 1 (2 * 3 = 6 and 6 % 5 = 1)

print((5 * ((25 % 13) + 100) / (2 * 13)) // 2) # 10.0 (5 * (12 + 100) / 26) // 2 = 10.0
    