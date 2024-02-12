# create a class and instantiates an object
# Two ways to create a mew empty object
# 1. new method
# 2. init method

class Recipe():
    # def __new__(cls) -> Self:
    #     pass
    def __init__(self, dish, items, time):
        self.dish = dish
        self.items = items
        self.time = time

    def contents(self):
        print("The " + self.dish + " has " + str(self.items) + \
              " and takes " + str(self.time) + " min to prepare")
    

pizza = Recipe("Pizza", ["cheese", "bread", "tomato"], 45)
pasta = Recipe("Pasta", ["penne", "sauce"], 55)

print(pizza.items)
print(pizza.contents())