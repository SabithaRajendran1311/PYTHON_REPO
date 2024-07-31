import turtle
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Bouncing Ball Animation")
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2
def move_ball():
    x, y = ball.position()
    if x + ball.dx > screen.window_width() // 2 or x + ball.dx < -screen.window_width() // 2:
        ball.dx *= -1
    if y + ball.dy > screen.window_height() // 2 or y + ball.dy < -screen.window_height() // 2:
        ball.dy *= -1    
    ball.setx(x + ball.dx)
    ball.sety(y + ball.dy)
    screen.update()
    screen.ontimer(move_ball, 20)
screen.tracer(0)
move_ball()
screen.mainloop()

