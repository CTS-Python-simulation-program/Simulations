import sys
import random
import math
import matplotlib.pyplot as plt
global progress
import matplotlib.patches as patches
progress = 0

def plot_shapes(boxLen, boxWidth, radius, boxCenterCoord, circleCenterCoord, squareCenterCoord, balls, title):
    fig, ax = plt.subplots()
    ax.set_xlim(0, boxLen)
    ax.set_ylim(0, boxWidth)
    rectangle = patches.Rectangle((0, 0), boxLen, boxWidth, linewidth=1, edgecolor='blue', facecolor='none')
    ax.add_patch(rectangle)
    circle = patches.Circle(circleCenterCoord, radius, linewidth=1, edgecolor='red', facecolor='none')
    ax.add_patch(circle)

    square_side = radius
    square = patches.Rectangle(
        (squareCenterCoord[0] - square_side / 2, squareCenterCoord[1] - square_side / 2),
        square_side, square_side, linewidth=1, edgecolor='green', facecolor='none'
    )
    ax.add_patch(square)

    ax.plot(*boxCenterCoord, 'bo', label="Box Center")
    ax.plot(*circleCenterCoord, 'ro', label="Circle Center")
    ax.plot(*squareCenterCoord, 'go', label="Square Center")

    try:
        ax.scatter(*zip(*balls), c='purple', s=1, label="Balls")
    except:
        print("Plot Skip")
    ax.set_title(title)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.legend()

    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def hitRandomBall(boxLen, boxWidth):
    locationX = random.randint(0, boxLen)
    locationY = random.randint(0, boxWidth)
    return locationX, locationY

def checkData(boxLen, boxWidth, radius, rounds):
    boxCenterCoord = [boxLen/2, boxWidth/2]
    circleCenterCoord = [boxCenterCoord[0]-(boxCenterCoord[0]/2), boxCenterCoord[1]]
    squareCenterCoord = [boxCenterCoord[0]+(boxCenterCoord[0]/2), boxCenterCoord[1]]
    hitCircle = 0
    hitSquare = 0
    ballCoords = [[0,0]]
    demoBalls = []
    lengthToCenter = math.sqrt((circleCenterCoord[0]+boxCenterCoord[0])**2 + (circleCenterCoord[1]+boxCenterCoord[1])**2)

    print(f"Box center coordinates: {boxCenterCoord}, Circle center coordinates: {circleCenterCoord}, Square center coordinates: {squareCenterCoord}")

    for i in range(0, rounds):
        ballCoords.append(hitRandomBall(boxLen, boxWidth))
        print(f"\rProgress: {i/rounds*100}%",end="")
        if math.sqrt((ballCoords[i][0]-circleCenterCoord[0])**2 + (ballCoords[i][1]-circleCenterCoord[1])**2) <= radius:
            hitCircle += 1
        elif ballCoords[i][0] < (squareCenterCoord[0]+radius/2) and ballCoords[i][0] > (squareCenterCoord[0]-radius/2) and ballCoords[i][1] < (squareCenterCoord[1]+radius/2) and ballCoords[i][1] > (squareCenterCoord[1]-radius/2):
            hitSquare += 1
        i += 1
    print()
    plot_shapes(boxLen, boxWidth, radius, boxCenterCoord, circleCenterCoord, squareCenterCoord, demoBalls, "Before Simulation - Close this window to continue")
    plot_shapes(boxLen, boxWidth, radius, boxCenterCoord, circleCenterCoord, squareCenterCoord, ballCoords, "After Simulation - Close this window to continue")
    print(f"\n\n\nNumber of balls inside the circle: {hitCircle}, Number of balls inside the square: {hitSquare}")
    print(f"Value of pi: {hitCircle/hitSquare}")

if __name__ == "__main__":
    rounds = 10000

    try:
        checkData(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]),  rounds)
    except:
        print("""Please provide the correct arguments !!!\n
Correct Format = python courseWork.py <box length> <box width> <radius>
box length, box width and radius should be numbers""")
    progress = 0
