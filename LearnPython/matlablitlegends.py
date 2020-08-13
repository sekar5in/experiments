#!/usr/local/bin/python3

# This is sample to display label with plot graph.

from matplotlib import pyplot as plt
from matplotlib import style

x = [1,2,3,4,5,6]
y = [5,6,7,8,9,7]

x1 = [5,6,7,8,9,7]
y1 = [1,2,3,4,5,6]

style.use('ggplot')
plt.grid(True, color='k')

plt.plot(x,y,'g',linewidth=5, label="Line one")
plt.plot(x1,y1,'c',linewidth=10, label='Line two')

plt.title("No idea what is this data for ?")
plt.xlabel('Some X data')
plt.ylabel('Some Y data')
plt.legend()


plt.show()
