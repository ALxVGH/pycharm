from turtle import *
from random import randint
# screen settings:
WIDTH, HEIGHT = 1024, 768



# turtle settings:
tu = Turtle()
tu.penup()
tu.setposition(0, -350)
tu.pendown()
tu.pensize(2)
tu.color("Red")
tu.speed(0)

axiom = "X"
itr = 12
angle = randint(0, 30)
color = [0.35, 0.2, 0.0]
thickness = 20
le = 80
stack = []

# dragon dict
# dic = {"+": "+", "-": "-", "X": "X+YF+", "Y": "-FX-Y", "F": "F"}
# simple tree
# dic = {"+": "+", "-": "-", "[": "[", "]": "]","X": "F[+X]F[-X]+X", "F": "FF"}
dic = {"+": "+", "-": "-", "[": "[", "]": "]", "@": "@", "X": "F@[-X]+X", "F": "F"}

def apply_rule(ax):
    Result_axiom = ""
    for simbl in ax:
        Result_axiom += dic[simbl]
    return Result_axiom


for k in range(itr):
    axiom = apply_rule(axiom)
tu.left(90)
tu.pensize(thickness)
for s in axiom:
    tu.color(color)
    if s == 'F':
        tu.forward(le)
    elif s == 'X':
        tu.forward(le)
    elif s == '@':
        le -= 6
        color[1] += 0.04
        thickness -= 2
        thickness = max(1, thickness)
        tu.pensize(thickness)
    elif s == '+':
        tu.right(randint(-45, 45))
    elif s == '-':
        tu.left(randint(-45, 45))
    elif s == '[':
        stack.append((tu.heading(), tu.pos(), thickness, le, color[1]))
    elif s == ']':
        ang_, pos_, thickness, le, color[1] = stack.pop()
        tu.pensize(thickness)
        tu.setheading(ang_)
        tu.penup()
        tu.goto(pos_)
        tu.pendown()
#tu.update()
#tu.mainloop()
