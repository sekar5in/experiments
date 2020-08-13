#!/usr/local/bin/python3

# This script to read the csv file.

import csv

with open('examplecsv.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

# empty list creation.
    dates = []
    colors = []

    for row in readCSV:
#        print(row)
#        print(row[0])
#        print(row[0], row[1])
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)
