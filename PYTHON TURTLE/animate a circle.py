import turtle
import math
screen=turtle.Screen()
screen.bgcolor("white")
t=turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.speed(0)
radius=100
angle_step=5
def animate():
    t.clear()
    angle=0
    while True:
        x=radius*math.cos(math.radians(angle))
        y=radius*math.sin(math.radians(angle))
        t.goto(x,y)
        angle+=angle_step
        if angle>=360:
            angle=0
animate()
screen.mainloop()
