from graphics import *
from random import *
from math import sqrt
from time import *

width = 800
height = 800
n = 1000

win = GraphWin("PI", width, height)
c = Circle(Point(width / 2, height / 2), width / 2)
c.draw(win)

pi_win = GraphWin("PI", 200, 100)
t = Text(Point(100, 50), "")
t.draw(pi_win)

inside_dots = 0
for i in range(1, n):
    sleep(0.05)  # can be removed
    x = randint(0, width)
    y = randint(0, height)
    dot = Circle(Point(x, y), 2)
    dot.setFill("red")
    dot.draw(win)
    if sqrt(((width / 2.0) - x) ** 2 + ((height / 2.0) - y) ** 2) < width / 2:
        inside_dots += 1
    t.setText((4.0 * inside_dots) / i)


win.getMouse()
