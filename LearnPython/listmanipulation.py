#!/usr/local/bin/python3

# This script used for list manipulation.

x = [1,2,3,4,5,6,7,8,9,96,5,43,3,2,23]

x.append(2)  # Adding the data '2' at the end of list.
print(x)
x.insert(1, 100)  # inserting the value 100 on the place 2
print(x)
x.remove(2)  # removing the element at place 3.
print(x)
print(x[5:9])  # filter only the elements from 5 to 9 to print
print(x[-2])  # reverse start from -1,-2,-3 so its filter the -2 item.
print(x.index(3))  # index helps to find the posting of the given data.
x.sort()   # This sorts the list in ascending order.
print(x)

