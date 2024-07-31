import turtle
screen=turtle.Screen()
screen.bgcolor("white")
screen.title("draw a triangle")
triangle_turtle=turtle.Turtle()
triangle_turtle.color("green")
triangle_turtle.speed(1)
def draw_triangle(size):
    for _ in range(3):
     triangle_turtle.forward(size)
     triangle_turtle.left(120)
draw_triangle(100)
screen.mainloop()
