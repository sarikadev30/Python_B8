# String Concatination

# x = 34
# y = 56
# print(x + y)

# a = "Hi!.."
# b = "Sam."
# c = "I am fine"
# print(a + b + c)

# .......................................................
# Comparison Operators

# a = 45
# b = 23
# print(a > b)
# print(a >= b)
# print(10 >= 10)
# print(a < b)
# print(a <= b)
# print(a == b)
# print(a != b)

# ........................

# ram = "ram"
# print(5 == 5)
# print("dam" == "dam")
# print(5 == "5")
# print(ram == "ram")
# print(5 == "ram")
# print(5 != 5)
# print(6 == "6")
# print(6 != "6")
# print(6 != 7)
# .................................
# fan = 5
# a = "fan"
# b = fan
# print(a == b)  # P-False
# print(a != b)  # P-True
# .................................
# Problem 1:
# age_of_ram = 25; age_of_mohan = 30;
# Check whether the Ram age is greater than Mohan or not.

# age_of_ram = 25
# age_of_mohan = 30
# print(age_of_ram > age_of_mohan)
# .................................
# Problem 2:
# sunil_marks = 36; passing_marks = 35;
# Check whether Sunil is passed or not, where the passing mark is 35
# sunil_marks = 33
# passing_marks = 33
# print(sunil_marks >= passing_marks)
# ..................................
# Problem 3:
# sunil_marks = 34; passing_marks = 35;
# Check whether Sunil failed or not, where the passing mark is 35
# sunil_marks = 34
# passing_marks = 35
# print(sunil_marks < passing_marks)
# ..................................
# Problem 4:
# Those customers will be eligible for the amazon discount
# whose spending is equal to or above 4000.
# Check whether a customer Sam is eligible for a discount or not
# Sam_Spendings = 4500
# print(Sam_Spendings >= 4000)


# ........................................................................
# Problem 5:
# Check whether Danny is eligible for driving a vehicle in India => 18
# Danny_age = 19

# print(Danny_age >= 18)
# ...........................................................................

# Problem 6:
a = 5
b = 6
c = "6"
d = -2
e = "m"
# print(b == c)  # F
# print(c == e)  # F
# print(a >= c)  # Error
# print(d <= a)  # T
# print(b != c)
# print(3.0 == 3)  # Implicit Typecasting
# ...........................................................................
# Check if the Number is Positive.
# x = -23
# print(x > 0)
# .......................................................
# Check the number is Even or not
# a = 24
# print(a%2 == 0)

# .......................................................
#  Check the number is Odd or not
# a = 24
# print(a % 2 != 0)
# print(a % 2 == 1)
# .......................................................
# Check the Number is divisible by 3
# a = 22
# print(a % 3 == 0)
# .....................................................................
# Logical Operators
# AND => True only when all are True

# print(True and True)
# print(False and True)
# print(True and False)
# print(False and False)
# print(True and True and True)

# a = True
# b = False
# print(a and b)  # F

# p = 3 > 5
# q = 9 >= 8
# print(p and q)  # F
# ...................................................................

# OR => True when anyone is True

# print(True or True)
# print(False or True)
# print(True or False)
# print(False or False)
# print(True or True or True)

# ...................................................................
# NOT => It will change to the opposite value

# print(not True)
# print(not False)
# ...................................................................
# Problem :
# a = 9 < 11   # T
# b = 2 == 3   # F
# c = 10 > 3   # T
# result = a and (b or c)
# print(result)
# ...................................................................
# x = 4 <= 4
# y = 10 < 5
# z = not (x and y)
# print(z)
# .................................................................

# m = 0 != 0
# n = 1 == 1
# o = m and not n
# print(o)
# .................................................................

# p = 6 == 6
# q = 5 != 5
# r = not (p or q)
# print(r)

# .................................................................

# p = 10 < 5
# q = 3 == 3
# r = 7 != 7
# result = not (p or q and r)
# print(result)
# ............................................................................
# Assignment Operators

# a = 2
# print(a)

# a += 2  # a = a + 2
# print(a)

# a -= 1  # a = a - 1
# print(a)

# a *= 2  # a = a * 2
# print(a)

# a /= 2  # a = a / 2
# print(a)

# a %= 2  # a = a % 2
# print(a)

# b = 89.67
# # print(b // 2)
# b //= 2  # b = b // 2
# print(b)

# a **= 2  # a = a**2   (1.0 * 1.0)
# print(a)
# ...................................................

# x = 8
# x *= 2
# x -= 4
# print(x)
# ...................................................
# a = 5
# b = 3
# a %= b
# print(a)
# .................................................
# x = 101
# x -= 25
# x //= 5
# print(x)
# .................................................
# b = 10
# b %= 4
# b *= 2
# print(b)
# ..........................................................................
