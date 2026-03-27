# FUNCTIONS


# def fun():
#     print("Hello World!...")


# fun()

# print("Start")

# print("Going On...")


# fun()

# print("End")
# ..............................................
# def fun():
#     a = 9
#     b = 12
#     print(a + b)
# fun()


# def add(a, b):
#     print(a + b)

# add(3, 5)
# add(4, 5)
# .............................................................
# Default Arguments


# def Fun(b, a=9):
#     print(a, b)
#     print(a - b)
# Fun(2, 3)
# Fun(2)
# ............................................
# Variable Length Arguments
# def fun(*x):
#     print(x)
#     print(sum(x))


# fun(1, 2)
# fun(1, 2, 3, 4, 5)
# fun(3, 4, 5)
# ...........................................
# Keyworded Arguments
# def fun(x, y):
#     print(x, y)

# y = 8
# x = 7
# fun(y=8, x=7)
# fun(y, x)


# def studentDetails(name, age, city):
#     print(f"name => {name} \nage => {age} \ncity=> {city}")


# # studentDetails("Joe", 23, "NY")
# studentDetails("Joe", city="NY", age=25)
# studentDetails("Joe", 34, city="NY")
# studentDetails("Joe", age=34, "NY")   #error
# ..............................................................................

# difference between print and return


# def studentDetails(name, age, city):
#     # print(f"name => {name} \nage => {age} \ncity=> {city}")
#     x = f"name => {name} \nage => {age} \ncity=> {city}"
#     return x


# # studentDetails("Joe", 23, "NY")
# ans = studentDetails("Joe", 23, "NY")
# print(ans)

# print(studentDetails("Joe", 23, "NY"))

# ......................................................
# Factorial of a number
# 5! = 5*4*3*2*1

# ....................................................
# Fibonacci Series
# next value= sum of previous two values
# 0 1 1 2 3 5 8
# def fib(n):
#     a = 0
#     b = 1
#     res = []
#     for i in range(n):
#         res.append(a)
#         c = a + b  # 1 => 0+1
#         a = b
#         b = c
#     return res

# print(fib(4))

# ....................................................
# SCOPE of A Variable
# LOCAL => ENCLOSING => GLOBAL SCOPE => BUILT IN SCOPE


# def fun():
#     a = 23  # Local Scope
#     print(a)


# fun()
# print(a)
# .............................................
# x = 34
# def funw():
#     print(x)  # Global  Scope

# funw()
# print(x)
# .............................................
# Enclosing Scope
# def fun():  # x = 89
#     x = 89
#     print(x)

#     def innerFun():  # x=67
#         x = 67
#         print(x)

#     innerFun()
#     print(x)


# fun()
# ..............................................

# def fun():  # x = 89
#     x = 89
#     print(x)

#     def innerFun():  # x=67
#         nonlocal x
#         x = 67
#         print(x)
#     innerFun()
#     print(x)

# fun()
# ..........................................

# x = 34  # global scope


# def printVal():
#     y = 23

#     x = 12
#     print(y)
#     print("inside", x)


# printVal()
# print("outside", x)
