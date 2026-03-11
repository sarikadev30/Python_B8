# While with Break

# Break => stops the execution

# i = 1
# print("Start")
# while i < 5:
#     if i == 3:
#         break
#     print(i)
#     i += 1
# print("End")

# i=1
# Start
# i=1 1<5 => T 1==3 => F  1 i=1+1=2
# i=2 2<5 => T 2==3 => F  2 i=2+1=3
# i=3 3<5 => T 3==3 => T  => ENDS...
# End
# .....................................................
# i = 1
# print("Start")
# while i < 5:
#     print(i)
#     if i == 3:
#         break
#     i += 1
# print("End")
# ......................................................................
#  While With Continue
# continue => skips the execution
# i = 1
# print("Start")
# while i < 5:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# print("End")

# i=1
# Start
# i=1 1<5 => T i=1+1=2 2==3 => F  2
# i=2 2<5 => T i=2+1=3 3==3 => T skip the execution
# i=3 3<5 => T i=3+1=4 4==3 => F  4
# i=4 4<5 => T i=4+1=5 5==3 => F  5
# i=5 5<5 => F Ends...
# End
# ....................................................................
# i = 1
# print("Start")
# while i < 5:
#     print(i)
#     if i == 3:
#         continue
#     i += 1
# print("End")

# i=1
# Start
# i=1 1<5 => T  1  1==3 => F   i=1+1=2
# i=2 2<5 => T  2  2==3 => F   i=2+1=3
# i=3 3<5 => T  3  3==3 => T  skip the execution
# i=3 3<5 => T  3  3==3 => T  skip the execution
# i=3 3<5 => T  3  3==3 => T  skip the execution ...........
# ................................................................................
#  Find the First Multiple of 7 (1:10)    (using break)

# .......................................................................................
# Sum of Digits
# 1234

# 1234 => 4 3 2 1
# 4  1234%10     1234//10 =>123
# 3  123%10      123//10 => 12
# 2  12%10       12//10 => 1
# 1  1%10        1//10 =>0

# num = 23
# sum = 0
# while num > 0:
#     r = num % 10
#     sum += r
#     num = num // 10

# print(sum)

# num=23 sum=0
# 23>0 =>T r=23%10=>3 sum=0+3=3 num=23//10=>2
# 2>0 =>T r=2%10=>2   sum=3+2=5 num=2//10=>0
# 0>0 =>F End.......
# .......................................................................
# FOR LOOP

#  for i in sequence:
# print(i)

# range(start, end, step)

# for i in range(1, 6, 1):
#     print(i)

# for i in range(1, 6, 2):
#     print(i)

# for i in range(6):  # default start=0  default step=1   end=6
#     print(i)

# for i in range(1, 6):  # start=1  default step=1   end=6
#     print(i)

# for i in range(10, 0, -1):
#     print(i)

# for i in range(10, 0, -2):
#     print(i)
# for i in range(10, -1, -1):
#     print(i)
# ........................................................................
# to print numbers from 1 to 50
