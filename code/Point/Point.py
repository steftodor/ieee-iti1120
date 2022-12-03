class Point:
    'Represents a point in 2-D space'

    def __init__(self, xcord=0, ycord=0) -> None:
        'Initialize the position of a new point'
        self.x = xcord
        self.y = ycord

    def setx(self, x):
        'Set the x coordinate of the point'
        self.x = x

    def sety(self, y):
        'Set the y coordinate of the point'
        self.y = y

    def get(self):
        'Return a tuple representing the point'
        return (self.x, self.y)

    def move(self, dx, dy):
        'Move the point by dx and dy'
        self.x += dx
        self.y += dy

    def __str__(self) -> str:
        'Return a string representation of the point'
        return "Point: ( " + str(self.x) + ", " + str(self.y) + " )" 

