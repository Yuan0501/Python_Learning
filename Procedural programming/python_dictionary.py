# 1. dictionary structure: key - value
sample_dict = {1: 'Coffee', 2: 'Tea', 3: 'Juice'}

# 2.access value by key
print(sample_dict[2]) 

# 3.change the value by key
sample_dict[2] = 'Mint Tea'
print(sample_dict[2]) 

# 4. delete value by key
del sample_dict[3]

# iterate the item in dictionary
my_d = {1: 'Test', 'Name': 'Jim'}

#print keys: 1, Name
for i in my_d:
    print(i)

for key, value in my_d.items():
    print(str(key) + " : " + value)