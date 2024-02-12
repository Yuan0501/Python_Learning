# map function requies two arguments, one is function, another is iterables, so using map function don't need to write for loop to pass 
# every items in the list 
# map function will return a map object, using for loop to see the item in the result
menu = ["espresso", "mocha", "latte", "cappuccino", "cortado", "americano"]

def find_coffee(coffee):
    if(coffee[0] == "c"):
        return coffee
    
# map function, result is [ None, None, None, cappuccino, cortado, None]
map_coffee = map(find_coffee, menu)
print(map_coffee)
for x in map_coffee:
    print(x)

# filter function, result is cappuccino, cortado
filter_coffee = filter(find_coffee, menu)
print(find_coffee)
for x in filter_coffee:
    print(x)

# map function return all the results that apply to the function
# filter function only return the results that are true to the function
   