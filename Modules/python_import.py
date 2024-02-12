# 1. Every python file can be a modules
# 2. Use modules that can be imported from anywhere

import sys
# This method can insert the other files in different directory into your working directory
sys.path.insert(1, r'/Users/yuanyuanzhu/Coursera-lesson/Python/Procedural programming')

# This is import the python file from other path
import python_pure_functions
print(python_pure_functions)


# Writing import statements
# import math can import all the methods from the math modules
import math
root = math.sqrt(9)
print(root)

#  This is just import the specific method from the modules you imported
from math import sqrt

root = sqrt(9)
print(root)

# rename the imported modules, when you use the method, you just renamed module name
import math as m
cosine = m.cos(0)

# You also can import many methods from modules
from math import factorial, log10, sqrt

# Import all the method form modules can use *
from math import *
