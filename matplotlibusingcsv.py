#!/usr/local/bin/python3

# Example for matplot to draw graph using csv / file.

from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

x,y = np.loadtxt('plotcsv.txt',
                 unpack= True,
                 delimiter=',')

plt.plot(x,y)
plt.title("No idea what is this data for ?")
plt.xlabel('Some X data')
plt.ylabel('Some Y data')

plt.show()

#Dirty Graph :-)

