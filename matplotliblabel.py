#!/usr/local/bin/python3

# This is sample to display label with plot graph.

from matplotlib import pyplot as plt

x = [1,2,3,4,5,6]
y = [5,6,7,8,9,7]

plt.plot(x,y)

plt.title("No idea what is this data for ?")
plt.xlabel('Some X data')
plt.ylabel('Some Y data')
plt.show()

