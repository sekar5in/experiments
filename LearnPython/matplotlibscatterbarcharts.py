#!/usr/local/bin/python3

# This is sample to display label with plot graph.

from matplotlib import pyplot as plt
from matplotlib import style

x = [1,2,3,4,5,6]
y = [5,6,7,8,9,7]

x1 = [5,6,7,8,9,7]
y1 = [1,2,3,4,5,6]

style.use('ggplot')

#plt.scatter(x,y, label='Line One')
#plt.scatter(x1,y1, label='Line Two')

#plt.scatter(x,y,color='g')
#plt.scatter(x1,y1,color='c')

plt.bar(x,y,color='g', align='center')
plt.bar(x1,y1,color='c', align='center')

plt.title("No idea what is this data for ?")
plt.xlabel('Some X data')
plt.ylabel('Some Y data')



plt.show()
