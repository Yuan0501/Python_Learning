# 1.list can hold different datatypes
list1 = [1, 2, 3, 4, 5]

list2 = ['A', 'B', 'C']

list3 = ['Hello', 1, True, 40.22]

list4 = [1,[2,3,4], 5]

# 2.print the item in list
print(*list1)
print(list1, sep = " ")

# 3.insert function buildin lists
list1.insert(len(list1), 6)
print(list1, sep= " ")

list1.extend([6, 7, 8, 9])
print(list1, sep= " ")

# 4.remove item in the list
# 4 is the index
list1.pop(4)    
print(list1, sep= " ")

del list1[2]

#iterate the list
for i in list1:
    print("Values: ", i)
