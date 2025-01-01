import sys
import random
import math
import matplotlib.pyplot as plt
global progress
import matplotlib.patches as patches
progress = 0

def plot_π_Array(π_Array):
    plt.plot(π_Array)
    plt.xlabel("Rounds")
    plt.ylabel("π")
    plt.title("π Value Over Rounds")
    plt.show()

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
    # locationX = random.randint(0, boxLen)
    # locationY = random.randint(0, boxWidth)
    locationX = random.random()*boxLen
    locationY = random.random()*boxWidth
    return locationX, locationY

def checkData(boxLen, boxWidth, radius, rounds):
    boxCenterCoord = [boxLen/2, boxWidth/2]
    circleCenterCoord    = [boxCenterCoord[0]-(boxCenterCoord[0]/2), boxCenterCoord[1]]
    squareCenterCoord = [boxCenterCoord[0]+(boxCenterCoord[0]/2), boxCenterCoord[1]]
    hitCircle = 0
    hitSquare = 0
    ballCoords = [[0,0]]
    demoBalls = []
    π_Array = []
    lengthToCenter = math.sqrt((circleCenterCoord[0]+boxCenterCoord[0])**2 + (circleCenterCoord[1]+boxCenterCoord[1])**2)

    print(f"Box center coordinates: {boxCenterCoord}, Circle center coordinates: {circleCenterCoord}, Square center coordinates: {squareCenterCoord}")

    for i in range(0, rounds):
        ballCoords.append(hitRandomBall(boxLen, boxWidth))
        progress = round(i/rounds*100)
        print(f"\rProgress:{progress}% [{'█'* progress :<100}]",end="")
        if math.sqrt((ballCoords[i][0]-circleCenterCoord[0])**2 + (ballCoords[i][1]-circleCenterCoord[1])**2) < radius:
            hitCircle += 1
        elif ballCoords[i][0] < (squareCenterCoord[0]+radius/2) and ballCoords[i][0] > (squareCenterCoord[0]-radius/2) and ballCoords[i][1] < (squareCenterCoord[1]+radius/2) and ballCoords[i][1] > (squareCenterCoord[1]-radius/2):
            hitSquare += 1
        if hitCircle != 0 and hitSquare != 0:
            π_Array.append(hitCircle/hitSquare)
        else:
            π_Array.append(0)
        i += 1
    print()
    plot_shapes(boxLen, boxWidth, radius, boxCenterCoord, circleCenterCoord, squareCenterCoord, demoBalls, "Before Simulation - Close this window to continue")
    plot_shapes(boxLen, boxWidth, radius, boxCenterCoord, circleCenterCoord, squareCenterCoord, ballCoords, "After Simulation - Close this window to continue")
    print(f"\n\n\nNumber of balls inside the circle: {hitCircle}, Number of balls inside the square: {hitSquare}")
    print(f"Value of pi: {hitCircle/hitSquare}")
    plot_π_Array(π_Array)

if __name__ == "__main__":
    try:
        if len(sys.argv) == 5:
            checkData(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]))
        else:
            print("""Please provide the correct arguments !!!\n
    Correct Format = python main.py <box length> <box width> <radius> <no of rounds>
    box length, box width, radius and rounds should be numbers""")
        progress = 0
    except Exception as e:
        print(f"Error: {e}")
