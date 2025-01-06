# Computing Group Project - Programs

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

# Task 1 - Explaination

The side length of the square is the same as the radius of the circle.
The positions are determined by the following logic:
> task_1/sysFiles/core.py (core.py contains the logic for the simulation)
```python
    self.boxCenterCoord = [self.boxLen / 2, self.boxWidth / 2]
    self.circleCenterCoord = [
        self.boxCenterCoord[0] - (self.boxCenterCoord[0] / 2),
        self.boxCenterCoord[1],
    ]
    self.squareCenterCoord = [
        self.boxCenterCoord[0] + (self.boxCenterCoord[0] / 2),
        self.boxCenterCoord[1],
    ]
    self.lengthToCenter = math.sqrt(
        (self.circleCenterCoord[0] + self.boxCenterCoord[0]) ** 2
        + (self.circleCenterCoord[1] + self.boxCenterCoord[1]) ** 2
    )
```
The above code calculates the center of the circle and the square. The circle is placed at the left side of the box and the square is placed at the right side of the box.
The distance between the center of the circle and the center of the box is calculated and stored in the variable lengthToCenter. This distance is used to determine if the point is inside the circle or the square.

and as for the simulation, the random points are plotted inside the box, and these will generate according to the length and width of the box
and to check if a point is inside the square or the cirlce, the following logic is used:
> task_1/sysFiles/core.py (core.py contains the logic for the simulation)
```python
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
```

# How to run task 1 ?

### Prerequisites

1. Python 3.6 or higher
2. pip

### Installing

1. Clone this repo
```
cd task_1/
pip install -r requirements.txt
```
### Running the program

```
navigate to the task_1 folder
cd task_1
For Commandline Version :
python3 main.py <box length> <box width> <radius of the circle> <number of samples>
For GUI Version :
python3 main.py
```

# How to run task 2?
### Prerequisites

1. Python 3.6 or higher
2. pip

### Installing

1. Clone this repo
```
pip install -r requirements.txt
```
### Running the program

```
navigate to the task_2 folder
cd task_2
For Q1:
python3 Q1.py <number of samples>
For Q2:
python3 Q2.py <number of samples>
```
