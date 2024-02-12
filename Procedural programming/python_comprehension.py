# 1. List comprehension
# [<expression> for x in <sequence> if <condition>]

data = [2,3,5,7,11,13,17,19,23,29,31]
data = [x+3 for x in data]
# The result is:  [5, 6, 8, 10, 14, 16, 20, 22, 26, 32, 34]
print("The result is: ", data)

# with if condition
data = [x for x in data if x%4 == 0]
# The result is:  [8, 16, 20, 32]
print("The result is: ", data)



# 2. Dictionary comprehension
# dict = { key: value for key, value in <sequence> if <condition>}

usingrange = {x:x+2 for x in range(10)}
# Using range:  {0: 2, 1: 3, 2: 4, 3: 5, 4: 6, 5: 7, 6: 8, 7: 9, 8: 10, 9: 11}
print("Using range: ", usingrange)

months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]
numdict = {x:x**2 for x in number}
print("Using one input to create dict: ",numdict)
months_dict = {key:value for key, value in zip(number, months)}
print("Using one input to create dict: ", months_dict)



# 3. set comprehension
# Similar to list comprehension
set_a = {x for x in range(10, 20) if x not in[12, 13, 15]}
print(set_a)



# 4. Generator comrehension
# The elements in this iterator object cannot be directly accessed and need the help of a for loop and as such, 
# I iterate over these elements and print them.
data = [2,3,5,7,11,13,17,19,23,29,31]
gen_obj = (x for x in data)
print(gen_obj)
print(type(gen_obj))
for items in gen_obj:
    print(items, end = " ")


a=[[96],[69]]
print(''.join(list(map(str,a))))