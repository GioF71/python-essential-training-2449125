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

    def up(self):
        self.plot(0)

    def down(self):
        self.plot(180)

    def right(self):
        self.plot(90)

    def left(self):
        self.plot(270)

    def plot(self, degrees):
        radians = (degrees/180) * math.pi
        direction = [math.sin(radians), - math.cos(radians)]
        pos = [self.pos[0] + direction[0], self.pos[1] + direction[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def drawSquare(self, size):
        i = 0
        while i < size:
            self.right()
            i = i + 1
        i = 0
        while i < size:
            self.down()
            i = i + 1
        i = 0
        while i < size:
            self.left()
            i = i + 1
        i = 0
        while i < size:
            self.up()
            i = i + 1

    def draw(self, pos):
        self.canvas.setPos(self.pos, self.trail)
        self.pos = pos
        self.canvas.setPos(self.pos, colored(self.mark, 'red'))
        self.canvas.print()
        time.sleep(self.framerate)

canvas = Canvas(30, 30)
scribe = TerminalScribe(canvas)

for i in range(20):
    scribe.plot(135)

scribe.draw([0,0])
scribe.drawSquare(5)