import matplotlib.pyplot as plt

x1 = [2, 4, 5, 7]
y1 = [2, 3, 6, 7]

plt.plot(x1, y1, color='red', linestyle='dashed',
         linewidth=3, marker='o', markerfacecolor='black', markersize=10, label="line-1")


plt.xlabel('x-Axix')
plt.ylabel('y-Axix')

plt.title('demo-graph')
plt.legend()
plt.show()
