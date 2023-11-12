import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 2, 0, 1])
plt.xticks([1, 2])
plt.yticks([1])

velocity = 0
pos = 1.5
for i in range(10, 0, -1):
    scat = plt.scatter(pos - velocity, 0.5, c='black')
    plt.pause(1)
    if i != 1:
        scat.remove()
    pos = pos - velocity
    if i == 10:
        velocity = 1
    velocity *= 0.5

plt.show()
