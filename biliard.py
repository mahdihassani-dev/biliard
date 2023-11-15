
import matplotlib.pyplot as plt

point = plt.plot(0, 0, "o")[0]
plt.ylim(0, 5)
plt.xlim(0, 5)
plt.ion()
plt.show()

point.set_data(4, 2.5)
plt.pause(1)

a = [[3.9, 2.5], (3.8, 2.5), (3.7, 2.5), (3.6, 2.5), (3.5, 2.5), (3.4, 2.5), (3.3, 2.5), (3.2, 2.5), (3.1, 2.5), (3.0, 2.5)]

for i in range(len(a)):
     point.set_data(a[i][0], a[i][1])
     plt.pause(0.01)

plt.show(block=True)
