import tkinter as tk
import math

# constants
mass = 0.1
COR = 0.9  # Coefficient of restitution
COF = 0.3  # Coefficient of friction
g = 10
t = 0.08  # time in secends


# Calculates and updates velocity
def updateVelocity(v0, gotHit):
    if gotHit:
         # hit the edge
        return COR * v0
    else:
        # moving on table
        return v0 - t * g * COF * 8


def drawO():
    global x, y, angle, x1, y1, x2, y2, velocity
    canvas.delete("o")

    # Calculates the position of "O" and angles
    # in the board
    newX = x - velocity * math.cos(math.radians(angle))
    newY = y - velocity * math.sin(math.radians(angle))

    if x1 < newX < x2 and y1 < newY < y2:
        x = newX
        y = newY

        velocity = updateVelocity(velocity, False)

    else:
        # out of board
        if not x1 < newX < x2:
            angle = 180 - angle

        else:
            angle = 360 - angle

        velocity = updateVelocity(velocity, True)

    canvas.create_text(x, y, text="o", fill="black", font=("Arial", 20), tags="o")

    # Positions of winning holes
    if (
        (x - 35) * (x - 35) + (y - 35) * (y - 35) < 225
        or (x - 785) * (x - 785) + (y - 35) * (y - 35) < 225
        or (x - 35) * (x - 35) + (y - 485) * (y - 485) < 225
        or (x - 785) * (x - 785) + (y - 485) * (y - 485) < 225
    ):
        print("YOU WON! ")  # victory()

    elif velocity > 0:
        base.after(80, drawO)
    else:
        newInputs()


# Gets new inputs after zero velocity
def newInputs():
    global velocity, angle
    velocity = int(input("enter velocity : "))
    angle = int(input("enter angle : "))
    newLine()
    drawO()


# Draws new line
def newLine():
    global angle, line
    canvas.delete("line")
    angleRad = math.radians(angle)
    lineLength = 300
    xLineEnd = x + lineLength * math.cos(angleRad)
    yLineEnd = y + lineLength * math.sin(angleRad)
    line = canvas.create_line(x, y, xLineEnd, yLineEnd, fill="red", tags="line")


# Initialize the tkinter window
base = tk.Tk()
base.title("board")
canvas = tk.Canvas(base, width=820, height=520)
canvas.pack()

# Initialize the board
x1, y1 = 20, 20
x2, y2 = 800, 500
canvas.create_rectangle(x1, y1, x2, y2, fill="green")

# first position of "o"
x = 410
y = 260


canvas.create_text(x, y, text="o", fill="black", font=("Arial", 20), tags="o")

# winning holes
x1hole1, y1hole1 = 20, 20
x2hole1, y2hole1 = 50, 50
canvas.create_oval(x1hole1, y1hole1, x2hole1, y2hole1, fill="black")

x1hole2, y1hole2 = 800, 20
x2hole2, y2hole2 = 770, 50
canvas.create_oval(x1hole2, y1hole2, x2hole2, y2hole2, fill="black")

x1hole3, y1hole3 = 20, 500
x2hole3, y2hole3 = 50, 470
canvas.create_oval(x1hole3, y1hole3, x2hole3, y2hole3, fill="black")

x1hole4, y1hole4 = 800, 500
x2hole4, y2hole4 = 770, 470
canvas.create_oval(x1hole4, y1hole4, x2hole4, y2hole4, fill="black")

# first inputs
velocity = int(input("enter first velocity : "))
angle = int(input("enter first angle : "))
angleRad = math.radians(angle)
lineLength = 300
xLineEnd = x + lineLength * math.cos(angleRad)
yLineEnd = y + lineLength * math.sin(angleRad)
line = canvas.create_line(x, y, xLineEnd, yLineEnd, fill="red", tags="line")

# waits for 0.08 sec
base.after(80, drawO)

base.mainloop()
