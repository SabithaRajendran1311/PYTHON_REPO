import turtle
screen=turtle.Screen()
screen.bgcolor("white")
screen.title("draw a circle")
circle_turtle=turtle.Turtle()
circle_turtle.color("red")
circle_turtle.speed(1)
def draw_circle(radius):
    circle_turtle.circle(radius)
draw_circle(50)
screen.mainloop()
