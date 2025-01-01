import sys
import random
import math
import matplotlib.pyplot as plt
from sysFiles.backup import hitRandomBall

global progress
import matplotlib.patches as patches
from sysFiles.plotting import Plot
from sysFiles.messageBox import Popup


class Sim:
    def __init__(self, boxLen, boxWidth, radius, rounds, progress_callback=None):
        self.boxLen = boxLen
        self.boxWidth = boxWidth
        self.radius = radius
        self.rounds = rounds
        self.π_Array = []
        self.progress = 0
        self.progress_callback = progress_callback
        self.boxCenterCoord = [self.boxLen / 2, self.boxWidth / 2]
        self.circleCenterCoord = [
            self.boxCenterCoord[0] - (self.boxCenterCoord[0] / 2),
            self.boxCenterCoord[1],
        ]
        self.squareCenterCoord = [
            self.boxCenterCoord[0] + (self.boxCenterCoord[0] / 2),
            self.boxCenterCoord[1],
        ]
        self.hitCircle = 0
        self.hitSquare = 0
        self.ballCoords = []
        self.ballDemoCoords = [[0, 0]]
        self.lengthToCenter = math.sqrt(
            (self.circleCenterCoord[0] + self.boxCenterCoord[0]) ** 2
            + (self.circleCenterCoord[1] + self.boxCenterCoord[1]) ** 2
        )

    def checkCenterCoords(self):
        print(
            f"Box Center Coordinates: {self.boxCenterCoord}, Circle center coordinates: {self.circleCenterCoord}, Square center coordinates: {self.squareCenterCoord}"
        )
        newPlot = Plot(
            self.boxLen,
            self.boxWidth,
            self.radius,
            self.boxCenterCoord,
            self.circleCenterCoord,
            self.squareCenterCoord,
            self.ballDemoCoords,
            "Simulation Overview: Before Simulation\nCheck Commandline",
        )
        newPlot.plot_shapes()
        userIn = input("Proceed ? (Y/N) :")
        if userIn.lower() == "y":
            pass
        else:
            sys.exit()

    def runSim(self):
        for i in range(0, self.rounds):
            self.ballCoords.append(
                ((random.random() * self.boxLen), (random.random() * self.boxWidth))
            )
            self.progress = round(i / self.rounds * 100)
            if self.progress_callback:
                self.progress_callback(self.progress)
            print(f"\rProgress:{self.progress}% [{'█'* self.progress :<100}]", end="")
            if (
                math.sqrt(
                    (self.ballCoords[i][0] - self.circleCenterCoord[0]) ** 2
                    + (self.ballCoords[i][1] - self.circleCenterCoord[1]) ** 2
                )
                < self.radius
            ):
                self.hitCircle += 1
            elif (
                self.ballCoords[i][0] < (self.squareCenterCoord[0] + self.radius / 2)
                and self.ballCoords[i][0]
                > (self.squareCenterCoord[0] - self.radius / 2)
                and self.ballCoords[i][1]
                < (self.squareCenterCoord[1] + self.radius / 2)
                and self.ballCoords[i][1]
                > (self.squareCenterCoord[1] - self.radius / 2)
            ):
                self.hitSquare += 1
            if self.hitCircle != 0 and self.hitSquare != 0:
                self.π_Array.append(self.hitCircle / self.hitSquare)
            else:
                self.π_Array.append(0)
        print("\n")

    def showData(self):
        debug = Popup()
        debug.show_popup(
            "Debugger: Simulation",
            f"Box Center Coordinates: {self.boxCenterCoord}\nCircle center coordinates: {self.circleCenterCoord}\nSquare center coordinates: {self.squareCenterCoord}\n\nHit Circle: {self.hitCircle}\nHit Square: {self.hitSquare}\n\nπ Value: {self.π_Array[-1]}",
        )
        # newPlot = Plot(self.boxLen, self.boxWidth, self.radius, self.boxCenterCoord, self.circleCenterCoord, self.squareCenterCoord, self.ballDemoCoords, "Simulation Overview: Before - Close this window to continue...")
        # newPlot.plot_shapes()
        debug.show_popup(
            "Debugger: Plot",
            "Simulation Overview is loading...\n This may take sometime...",
        )
        newPlot = Plot(
            self.boxLen,
            self.boxWidth,
            self.radius,
            self.boxCenterCoord,
            self.circleCenterCoord,
            self.squareCenterCoord,
            self.ballCoords,
            "Simulation Overview: After - Close this window to continue...",
        )
        # newPlot.plot_shapes_gpu()
        newPlot.plot_shapes()
        newPlot.plot_π_Array(self.π_Array)


if __name__ == "__main__":
    if len(sys.argv) == 5:
        MonteSim = Sim(
            float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4])
        )
        # MonteSim.checkCenterCoords()
        MonteSim.runSim()
        MonteSim.showData()
    else:
        print(
            """Please provide the correct arguments !!!\n
                Correct Format = python main.py <box length> <box width> <radius> <no of rounds>
                box length, box width, radius and rounds should be numbers"""
        )
