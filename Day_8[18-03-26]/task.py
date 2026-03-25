"""
    *
   ***
  *****
 *******
*********

....*
...***
..*****
.*******
*********
"""

# n=5
# i=1 => 4 (spaces)  =>  (n-i)     5 => 1         (2*i-1)  2*1-1
# i=2 => 3                         4 => 3                  2*2-1 =3
# i=3 => 2                         3 => 5                  2*3-1 =5
# i=4 => 1                         2 => 7                  2*4-1=7
# i=5 => 0                         1 => 9                  2*5-1=9

# n = 5
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(".", end="")
#     for k in range(2 * i - 1):
#         print("*", end="")
#     print()


"""
1  2  3  4  5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9

"""

# .................................................................................
# DATA TYPES
# str float int bool
# s = "Hello"
# print("s", s, s[1])
# s[1] = "u"
# print("s", s)

# .................................................................................
# LIST
x = ["chips", "icecreams"]
print(x, type(x), len(x))

# CRUD  => CREATE READ UPDATE DELETE

# CREATE
# x = ["chips", "icecreams"]
# y = list((23, 45, 12, 23))
# print(y, type(y))
# .....................................................................
# READ
# z = [2, 3, 4, 5, 6, 7, 8, 9]
#  0 1 2.............
#               -2 ,-1
# Positive Indexing => 0 to n-1
# Negative Indexing => -n to -1

# z = [1, 2, 3, 4, "Sam", 3.4, True, False, 54.90]
# print(z[4], z[-2])

# K = [1, 2, 3, "Sam", "Danny", True, 3.4, [1, 4, 5, 6, 7]]
# print(K[-1])
# print(K[-1][2])
# ..........................................................
# loops
# for i in z:  # [2, 3, 4, 5, 6, 7, 8, 9]
#     print(i,z.index(i))

# for i in range(len(z)):
#     print(i, z[i])
# ..........................................................
# SLICING
z = [2, 3, 4, 1, 6, 7, 8, 9, 10, 23]
# Syntax => listName[start:end:step]

# print(z[2:5:1])  # end => end-1
# print(z[:3:2])  # start default=0
# print(z[:5:])  # step default=1
# print(z[6::-1])
# print(z[6::1])
# print(z[6::])
# print(z[-2::-1])  # step=-1
# .........................
# Problem:
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#               0      1          2          3       4       5         6
# print(thislist[-4:-1])  # end => end-1
# print(thislist[:4])
# print(thislist[2:5])
# print(thislist[2:])
# .....................................................................
# UPDATE

# z = [2, 3, 4, 1, 6, 7, 8, 9, 10, 23]
#    0  1  2  3  4  5  6  7   8  9

# Replace......................
# print(z)
# z[2] = 34
# z[-2] = 3
# print(z)

# Addition .................................................
# Append : add an element at the end
# z.append(45)
# z.append(["chips", "icecreams", "softdrinks"])
# print(z)
# ....................................................
# Insert : add element at the perticular position =>.insert(position, value)
# z.insert(2, "SAM")
# print(z)
# z.insert(-2, [2, 3, 4, 5])
# print(z)
# ...............................................................
# Extend  : add the elements of the list : at the end
# z.extend(["SAM", "DANNY", "JOE", "MONICA"])

# w = ["SAM", "DANNY", "JOE", "MONICA"]
# z.extend(w)

# print(z)
# ........................................................................................
# PROBLEM 1 **Perform the following tasks :**
# 1. **Create list of superheroes**
# 2. **push 4 superheroes in the List**
# 3. **Print the List**
# sup = ["Ironman"]

# sup = ["Ironman"]
#        0
# sup.insert(1, "Superman")
# sup.append("Wonderwoman")
# sup[2] = "Wonderwoman"
# sup[3] = "Batman"
# sup.extend(["Batman"])
# print(sup)
# ........................................................................................
