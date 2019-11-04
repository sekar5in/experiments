#!/usr/local/bin/python3

# This script is used to introduce the class in python3


# Class defined with different functions.
class calculator:

    def addition(x, y):
        added = x + y
        print(added)

    def subtraction(x, y):
        sub = x - y
        print(sub)

    def multiplication(x, y):
        mult = x * y
        print(mult)

    def division(x, y):
        div = x / y
        print(div)


# Object defined

cal = calculator
cal.addition(10,10)

# Class Object function call.

calculator.addition(5, 6)
calculator.subtraction(100, 99)
calculator.multiplication(5, 5)
calculator.division(100, 20)
