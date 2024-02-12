# 1. args can pass in any non-keyword variables 
def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

# different number of variables can pass in function
print(sum_of(1, 3))
print(sum_of(4, 5, 6, 7))

# 2. kwargs can pass in any keyword arguments
def sum_of1(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
    return round(sum,2)
print(sum_of1(coffee = 2.99, cake = 4.55, juice = 2.99))


