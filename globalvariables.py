#!/usr/local/bin/python3

# This script to show the syntax of global and local variables usage.

x = 10


# global variable declaration and usage.
def example():
    global x
    print('example')
    print(x)
    print(x+5)

# global variable converted into local variable.
def examplelocalvariable():
    print('examplelocalvariable')
    globx = x
    print(globx)
    print(globx+20)


# global variable converted into local variable with return value.
def examplelocalvariablereturn():
    globx = x
    print('examplelocalvariablereturn')
    print(globx)
    return globx+20

# global variable function call.
example()

# local variable function call.
examplelocalvariable()


# local variable function call with return result.
x = examplelocalvariablereturn()

# global variable value changed after function call with returned value from examplelocalvariable().
print(x)
