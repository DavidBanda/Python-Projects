from matplotlib import pyplot as plt
import numpy as np

plt.style.use('ggplot')
#plt.style.use('dark_background')

'''
x = [2, 4, 6, 8]
y = [7, 3, 8, 3]

x2 = [1, 3, 5, 7]
y2 = [6, 7, 2, 6]

#plt.plot(x, y, 'b', linewidth=5, label = 'line1')
#plt.plot(x2, y2, 'c', linewidth=7, label = 'line2')

#plt.scatter(x, y, color='b', label = 'line1')
#plt.scatter(x2, y2, color='c', label = 'line2')

plt.bar(x, y, color='b', label = 'line1', align='center')
plt.bar(x2, y2, color='c', label = 'line2', align='center')
'''
x, y = np.loadtxt('valuesMatplotlib.csv', unpack=True, delimiter=',')

plt.plot(x, y)

plt.title('Grafica', fontsize=20)
plt.ylabel('Eje Y', fontsize=15)
plt.xlabel('Eje X', fontsize=15)
#plt.legend()
#plt.grid(True, color='y')


plt.show()
