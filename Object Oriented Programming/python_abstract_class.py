# Abstract Classes
#  1. Cannot create an instance for the abstract classes
#  2. should impose a module to define an abstract class
#  3. methods in the absract class needs to be defined before they can implemented

# Advantages to use abstract class
# 1. To hide the details of the implementation without sacrificing functionality
# Implement of absract class should in child class, and super() function can be used

# To implement the abstract class we should import a module ABC, and abstract method decorator
from abc import ABC, abstractclassmethod

# create inheriting class
class someAbstractClass(ABC):
    # A decorator is a function that takes another function as its arguments and gives a new function as its output, denoted by @ sign
    @abstractclassmethod
    def someabstractmethod(self):
        pass