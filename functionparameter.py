#!/usr/local/bin/python3

# This script will help to find the usage of function call with parameter.

def simple_addition(num1, num2):
    result = num1 + num2
    print ('The Addition of %d + %d = %d' % (num1,num2, result))


simple_addition(num1=100, num2=200)
simple_addition(1024,2048)
