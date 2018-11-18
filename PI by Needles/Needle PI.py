import graphics
from random import *
from math import sin, cos
import Image

width = 1800
height = 1000
const = 100
d = 257
t = 257
n = 500

win = graphics.GraphWin("PI", width, height)
pi_win = graphics.GraphWin("PI", 200, 100)
text = graphics.Text(graphics.Point(100, 50), "")
text.draw(pi_win)

for i in range(height // t + 1):
    l = graphics.Image(graphics.Point(width // 2, i * t + const), "line.png")
    l.draw(win)

cross_overs = 0

for i in range(n):
    y = randint(0, height)
    x = randint(0, width)
    theta = randint(0, 360)
    xp = x + d * cos(theta)
    yp = y - d * sin(theta)
    if (yp // t) != (y // t):
        cross_overs += 1

    needle_name = Image.load_img(theta)
    needle = graphics.Image(graphics.Point((x + xp) // 2, (y + yp) // 2), needle_name)
    needle.draw(win)
    if cross_overs != 0:
        text.setText((2.0 * d * i) / (t * cross_overs))

try:
    win.getMouse()
except graphics.GraphicsError:
    pass
