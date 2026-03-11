# Year=1800
# if(Year%400 == 0 or (Year%4 == 0 and Year%100 != 0)):
#     print("Its a Leap year")
# else:
#     print("Its not a Leap year")

# Year%400 == 0 => Year%4 == 0 and Year%100 == 0
# 2000
# 2024
# 1700 NL
# 1900 NL
# 1600
# 2400
# 2800
# ...........................................................
# Ternary Operator

# a = 5
# b = 9
# if a >= b:
#     print("a is greater or equal to b")
# else:
#     print("b is greater than a")

# print("a is greater or equal to b") if a >= b else print("b is greater than a")

# .................................................
# a = 34
# b = 2
# if a % b == 0:
#     print("Divisible")
# else:
#     print("Not divisible")
# .....................................................
# x = 78
# if x > 0:
#     print("Positive ")
# elif x < 0:
#     print("Negative ")
# else:
#     print("Equals to 0 ")

# print("Positive" if x > 0 else "Negative" if x < 0 else "Equals to 0")
# .........................................................................
# LOOPS

# print("Hello World!....")
# print("Hello World!....")
# print("Hello World!....")
# print("Hello World!....")
# print("Hello World!....")
# do-while/ while /for loop

# i = 0
# while i < 5:
#     print("Hello World!...")
#     i += 1

# DRY RUN
# i=0 => 0<5 => T => Hello i=0+1=1
# i=1 => 1<5 => T => Hello i=1+1=2
# i=2 => 2<5 => T => Hello i=2+1=3
# i=3 => 3<5 => T => Hello i=3+1=4
# i=4 => 4<5 => T => Hello i=4+1=5
# i=5 => 5<5 => F .... ENDS
# .....................................................................
# print numbers from 1 to 10 using while loop
# print the sum of numbers from 1 to 10 using while loop
# i = 1
# sum = 0
# while i <= 3:
#     sum += i
#     i += 1
# print(sum)

# dry run
# i=1 sum=0
# i=1 1<=3 => T sum=0+1=1  i=1+1=2
# i=2 2<=3 => T sum=1+2=3  i=2+1=3
# i=3 3<=3 => T sum=3+3=6  i=3+1=4
# i=4 4<=4 => F END...
# 6

# Calculate product of numbers from 1  to 10 using while loop
# Print the sum of all the multiples of 3 from 0 to 40
# print the average of numbers from 1 to 10 using while loop
#   average = sum of number / number of observations

# Print the average of even numbers from 1 to 100 (both included)
# .....................................................................
# i = 1
# sum = 0
# while i <= 10:
#     sum += i
#     i += 1
# avg = sum / 10
# print("The average of numbers from 1 to 10 is:", avg)
# .....................................................................
# i = 2
# j = 0
# sum = 0
# while i <= 100:
#     sum += i
#     i += 2
#     j += 1
# avg = sum / j
# print(j)
# print(f"The average of numbers from 1 to 10 is:{avg}")
# ............................................................
