# Super class
class Employees:
    def __init__(self, name, last):
        self.name = name
        self.last = last
    
# Inherance in python is to put the super class in the child class's parentheses
class Supervisors(Employees):
    def __init__(self, name, last, password):
        super().__init__(name, last)
        self.password = password

class Chefs(Employees):
    def leave_request(self, days):
        return "May I take a leave for " + str(days) + " days"


adrian = Supervisors("Adrian", "A", "Apple")
emily = Chefs("Emily", "E")
juno = Chefs("Juno", "J")

print(emily.leave_request(3))
print(adrian.name)

# Build-in functions:
# There are two built-in functions that can come in handy when trying to find the relationship between different classes and objects: 
# issubclass() and isinstance().issubclass()
#  result is [False, True], subclass in the front is True
print(issubclass(Employees, Supervisors))
print(issubclass(Supervisors, Employees))

# Another built-in function similar to this one is isinstance() thatdetermines if some object is an instance of some class. 
print(isinstance(adrian, Employees))
