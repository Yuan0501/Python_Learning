# To reverse a string, one way is using slice function, another way is to use recursion
# 1. str[start:stop:step]

trial = "reversal"
#slice function
new_trial = trial[::-1]
print(new_trial)

# 2. recursion function
def string_reverse(str):
    if(len(str) == 0):
        return str
    else:
        return string_reverse(str[1: ]) + str[0]

print(string_reverse("reversal"))