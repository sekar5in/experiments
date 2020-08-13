import matplotlib.pyplot as plt
import csv
import matplotlib.style as style
import numpy as np

style.use('ggplot')

'''
example.csv content
3,8
4,6
8,9
1,2
5,9
2,9
3,8
4,6
8,9
1,2
5,9
2,9
'''

x = []
y = []

'''
# Commented of csv file graph
with open('example.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y, label='Loaded from file')
'''

x,y = np.loadtxt('example.csv', delimiter=',', unpack=True)
plt.plot(x,y, label='Loaded from file')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph')
plt.legend()
plt.show()
