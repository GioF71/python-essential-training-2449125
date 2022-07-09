import os
import time
from termcolor import colored
import math 
from enum import Enum

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

        self.direction = [0, 1]

    def setDegrees(self, degrees):
        radians = (degrees/180) * math.pi 
        self.direction = [math.sin(radians), -math.cos(radians)]

    def up(self):
        self.direction = [0, -1]
        self.forward()

    def down(self):
        self.direction = [0, 1]
        self.forward()

    def right(self):
        self.direction = [1, 0]
        self.forward()

    def left(self):
        self.direction = [-1, 0]
        self.forward()

    def forward(self):
        pos = [self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]]
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

class Direction(Enum):
    LEFT = 1,
    RIGHT = 2,
    UP = 3,
    DOWN = 4

class Action(Enum):
    SET_DEGREES = 0,
    GO_LEFT = 1,
    GO_RIGHT = 2,
    GO_UP = 3,
    GO_DOWN = 4

class Program:

    def __init__(self):
        self.actions = []

    def go(self, degrees, count):
        self.actions.append([degrees, count])

    def execute(self, scribe):
        for current in self.actions:
            scribe.setDegrees(current[0])
            for i in range(current[1]):
                scribe.forward()


canvas = Canvas(30, 30)
scribe = TerminalScribe(canvas)
#scribe.setDegrees(135)
#for i in range(30):
#    scribe.forward()

p1 = Program()
p1.go(135, 30)
p1.execute(scribe)

scribe.draw((0, 0))

p2 = Program()
p2.go(90, 5)
p2.go(180, 5)
p2.go(270, 5)
p2.go(0, 5)

p2.execute(scribe)
