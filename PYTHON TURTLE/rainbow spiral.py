import turtle
import time
screen=turtle.Screen()
screen.bgcolor("white")
screen.title("colorful spiral animation")
spiral=turtle.Turtle()
spiral.speed(0)
colors=["red", "orange", "yellow", "red", "green", "blue", "purple"]
def animate_spiral():
    try:
        for i in range(360):
            spiral.color(colors[i % 6])
            spiral.forward(i * 0.5)
            spiral.right(59)
            time.sleep(0.01)
            screen.update()
    except turtle.Terminator:
        pass
screen.tracer(0)
animate_spiral()
screen.mainloop()

