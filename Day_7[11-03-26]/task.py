# FOR LOOP

# for i in range(1, 6, 1):
#     print("Hello World")

# calculate sum from range 1-100


# for i in range(6):  # start=0  step=1   i = 0 1 2 3 4 5
#     print("Hello World")
# .....................................................................
# For loop with Break

# for guest in range(1, 6):
#     if guest == 4:
#         break
#     print("Guest", guest)

# dry run
# guest=1    (1,6)  guest==4 => F  "Guest 1" guest=2
# guest=2    (1,6)  guest==4 => F  "Guest 2" guest=3
# guest=3    (1,6)  guest==4 => F  "Guest 3" guest=4
# guest=4    (1,6)  guest==4 => T  break....
# Ends....
# ............................................................................
# for guest in range(1, 6):
#     print("Guest", guest)
#     if guest == 4:
#         break

# ............................................................................
# For loop with continue

# for i in range(1, 8):
#     if i == 5:
#         continue
#     print("Guest", i)

# count = 1
# for k in range(1, 10):  # 1,2,3,4,5,6,7,8,9

#     if k == 5:
#         continue
#     count += 1

# print(count)  # P = 10  N = 10  / 9

# .......................................................................
# Nested Loop

# for i in range(1, 6):  # 1,2,3,4,5
#     for j in range(1, 4):  # 1,2,3
#         print(f"family {i} ate {j} candy")

# 15 outcomes

# .......................................
# i = 0
# while i < 3:
#     j = 0
#     while j < 2:
#         print("Hello", i, j)
#         j += 1
#     i += 1
# dry run
# i=0  0<3 => T
# j=0 0<2 => T "Hello 0 0" j=0+1=1
# j=1 1<2 => T "Hello 0 1" j=1+1=2
# j=2 2<2 => F ... ENDS...
# i=0+1=1
# i=1 1<3 => T
# j=0 0<2 => T "Hello 1 0" j=0+1=1
# j=1 1<2 => T "Hello 1 1" j=1+1=2
# j=2 2<2 => F ... ENDS...
# i=1+1=2
# i=2 2<3 => T
# j=0 0<2 => T "Hello 2 0" j=0+1=1
# j=1 1<2 => T "Hello 2 1" j=1+1=2
# j=2 2<2 => F ... ENDS...
# i=2+1=3
# i=3 3<3 => F  ....Ends........

# ........................................................................
# Father gave the son a target, of completing 10 sets. Each set contains 10 Rounds of a field.
# "Set 1 , Round 1"

# ....................................................................................
"""
**********
**********
**********
**********
**********
"""
# row
# column
# row = 5
# col = 10
# for i in range(row):  # 0 1 2 3 4
#     for j in range(col):  # 0 1 2 3 4 5 6 7 8 9
#         print("*", end="")
#     print()

"""
0123456789
0123456789
0123456789
0123456789
0123456789
"""
"""
12345678910
12345678910
12345678910
12345678910
12345678910
"""
# row = 5
# col = 10
# for i in range(row):
#     for j in range(1, col+1):
#         print(j, end="")
#     print()
"""
0000000000
1111111111
2222222222
3333333333
4444444444
"""

"""
1111111111
2222222222
3333333333
4444444444
5555555555
"""

"""
*
**
***
****
*****
******
*******
"""
# # Number of rows and columns
# rows = 5
# cols = 10

# # Outer loop for rows
# for i in range(1, rows + 1):  # 1 2 3 4 5
#     # Inner loop for columns
#     for j in range(i):
#         print("*", end="")
#     # Move to the next line after each row
#     print()

"""
1
12
123
1234
12345
123456
"""
# row = 6
# for i in range(1, row + 1):  # 1,2,3,4,5,6
#     for j in range(1, i + 1):  # 1,2 3 ....
#         print(j, end="")
#     print()

"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6
"""
"""
1
21
321
4321
54321
654321
"""

"""
******
*****
****
***
**
*
"""
