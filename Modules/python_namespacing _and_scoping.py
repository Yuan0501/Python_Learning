def d():
    # Local variable
    animal = "elephant"
    def e():
        nonlocal animal
        # local variable
        animal = "giraffe"
        print("Inside nested function: " + animal)

    print("Before calling function: " + animal)
    e()
    print("After nested function: " + animal)

# Global variable
animal = "camel"
d()
print("Global animal: " + animal)

# result is:
# Before calling function: elephant
# Inside nested function: giraffe
# After nested function: giraffe
# Global animal: camel