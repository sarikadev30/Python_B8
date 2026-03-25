# TUPLE

# CRUD => CREATE   READ  UPDATE => X  DELETE => X

#  Create........................................
# x = (2, 3.4, "SAM", True)
# print(x, type(x))

# y = tuple((2, 45, "Danny"))
# print(y, type(y))

# a = [23, 45, 67, 90, 120, 230, 45]
# b = {23, 45, 67, 89, 123, 1232344}
# z = tuple(a)
# z = tuple(b)
# print(z, type(z))

# .............................................
# Read
# z = (23, 45, "SAM", 56.78, True, False)
# Indexing
# print(z[3])
# ............................
# Loops
# for i in z:
#     print(i, z.index(i))

# for i in range(len(z)):
#     print(i, z[i])
# ............................
# Slicing
# print(z[2::])
# print(z[-1::-1])
# .......................................................
x = (2, 3, 5, 6, 7, 8, 9, 10)
# print(x[-3])
# print(x[5:0:-1])
# print(x[-3:-7:-1])
# .......................................................
y = (2, 3, 12, 13, 14, 15, 16, 17)

# Merging
# a = y + x + z
# print(a)

# ........................................................................
# Adding Element to a Tuple =>
#   tuple to list => add the element => list to tuple
# y = (2, 3, 12, 13, 14, 15, 16, 17)
# print(type(y))

# z = list(y)
# print(type(z))
# z.append(93)
# print(z)
# y = tuple(z)
# print(y, type(y))
# ...............................................................................
# PROBLEMS............
# nested = (1, 2, (3, 4), [5, 6], {23, 45, 190})
# nested[3].append(7)
# nested[3].extend([9, 34, 23, 12])

# nested[4].add(0)
# print(nested)
# ................................................................................
# DICTIONARY

# CREATE
# 1.
# x = {"name": "SAM", "age": 23, "city": "NY"}
# print(x, type(x))
# 2.
# y = dict({"name": "SAM", "age": 23, "city": "NY"})
# print(y, type(y))
# print(len(x))
# .........................................................
# READ
# print(x["city"])
# print(x["name"])

# for i in x:
#     print(i, x[i], end=" ")


# for key, value in x.items():
#     print(key, value)


# d = {
#     "name": ["Anny", "Bunny", "Danny", "Enav"],
#     "age": [25, 36, 22, 32],
#     "income": [90, 75, 80, 93],
# }
# print(f"{d["name"][0]} - {d["age"][0]}")
# print(f"{d["name"][0]} - {d["age"][0]} - {d["income"][0]}")

# for i in d:
#     print(i, d[i][2])

# ............................................................
# x = {"name": "SAM", "age": 23, "city": "NY", "name": "Danny"}
# print(x)


# ..................................................................
# UPDATE
# x = {"name": "SAM", "age": 23, "city": "NY"}
# # Replace
# x["name"] = "Danny"
# print(x)
# # add
# x["fatherName"] = "Joe"
# print(x)
# .......................................................
# PROBLEM
# countries = ["India", "France", "Japan", "Canada"]
# capitals = ["New Delhi", "Paris", "Tokyo", "Ottawa"]

# CCD = {}
# for i in range(len(countries)):
#     CCD[countries[i]] = capitals[i]

# print(CCD)
# .......................................................
# DELETE

# x = {"name": "SAM", "city": "NY", "age": 23}
# print(x)
# ...........................................
# pop => delete a particular key-value pair
# x.pop("city")
# print(x)
# ...........................................
# popitem => delete the last key-value pair
# x.popitem()
# print(x)
# ...........................................
# clear => to remove all the key-value pairs
# x.clear()
# print(x)
# ..........................................
# del => delete a dictionary
# del x
# print(x)
# ..............................................................

# Set Exception ..............
# o = {1, 2, 3, 4, 5}
# print(o, type(o))
# o.clear()
# print(o)
# ...........................................
# Problem
# y = {}
# z = ()
# a = []
# print(y, z, a, type(y), type(z), type(a))
# ........................................................................
# Functions/Methods in dictionary
x = {"name": "SAM", "city": "NY", "age": 23}
print(x)
print(x["city"])

# get() => to get the value based on key . We can add a customize msg
ans = x.get("city")
ans = x.get("fatherName", "Not Found")
print(ans)

# keys() => to get all the keys
print(x.keys())
# values() => to get all the value
print(x.values())

for i in x.values():
    print(i)

# items() => to get all the key-value pairs
print(x.items())

# ......................................................................
