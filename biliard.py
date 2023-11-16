import matplotlib.pyplot as plt
import matplotlib.patches as patches

# game table setup
fig, ax = plt.subplots()
board = patches.Rectangle((0, 0), 5, 5, facecolor='green')
ax.add_patch(board)
point = plt.plot(0, 0, "o", color='black')[0]
point.set_data(4, 2.5)

# show table with anim
plt.ion()
plt.show()

# game variables
ballIsMoving = False


def isWinner(x, y):
    if (x == 0 or x == 5) and (y == 0 or y == 5):
        print("You won!")
        return True


# test values -------> they will be removed after implementing main values and functions
a = [[3.9, 2.5], (3.8, 2.5), (3.7, 2.5), (3.6, 2.5), (3.5, 2.5), (3.4, 2.5), (3.3, 2.5), (3.2, 2.5), (3.1, 2.5),
     (3.0, 2.5)]

# game loop
while True:

    # movement of ball based on inputs
    if ballIsMoving:
        for i in range(len(a)):
            point.set_data(a[i][0], a[i][1])
            plt.pause(0.1)
            if isWinner(a[i][0], a[i][1]):
                break
        ballIsMoving = False

    # get velocity and angle from user
    else:
        input("velocity :")
        ballIsMoving = True
