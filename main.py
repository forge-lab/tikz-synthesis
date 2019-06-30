#!/usr/bin/env python3

from circle import *
from z3 import *

circles = detect_circles("input.png", "output.png")
s = Solver()
n = len(circles)
xcoords = []
ycoords = []
for x in range(0, n):
    xcoords.append(Int("x_" + str(x)))
    s.add(xcoords[x] >= 0)
for y in range(0, n):
    ycoords.append(Int("y_" + str(y)))
    s.add(ycoords[y] >= 0)
s.add(Sum(xcoords) < n ** 2)
s.add(Sum(ycoords) < n ** 2)
for i in range(0, n):
    for j in range(i + 1, n):
        if(abs(circles[i][0] - circles[j][0]) < circles[i][2]):
            s.add(xcoords[i] == xcoords[j])
        elif(circles[i][0] < circles[j][0]):
            s.add(xcoords[i] < xcoords[j])
        else:
            s.add(xcoords[i] > xcoords[j])
        if(abs(circles[i][1] - circles[j][1]) < circles[i][2]):
            s.add(ycoords[i] == ycoords[j])
        elif(circles[i][1] < circles[j][1]):
            s.add(ycoords[i] < ycoords[j])
        else:
            s.add(ycoords[i] > ycoords[j])
if(s.check() == sat):
    print(s.model())
