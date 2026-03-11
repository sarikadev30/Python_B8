# b = 10
# b %= 4
# b *= 2
# print(b)  # N-4
# .............................................................
# Membership Operator

# in
# x = "How are you?"
# txt = "Are"
# print(txt in x)

# xy = [23, 34, 45, 12, 34, 56]
# val = 34
# print(34 in xy)

# not in

# print(txt not in x)
# print(34 not in xy)
# ...........................................................
# SWAP TWO Numbers

# a = 23
# b = 45

# print(a, b)
# c = a  # c=> 23
# a = b  # a=> b => 45
# b = c  # b=> c => 23
# print(a, b)

# a = 23
# b = 45
# print(a, b)

# a = a + b  # a => 68
# b = a - b  # 68 - b => 68 - 45 => 23 => b
# a = a - b  # 68 - b =>68 -23 => 45 => a

# print(f"Swapped values a= {a} and b= {b}")

# a = 23
# b = 45
# c = 78
# print(a, b, c)

# a, b, c = b, c, a
# print(a, b, c)
# ....................................................

# greeting = "good morning"
# print("good" in greeting)
# print("Good" in greeting)
# print("night" not in greeting)

# ....................................................................
# Identity Operators

# is
# a = 100
# b = 100
# print(a is b)

# x = "hello"
# y = "hello"
# s = "hello"
# print(x is y)
# print(x is s)
# print(y is s)

# z = "hello world"[0:5]
# print(x == z)
# print(x is z)  # F
# .............................................

# constant reuse => compile time optimization
# x = 360
# y = 360
# print(x is y)  # False → different memory locations

# ....................................................................
# Conditional Statements

# if
# x = -78

# print("Start")

# if x > 0:
#     print("Positive Integer...")
#     print("Hello Integer")


# print("End")
# ........................................................
# Multiple of 5

# num = int(input("Enter a Number: "))
# print(num, type(num))

# if num % 5 == 0:
#     print(f"Yes, {num} is a multiple of 5")

# ........................................................
# Print "Its Hot!..." if the temperature is above 40 and if not print "Its OK"


# if-else
# num = int(input("Enter a Number: "))
# print(num, type(num))

# if num % 5 == 0:
#     print(f"Yes, {num} is a multiple of 5")
# else:
#     print(f"No, {num} is not a multiple of 5")

# print("End")


# .......................................................
# Print "In Range" if the number is in between 20 and 30 else print "Not in Range".
# num = 34
# if num > 20 and num < 30:
#     print("In Range")
# else:
#     print("Not in Range")

# ...............................................................
# if-elif-else
# num = 0
# is num +ve -ve or zero

# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero...")

# ...........................................
# Print "In Range" if the number is in between 20 and 30
# else if number < 20 Print"Below"
# else if number is > 30 Print "Above"
# else print "Equals to 20 or 30".

# ...........................................................
# Nested - If
# if condition:
#     if condition :

# Voting Eligibility with ID Check
# Voting age in India is 18. Voter must also have a voter ID.

# age = int(input("Enter your age: "))
# if age >= 18:
#     isID = input("Do you have voter id ?(yes/no): ").lower()
#     print(isID)
#     # Yes yes YES
#     if isID == "yes":
#         print("You are Eligible")
#     else:
#         print("Not Eligible")
# else:
#     print("Not Eligible")

# Problem 1: Login System
# Problem Statement:
# Write a login system that checks if the username and password are correct.
# Sample Input:
# Username: admin
# Password: 1234
# Sample Output: Login Successful
# .....................................................................
# Problem 1
# - My mother told me to get all of the things if available from the market
# 1. If Rice is available then print Buy rice
# 2. If wheat is available then print buy wheat
# 3. If apple is available then print buy apple

# .....................................................................
# Problem 2
# - My mother told me to get any one of the things from the market
# 1. If Rice is available then print Buy rice
# 2. Else If wheat is available then print buy wheat
# 3. Else If apple is available then print buy apple
# .......................................................................
# Check the number is divisible by both 5 and 7
