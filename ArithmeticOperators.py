#!/usr/local/bin/python3

# This script helps to find the usage of math operators.
# + :   Addition
# - :   Subtraction
# * :   Multiplication
# / :   Division
# % :   Modulus
# **    :   Exponent
# //    :   Floor Division

# Declare the variables and assign values.
num1 = 100
num2 = 75
result = 0

# Addition
result = num1 + num2
print('The value of ', num1 ,'+' ,num2 ,'is :' ,result)

#subtraction
result = num1 - num2
print('The value of', num1, '-', num2 ,'is :', result)

#Multiplication
result = num1 * num2
print('The value of %d * %d is :  %d' % (num1, num2, result))

#Division
result = num1 / num2
print('The value of %d / %d is : %f' % (num1,num2,result))

#Modulus
result = num1 % num2
print('The value of %d %d is : %f' % (num1, num2, result))

#Exponent
result = num1 ** num2
print('The value of %d ** %d is : %f' % (num1,num2, result))

#Floor Division
result = num1 // num2
print('The value of %d // %d is : %f' % (num1, num2, result))
