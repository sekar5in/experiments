#!/usr/local/bin/pyton3

# This script is used to find the syntax of try and except call for error handling.

import csv

with open('examplecsv.csv') as csvFile:
        csvRead = csv.reader(csvFile, delimiter=',')

        names = []
        ages = []


        for row in csvRead:
            name = row[3]
            age = row[1]

            names.append(name)
            ages.append(age)

        print(names)
        print(ages)

try:
    findName = input('What is name you like to search : ')
    findIndex = names.index(findName)
    findAge = ages[findIndex]
    print('The %s is %d years old' % (findName, int(findAge)))

except Exception as e:
    print(e)
