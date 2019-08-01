#!/usr/bin/env python3

from circle import *
from z3 import *
from tex_compile import *

def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

if len(sys.argv) < 3:
    print("Please enter valid input and output files.")
    exit()

#for objective function
def z3abs(x):
    return If(x >= 0,x,-x)

circles = detect_circles(sys.argv[1], "output.png")
s = Optimize()
n = len(circles)
xcoords = []
ycoords = []
for x in range(0, n):
    xcoords.append(Int("x_" + str(x)))
    s.add(xcoords[x] >= 0)
for y in range(0, n):
    ycoords.append(Int("y_" + str(y)))
    s.add(ycoords[y] >= 0)
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
            s.add(ycoords[i] > ycoords[j])
        else:
            s.add(ycoords[i] < ycoords[j])
for i in range(0, n):
    for j in range(i + 1, n):
        s.minimize(z3abs(xcoords[i] - xcoords[j]))
        s.minimize(z3abs(ycoords[i] - ycoords[j]))
if(s.check() == sat):
     m = s.model()
     contents = "\\documentclass{article}\n"
     contents += "\\usepackage{tikz}\n"
     contents += "\\begin{document}\n"
     contents += "\\begin{tikzpicture}\n"
     for i in range(0, n):
         contents += "\\node[shape=circle, draw=black] (" + str(i) + ") at (" + str(m.get_interp(xcoords[i])) + "," + str(m.get_interp(ycoords[i])) + ") {};\n"
     contents += "\\end{tikzpicture}\n"
     contents += "\\end{document}"
     writeFile(sys.argv[2], contents)
     pdf_compile(sys.argv[2])
