# !pip install icecream

from icecream import ic

# normal way of printing the value of variables
var_1 = 1
var_2 = 2
print("var_1 =", var_1)
print("var_2 =", var_2)

ic(var_1)         # output is: ic| var_1: 1
ic(var_2)         # output is: ic| var_2: 2

def func(num):
    return num*2

ic(func(3))        # output is: ic| funct(3): 6

# when finished, search for the pattern 'ic(' and remove the staterments
# you can also use ic.disable() to stop from printing
# if you need to reuse them, use ic.enable()
