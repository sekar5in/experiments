#!/usr/local/bin/python3

# This script helps to find the usage of default values in function parameters.


def simple_passing():
    pass

def simple_passin(num1, num2 =100):
    print(num1, num2)

def motorcar(make, model, color='White', Wheels=True):
    print(make, model, color)

# This is pass statement define function call.
simple_passing()

# This is function with default value on second argument call.
simple_passin(100)

# This is function call of default value and not used one arugment.
motorcar('Maruthi', 'SwiftDezire')
