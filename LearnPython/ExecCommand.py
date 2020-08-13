#!/usr/local/bin/python3

# This example for Exec command.

exec("print('Hello this string of statement')")

exec("list_str = [5,6,7,8,93,2]")
print(list_str)

exec("def test_Program(): print('Hello World!!!')")

exec('''
def func_Cal():
    print("May be this also works")
''')

#Function Call
test_Program()
func_Cal()

