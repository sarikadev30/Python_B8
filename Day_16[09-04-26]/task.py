# ujson
# pandas
# orjson

# .....................................................
# Packages

# Group of modules => package

# photos
#  image1.png
# image2.png
# .....................................................
# import package.math_utils, package.string_utils

# ans = package.math_utils.powOfA(2, 3)
# print(ans)
# package.math_utils.sumOfNums(2, 3)
# package.string_utils.reverseStr("python")

# .......................................................
# from package import *

# math_utils.sumOfNums(2, 3)
# string_utils.reverseStr("python")        # not defined

# .......................................................
# import package

# package.sumOfNums(4, 5, 6)
# package.reverseStr("JOEY")
# .......................................................
# from package import sumOfNums, reverseStr
# from package import sumOfNums as a, reverseStr

# sumOfNums(3, 4, 5, 6)
# a(3, 4, 5, 6)
# reverseStr("Monica")

# .........................................................

# Create a package called shapes with two modules:
# circle.py and rectangle.py,
# each with appropriate functions.

# Circle
# circumference => using radius
# area => using radius

# Rectangle
#  Perimeter => length, breadth
#  Area => length, breadth
# ......................................................................
# COUNTER => subclass of dictionary

from collections import Counter

# d = [
#     "apple",
#     "mango",
#     "apple",
#     "banana",
#     "mango",
#     "apple",
#     "kiwi",
#     "kiwi",
#     "kiwi",
#     "kiwi",
# ]
# ans = Counter(d)
# print(ans)

# useful methods
# most_common
# res = ans.most_common(2)
# print(res)

# add more elements
# ans.update(["orange", "watermelon", "orange"])
# print(ans)
# print(ans["kiwi"])

# .........................................................

# Count word frequency in a paragraph.

x = """Atoms of radioactive elements can split. According to Albert Einstein, mass and energy are interchangeable under certain circumstances.
When atoms split, the process is called nuclear fission. In this case, a small amount of mass is converted into energy.
Thus the energy released cannot do much damage. However, several subatomic particles called neutrons are also emitted during this process.
Each neutron will hit a radioactive element releasing more neutrons in the process.
This causes a chain reaction and creates a large amount of energy.
This energy is converted into heat which expands uncontrollably causing an explosion. Hence, atoms do not literally explode.
They generate energy that can cause explosions."""
