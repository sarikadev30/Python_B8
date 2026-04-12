# Modules => reusable piece of code
# 3 types
# Inbuilt
# User-Defined
# third party
# ........................................................
# def fun():
#     print("Hi")


# fun()
# ...........................................................
# INBUILT MODULE
# math , random , sys

# math
# 1.
# import math
# print(math.pi)
# # pi=3.1444...
# print(math.sqrt(4))
# ......................................................
# 2.
# import math as m

# print(m.cbrt(27))
# ......................................................
# 3.
# from math import pi, sqrt
# print(sqrt(81))

# Giving you diameter = 14 cm. Calculate circumference and area of circle. (2* pi *r)
# ..............................................................................
# user-defined modules

# import user_module

# print(dir(user_module))
# import user_module as u
# from user_module import add
# from user_module import add as a
# from user_module import add as a, product as b

# print(user_module.product(5, 6))
# print(u.product(5, 6))
# user_module.add(5, 6)
# u.add(5, 6)

# add(6, 7, 8, 9)
# a(6, 7, 8, 9)
# print(b(3, 4))
# .....................................................................
# Third Party Module
# import pyjokes

# print(dir(pyjokes))
# print(pyjokes.get_joke())

# .......................................................................
# Special Function => Reduce

# from functools import reduce

# ds = [1, 2, 3]
# ans = reduce(lambda x, y: x * y, ds)
# print(ans)
# ......................................................................
# ds = [2, 3, 4]
# from functools import reduce

# x = reduce(lambda a, b: a + b**2, ds,89)
# print(x)

# .........................................................................
# sys => inbuilt module
# random => inbuilt module

import random

# print(dir(random))
# print(random.randint(1, 5))

# Give user 3 chances => to guess the number if choice matches print "You Won" else "You Lose"

# random.randrange(start,end,step)
# print(random.randrange(2, 4))  # 2 3
# print(random.randrange(2, 4, 2))  # 2

# random.shuffle(list)       => shuffle the list elements
# x = [2, 3, 4, 5, 6]
# random.shuffle(x)
# print(x)

# random.choice(list)
# print(random.choice(x))
