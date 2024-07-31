import turtle
screen=turtle.Screen()
screen.bgcolor("white")
screen.title("draw a square")
square_turtle=turtle.Turtle()
square_turtle.color("blue")
square_turtle.speed(1)
def draw_square(size):
    for _ in range(4):
        square_turtle.forward(size)
        square_turtle.right(90)
draw_square(100)
screen.mainloop()
