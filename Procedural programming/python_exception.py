#Index Error
items = [1, 2, 3, 4, 5]
# item = items[6] Error
try:
    item = items[6]
except:
    print("The index does not exist in the list")


#ZeroDivisionError
def divide(a, b):
    try: return a / b
    except ZeroDivisionError:
        return 0
    except Exception as e:
        print(e, 'Something went wrong')

print(divide(40, 0))