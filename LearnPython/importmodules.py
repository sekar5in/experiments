#!/usr/local/bin/python3

#import statistics as s   --> This import statistics and alias as  's'
#from statistics import variance  --> It only imports variance function only from statistics module.
#from statistics import variance as v  --> it imports variance from statistics and named as v for the imported function.
#from statistics import *  ---> it imports all functions from statistics modules.

import statistics as s

example_list = [1,3,4,5,6,7,6,4,3,4,5,8,6,5,4,3,2,3,4,8,9,8,9,7,6,5]
x = s.variance(example_list)
y = s.mean(example_list)
print(x)
print(y)



