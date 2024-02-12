# 1.set don't accept the duplcate values
set_a = {1, 2, 3, 4, 5, 5}
# result is [1, 2, 3, 4, 5]
print(set_a)

# 2. add item in set
set_a.add(6)
print(set_a)

# 3.remove item in set
set_a.remove(2)
print(set_a)
set_a.discard(3)
print(set_a)
 

# 4. mathematical methods in set
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(set_a.union(set_b))
#result is {1, 2, 3, 4, 5, 6, 7, 8}

print(set_a.intersection(set_b))
#result is {4, 5}

print(set_a.difference(set_b))
#result is {1, 2, 3}

print(set_a.symmetric_difference(set_b))
#result is {1, 2, 3, 6, 7, 8}

# 5.set are not subscriptable, it doesn't contain an ordered index of all elements inside
#error
print(set_a[0])