# 1.tuples can hold different datatypes
my_tuples = (1, 'strings', 4.5, True)

# 2. access item in tuples
print(my_tuples[1])

# 3.functions in tuple
print(my_tuples.count('strings'))
print(my_tuples.index(4.5))

# 4.iterate in tuple
for i in my_tuples:
    print(i) 

# 5. tuple values are immutable, that is they cannot be changed
#error
my_tuples[0] = 5 
