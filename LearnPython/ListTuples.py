#!/usr/local/bin/python3

# This script used to demo the list and tuples datatypes.
# Tuples syntax
# x = 1,2,3,4,5
# x = (4,5,6,78)

# List syntax
# y = [10,20,30,40]

# Tuple and List declaration.
x = (4,5,6,78)
y = [10,20,30,40]

print(x[1])
print(y[2],y[3])


# Sample function
def exampleFunc():
    return 15,6

# Return value in different variables assignment.
x,y = exampleFunc()
print("functin return", x,y)

