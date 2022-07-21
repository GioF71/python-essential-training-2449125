import os
import time
from termcolor import colored
import math


class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    def hitsWall(self, point):
        return round(point[0]) < 0 or round(point[0]) >= self._x or round(point[1]) < 0 or round(point[1]) >= self._y

    def setPos(self, pos, mark):
        self._canvas[round(pos[0])][round(pos[1])] = mark

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))


class TerminalScribe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.trail = '.'
        self.mark = '*'
        self.framerate = 0.05
        self.pos = [0, 0]

    def setPosition(self, pos):
        self.pos = pos

    def calcDirection(self, degrees):
        radians = (degrees/180) * math.pi
        return [math.sin(radians), -math.cos(radians)]

    def up(self):
        self.forward(0)

    def down(self):
        self.forward(180)

    def right(self):
        self.forward(90)

    def left(self):
        self.forward(270)

    def forward(self, degrees):
        direction = self.calcDirection(degrees)
        pos = [self.pos[0] + direction[0],
               self.pos[1] + direction[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def drawSquare(self, size):
        for i in range(size):
            self.right()
        for i in range(size):
            self.down()
        for i in range(size):
            self.left()
        for i in range(size):
            self.up()

    def draw(self, pos):
        self.canvas.setPos(self.pos, self.trail)
        self.pos = pos
        self.canvas.setPos(self.pos, colored(self.mark, 'red'))
        self.canvas.print()
        time.sleep(self.framerate)


canvas = Canvas(30, 30)
scribe = TerminalScribe(canvas)

# I added the regular square just to verify that the up down left right method are still working
scribe.setPosition([0, 0])
scribe.drawSquare(10)

# restore initial position
# setPosition method should not necessarily be available also on the challenge
# I created it so that I can also draw the rectangle
scribe.setPosition([0, 0])

for i in range(30):
    scribe.forward(135)
