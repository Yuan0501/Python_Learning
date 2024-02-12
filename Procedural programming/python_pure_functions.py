#pure function is to not change the original value when it pass to the function as args
# so inside the function, it should create a new variable
my_list = [1, 2, 3]

# nl = lst.copy() is variable that newly created
def add_to_list(lst, item):
    nl = lst.copy() 
    nl.append(item)
    return nl

new_list = add_to_list(my_list,4)
#the result are :new_list = [1, 2, 3, 4]
#my_list = [1, 2, 3]
print(new_list)
print(my_list)
