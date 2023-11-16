
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots()
board = patches.Rectangle((0, 0), 5, 5, facecolor='green')
ax.add_patch(board)
point = plt.plot(0, 0, "o", color='black')[0]
#plt.ylim(0, 5)
#plt.xlim(0, 5)
plt.ion()
plt.show()

point.set_data(4, 2.5)
plt.pause(1)

a = [[3.9, 2.5], (3.8, 2.5), (3.7, 2.5), (3.6, 2.5), (3.5, 2.5), (3.4, 2.5), (3.3, 2.5), (3.2, 2.5), (3.1, 2.5), (3.0, 2.5)]

for i in range(len(a)):
     point.set_data(a[i][0], a[i][1])
     plt.pause(0.1)

     if (a[i][0] == 0 or a[i][0] == 5) and (a[i][1] == 0 or a[i][1] == 5):
          print("You won!")
          plt.pause(2)
          break

plt.show(block=True)
