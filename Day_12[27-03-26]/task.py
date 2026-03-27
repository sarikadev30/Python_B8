# GLOBAL SCOPE

# x = 34  # global Scope


# def printVal():
#     # global x
#     y = 23
#     x = 12
#     print(y)
#     print("inside", x)


# printVal()
# print("outside", x)


# ..............................................................
# def outer():
#     a = 23
#     print(a)

#     def inner():
#         nonlocal a
#         a = 90
#         b = 13
#         print("inner", a, b)

#     inner()
#     print(a)


# outer()
# ........................................................................
# BUILT-IN SCOPE           => (built in module)
# print(len("PYTHON"))
# print(type("string"))

# Local => Enclosing => Global => Built-In => Error
# ..........................................................................
# x = 100


# def change():
#     global x
#     print(x)
#     x = 200
#     print(x)


# change()
# print(x)
# ...........................................................................
# x = 5
# def outer():
#     x = 10
#     def inner():
#         print(x)
#     inner()


# outer()
# print(x)
# ...........................................................................

# def func():
#     print(x)


# # func()   #error
# x = 50
# func()
# ...........................................................................
# x = "global"


# def outer():
#     x = "outer"

#     def inner():
#         print("inner:", x)

#     print("outer:", x)
#     inner()
#     # return inner


# outer()
# print("global", x)
# # inner()
# # xu = outer()
# # xu()

# # outer outer global outer

# ................................................................
# File Handling

# 1st Way
# file = open("data.txt", "r")  # opens data.txt in read mode
# print(file.read())


# file.close()  # close the file after finishing

# ........................................................
# 2nd Way
# with open("fileA.txt", "r") as f:
#     # f.write("Bye... I am going to give Error")
#     content = f.read()
#     print(content)
# File is automatically closed after the with-block ends
# ..................................................................
# File Modes
# r => Read
# w => Write /Overwrites
# a => Append
# variants of r and w
# r+ => r and w
# w+ => r and w
# a+ => r and w
# ..................................................................
# with open("fileA.txt", "w") as f:
#     f.write("Hi.. I am back!....")

# with open("fileA.txt", "a") as f:
#     f.write("Bye.......")
# ..................................................................
# r+ => No file creation possible
# with open("data.txt", "r+") as f:
#     print(f.tell())
#     print(f.read())
#     print(f.tell())
#     f.write("Updates Done...")
#     print(f.tell())
#     f.seek(0)
#     f.write("Updates Starts from 0...")
# ....................................................................
# w+ => File created if not there

# with open("document.txt", "w+") as f:
#     print(f.tell())
#     # f.write("Hello!...")
#     # print(f.tell())
#     # f.seek(0)
#     res = f.read()
#     print(res)
# ...................................................................
# a+ => File created if not present

with open("document.txt", "a+") as f:
    print(f.tell())
    # f.seek(0)
    f.write("World!...")
    print(f.tell())
    f.seek(0)
    res = f.read()
    print(res)
# ...................................................................
# read() => read whole file as a string
# readline() => read the file line by line
# readlines() => read the file lines into a list

# with open("studentData.txt", "r+") as f:
#     # x = f.readline()
#     # print(x)
#     # a = f.tell()
#     # print(a)
#     # f.seek(a)
#     # x = f.readline()
#     # print(x)

#     x = f.readlines()
#     print(x)
#     for i in x:
#         print(i)
# ....................................................................

# with open("d2.txt", "w+") as f:
#     print(f.tell())
#     l = f.readlines()
#     print(l)
#     f.seek(0)
#     print(f.tell())

# for i in range(len(l)):
#     f.write(f"Good Morning...{l[i]}")
#     if i == 4:
#         f.seek(0)
#         print(f.read())
#         break
# ...........................................................................
