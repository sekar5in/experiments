#!/usr/local/bin/python3

# This is subprocess module example programe.

import subprocess

# This print the ls output in stdout.
subprocess.call('ls', shell=True)

# This output the result to variable out in byte sting and can be printed as required.

out = subprocess.check_output('ls', shell=True)
print(out)

