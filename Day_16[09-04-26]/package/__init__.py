print("Hi... I am a package")


# to export some methods
# __all__ = ["math_utils"]

from .math_utils import sumOfNums
from .string_utils import reverseStr
