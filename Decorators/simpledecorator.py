# -*- coding: utf8 -*-

# Decorator is just a function which call another function.
# Author : Dhanasekara Pandian
# Email : sekar5in@quehive.com
# Free to modify and use for any purpose
# www.quehive.com

# Importing the Libraries
import functools


# Decorator Definition
def my_decorator(func):
    @functools.wraps(func)
    def function_run():
        print("In the decorator")
        func()
        print("After the decorator")
    return function_run


# Function Definition
@my_decorator
def my_function():
    print("This print from my_function")


# Function Call
my_function()
