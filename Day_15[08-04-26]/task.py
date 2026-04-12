# Pickle Module
# import pickle

# x = [12, 34, 56, 78, 34, 11, 178, 67, 45, 90]

# write a file
# with open("modules/data.pkl", "wb") as f:
#     pickle.dump(x, f)
#     print("data saved")

# read a file
# with open("modules/data.pkl", "rb") as f:
#     y = pickle.load(f)
#     print("data loaded: ", y)
# ............................................................
# PYTHON EXCEPTIONS
# ZeroDivisionError: division by zero
# print(23 / 0)

# ValueError
# ans = int(input("Enter a Number: "))
# print(ans)

# IndexError: list index out of range
# d = [1, 2, 3, 4, 56, 78]
# print(d[10])

# ..................................................
# try-except block
# x = int(input("Enter a Number: "))

# try:
#     ans = 100 / x
#     print(ans)
# except ZeroDivisionError:
#     print("Cannot Divide 100 with 0")

# ...................................................
# multiple-except block

# try:
#     x = int(input("Enter a Number: "))
#     ans = 100 / x
#     print(ans)
# except ValueError:
#     print("Input needs to be a Number")
# except ZeroDivisionError:
#     print("Cannot Divide 100 with 0")
# .....................................................
# catching multiple exceptions together

# try:
#     x = int(input("Enter a Number: "))
#     ans = 100 / x
#     print(ans)
# except (ValueError, ZeroDivisionError) as e:
#     print("Error: ", e)

# print("Continue...")
# .....................................................
# Generic-exception handling
# try:
#     x = int(input("Enter a Number: "))
#     ans = 100 / x
#     res = [2, 34, 57, 899, 123, 234]
#     print(res[10])
# except Exception as e:
#     print("Error: ", e)
# print("Continue...")
# .....................................................
# finally
# try:
#     x = int(input("Enter a Number: "))
#     ans = 100 / x
#     res = [2, 34, 57, 899, 123, 234]
#     print(res[10])
# except Exception as e:
#     print("Error: ", e)
# finally:
#     print("We are handling all types of errors")
# print("Continue...")
# .........................................................
# Raising an error


# def divide(a, b):
#     if b == 0:
#         raise ValueError("b cannot be zero")
#     return a / b


# divide(10, 0)
# ..........................................................
