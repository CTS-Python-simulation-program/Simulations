import sys
import random
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from sysFiles.messageBox import Popup
import vispy.plot as vp

globalDebug = Popup()
global hardwareAccel

hardwareAccel = False

# -> Try to initialize hardware acceleration
try:
    import cupy as cp

    # globalDebug.show_popup("Hardware Acceleration Status", "CUDA Device Detected !\nCanvas is now hardware accelerated using NVIDIA Graphics.")
    print(
        f"\n\nHardware Acceleration Status: CUDA Device Detected !\nCanvas is now hardware accelerated using NVIDIA Graphics."
    )
    print(f"Device Details : {cp.cuda.Device(0)}\n\n")
    cuda_available = True
    if hardwareAccel == False:
        print("Hardware Acceleration is not developed yet !, CUDA device will be ignored.\n\n")
except ImportError:
    # -> if hardware acceleration initialization shits the bed
    import numpy as np

    print(
        f"\n\nFailed to detect CUDA Device !\nHardware Acceleration is not available."
    )
    # globalDebug.show_popup("Hardware Acceleration Status", "Failed to detect CUDA Device !\nHardware Acceleration is not available.")
    cuda_available = False


class Plot:
    def __init__(
        self,
        boxLen,
        boxWidth,
        radius,
        boxCenterCoord,
        circleCenterCoord,
        squareCenterCoord,
        balls,
        title,
    ):
        self.boxLen = boxLen
        self.boxWidth = boxWidth
        self.radius = radius
        self.boxCenterCoord = boxCenterCoord
        self.circleCenterCoord = circleCenterCoord
        self.squareCenterCoord = squareCenterCoord
        self.balls = balls
        self.title = title

    def plot_π_Array(self, π_Array):
        plt.plot(π_Array)
        plt.xlabel("Rounds")
        plt.ylabel("π")
        plt.title("π Value Over Rounds")
        plt.show()

    def plot_shapes(self):
        fig, ax = plt.subplots()
        ax.set_xlim(0, self.boxLen)
        ax.set_ylim(0, self.boxWidth)
        rectangle = patches.Rectangle(
            (0, 0),
            self.boxLen,
            self.boxWidth,
            linewidth=1,
            edgecolor="blue",
            facecolor="none",
        )
        ax.add_patch(rectangle)
        circle = patches.Circle(
            self.circleCenterCoord,
            self.radius,
            linewidth=1,
            edgecolor="red",
            facecolor="none",
        )
        ax.add_patch(circle)

        square_side = self.radius
        square = patches.Rectangle(
            (
                self.squareCenterCoord[0] - square_side / 2,
                self.squareCenterCoord[1] - square_side / 2,
            ),
            square_side,
            square_side,
            linewidth=1,
            edgecolor="green",
            facecolor="none",
        )
        ax.add_patch(square)

        ax.plot(*self.boxCenterCoord, "bo", label="Box Center")
        ax.plot(*self.circleCenterCoord, "ro", label="Circle Center")
        ax.plot(*self.squareCenterCoord, "go", label="Square Center")

        try:
            ax.scatter(*zip(*self.balls), c="purple", s=1, label="Balls")
        except ValueError:
            print("Plot Skip")
        ax.set_title(self.title)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.legend()

        plt.gca().set_aspect("equal", adjustable="box")
        plt.show()

    # TODO - Hardware acceleration fix
    def plot_shapes_gpu(self):
        fig = vp.Fig(show=True)
        ax = fig[0, 0]

        # Plot box - blue lines
        ax.plot(
            [0, self.boxLen, self.boxLen, 0, 0],
            [0, 0, self.boxWidth, self.boxWidth, 0],
            color=(0),  # RGBA for blue
            width=2,
        )

        # Plot Circle - red lines
        theta = (
            cp.linspace(0, 2 * cp.pi, 100)
            if cuda_available
            else np.linspace(0, 2 * cp.pi, 100)
        )
        circle_x = (
            self.boxLen / 2 + self.radius * cp.cos(theta)
            if cuda_available
            else self.boxLen / 2 + self.radius * np.cos(theta)
        )
        circle_y = (
            self.boxWidth / 2 + self.radius * cp.sin(theta)
            if cuda_available
            else self.boxWidth / 2 + self.radius * np.sin(theta)
        )
        ax.plot(
            [0, self.boxLen, self.boxLen, 0, 0],
            [0, 0, self.boxWidth, self.boxWidth, 0],
            color="blue",  # Use a string color or RGBA tuple
            width=2,
        )

        # Plot Balls - purple dots
        ax.scatter(
            self.balls[:, 0], self.balls[:, 1], size=5, color=(0.5, 0, 0.5, 1)
        )  # RGBA for purple

        ax.set_xlim([0, self.boxLen])
        ax.set_ylim([0, self.boxWidth])
        ax.title = "Simulation Plot"
