# -*- coding: utf8 -*-

# Decorator is just a function which call another function.
# Author : Dhanasekara Pandian
# Email : sekar5in@quehive.com
# Free to modify and use for any purpose
# www.quehive.com

# Importing the Libraries
import functools


def my_decorator(func):
    @functools.wraps(func)
    def function_run():
        print("In the decorator")
        func()
        print("After the decorator")
    return function_run


# Decorator With Arguments
def my_decorator_with_arguments(number):
    def my_deco(func):
        @functools.wraps(func)
        def function_run_with_arguments(*args, **kwargs):
            print("In the decorator")
            if number == 50:
                func()
            else:
                print("display from actual function")
                func(*args, **kwargs)
            print("After Decorator")
        return function_run_with_arguments
    return my_deco


# Function Definition
@my_decorator
def my_function():
    print("This print from my_function")


@my_decorator_with_arguments(51)
def my_function_with_argument():
    print("This print from my_function_with_argument ")


# Function Call
my_function()
my_function_with_argument()
