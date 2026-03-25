# LIST

# DELETE
# z = [2, 10, 3, 4, 10, 1, 6, 10, 7, 10, 8, 9, 10, 23, 10]

# POP => using Index
# print(z)
# z.pop(2)
# z.pop(17)   Index Error
# print(z)
# If index not provided, it will remove the last element

# REMOVE => using the value
# z.remove(23)
# z.remove(230)  Value Error
# print(z)
# If multiple values are there => it will remove the first iteration
# z.remove(10)
# print(z)
# ..................................................................................
# PROBLEM
# stationary = []
# stationary.extend(["pen", "pencil", "notebooks", "marker", "Eraser", "Sharpner"])
# print(stationary)
# stationary.remove("marker")
# print(stationary)
# stationary.pop(2)
# print(stationary)
# stationary.pop()
# print(stationary)
# ......................................................................................
# movies = ["bahubali", "Spider-Man", "Iron Man", "Superman"]
# for i in range(len(movies)):
#     if i == 3:
#         break
#     print(movies[i])

# movies = ["bahubali", "Spider-Man", "Iron Man", "Superman", "Thor", "Avengers"]
# for i in range(len(movies)):
#     print(movies[i])
#     if i == 2 or i == 4:
#         continue

# ......................................................................................
# INBUILT FUNCTIONS

# # sum
# z = [2, 10, 3, 4]
# print(sum(z))
# # max
# print(max(z))
# #  min
# print(min(z))
# # index
# print(z.index(2))
# ..........................................................................
# Problem 1 :
# l = []
# for i in range(1, 6):  # 1 2 3 4 5
#     a = int(input(f"Enter number {i} :"))
#     print(a)
#     l.append(a)

# print(l)

# Problem 2 :
# x = [1, 2, 5, 3, 4]
# fmx = x[0]
# smx = x[0]
# for i in range(len(x)):
#     if x[i] > fmx:
#         smx = fmx
#         fmx = x[i]
#     elif x[i] < fmx and x[i] > smx:
#         smx = x[i]
# print(smx, fmx)

# Problem 3 :
# y = [1, 2, 3, 4, 5, 6, 7]
# print(y[2:6:1])
# range(start,end,step)
# ............................................................................
# SET
x = {1, 5, 7, 8, 2, 4}
y = {"Mango", "Apple", "Grapes", "Kiwi", "Pineapple"}
# print(x, y)
# print(type(x))

# print(x[2:4:1])   # Slicing Not Possible

# CRUD OPERATION ...............................................................
# CREATE
# WAY 1
# x = {1, 5, 7, 8, 2, 4}
# WAY 2
# y = set((3, 4, 9, 0, 12))
# print(y, type(y), len(y))

# ...........................................................................
# READ
# for i in y:
#     print(i)

# ............................................................................
# UPDATE
# x = {1, 5, 7, 8, 2, 4}
# print(x)

# add => add a single element
# x.add(90)
# x.add(90)
# x.add(90)
# x.add(90)
# x.add(0)
# print(x)

# update => add a list
# y = [9, 4, 6, 8, 2, 6, 9]
# x.update(y)
# print(x)
# ...........................................................
# DELETE
# x = {1, 5, 7, 8, 2, 4}
# print(x)
# remove =>  it will raise error, if value is not present
# x.remove(5)
# print(x)
# x.remove(50)
# print(x)

# .......................................
# discard   =>  it will not raise error, if value is not present
# x.discard(5)
# print(x)
# x.discard(500)
# print(x)

# .......................................
# clear => to remove all elements from the set (empty set)
# x.clear()
# print(x)
# .......................................
# pop => removes the first element in that scenario

# ................................................................
# SEARCHING
# print(2 in x)
# print(7 not in x)
# ..........................................................................................
# letters = set("mississippi")
# print(letters, len(letters))
# letters.pop()  # removes the first value from the set
# print(letters)
# ..............................................................................
# even_numbers = {2, 4, 6, 8, 10}
# prime_numbers = {2, 3, 5, 7}
# intersection = even_numbers & prime_numbers
# print(intersection)
# x = even_numbers - intersection
# print(x)
# .................................................................
# y = [1, 2, 3, 4, 5, 4, 2, 1, 2, 2, 3, 3, 4, 4, 5]

# x = set(y)
# print(x, type(x))

# ....................................................................................
