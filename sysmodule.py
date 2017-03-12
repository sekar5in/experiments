#!/usr/local/bin/python3

# This script demo for sys module.

import sys

#sys.stderr.write('Thisis test message in screen')
#sys.stderr.flush()
#sys.stdout.write('This is stdout message')

#print(sys.argv)

#if len(sys.argv) > 1:
#    print(sys.argv[1])

# This receives the argument from main function call of sys.argv argument.
def main(arg):
    print(arg)

# Passing the system argument value to main function and main function prints the same.
main(sys.argv[1])

'''
Its ran in console and below is the result.

[root@devops experiments]# chmod +x sysmodule.py
[root@devops experiments]# ./sysmodule.py 100
100
[root@devops experiments]#

'''