#!/usr/bin/python

# Author : Dhanasekara Pandian
# Email : sekar5in@gmail.com
# 14-APR-2019 20:30:00 PM
# Free to modify and use for any purpose
# This script is to walk into the directory and find the file which contains the string of ip or hostname given 
# as agrument while running the script.

import argparse
import os
import re

# Specify the Master Path Where the directories to be scanned
MASTERPATH="/mnt/master"


def walk_by_directory(searchval):
    for root, dirs, files in os.walk(MASTERPATH):
        if files:
            for name in files:
                mypath=os.path.join(root,str(name))
                with open(mypath, 'r') as f:
                    if re.search(searchval, f.read()):
                        print(mypath)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("val", type=str, help="ip or hostname to search")
    args = parser.parse_args()
    walk_by_directory(args.val)


if __name__ == '__main__':
    main()