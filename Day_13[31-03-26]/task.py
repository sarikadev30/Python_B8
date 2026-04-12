# Special Functions
# Special functions are built-in functions or anonymous functions
# that enhance Python’s expressiveness and functional programming capabilities

# print(len("PYTHON"))
# print(sum([2, 3, 4, 5]))

# LAMBDA FUNCTION anonymous function => no name => map , filter


# def fun(x):
#     print(x * x)

#     def y(x):
#         print("Hi I am new X: ", x)

#     return y


# ans = fun(6)
# print(ans(6))

# s = lambda x: x * x
# print(s(6))
# .......................................................................
# MAP Function => applies the function to each item in iterable

# map(function, iterable)

# a = [1, 2, 3, 4, 5, 6, 7, 8]
# print(a)

# x = list(map(lambda x: x * x, a))
# print(x)

# a = [1, 2, 3, 4, 5, 6, 7]
# x = list(map(lambda z: z % 2 == 0, a))
# print(x, a)

# ................................................................
# Filter Function => selects the element only when function returns true

# filter(function, iterable)

# a = [1, 2, 3, 4, 5, 6, 7]
# x = filter(lambda z: z % 2 == 0, a)
# x = list(filter(lambda z: z % 2 == 0, a))
# x = list(filter(lambda z: z*z, a)) # get all elements as function is not returning any false condition
# x = list(filter(lambda z: 0, a))
# print(x, a)

# .................................................................
# take a tuple and filter the multiples of 5

# ......................................................................
# Sorted Function => returns a new list out of iterables

# sorted(iterable)
# a = (2, 4, 5, 9, 1, 0, 12, 78, 12345, 45, 2, 6)
# z = sorted(a)
# print(z, a)


# sorted(iterable, key)
# d = {"a": 3, "c": 4, "b": 1}
# print(d.items())
# ans = sorted(d.items(), key=lambda x: x[0])  # based on key
# ans = sorted(d.items(), key=lambda x: x[1])  # based on value
# print(ans, d)
# pairs = [(1, 3), (2, 2), (4, 1)]
# ans = sorted(pairs, key=lambda x: x[1])  # based on value
# print(ans, pairs)
# words = ["appl", "bananaaaaa", "apricot", "cherry", "avocadoooooooooooooo"]
# ans = sorted(words, key=lambda x: len(x))  # based on value
# print(ans, words)

# ................................................................................
# isinstance => type checking

# x = 34
# y = input("Enter a number: ")
# ans = isinstance(x, int)
# # ans2 = isinstance(y, int)
# ans2 = isinstance(y, str)
# print(ans, ans2)

# ................................................................................
# ZIP => combines the multiple iterables
# words = ["apple", "banana", "apricot", "cherry", "avocado", "kiwi"]
# b = ["Sam", "Fam", "Hello", "Danny", "Leo"]
# c = [1, 2, 3, 4, 5, 6, 76, 7, 8, 7, 8, 9]
# ans = list(zip(words, b, c))
# print(ans)
# ................................................................................
# dir() =>
# repr() vs str()
