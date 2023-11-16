import turtle
import ball

class BallApp:
    def __init__(self):
        num_balls = int(input("Number of balls to simulate: "))
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        canvas_width = turtle.screensize()[0]
        canvas_height = turtle.screensize()[1]
        turtle.colormode(255)
        self.__ballSystem = ball.BallSystem(ball.Vec2(canvas_width, canvas_height))
        self.__ballSystem.addRandomBalls(num_balls);
    def loop(self):
        while (True):
            turtle.clear()
            self.__ballSystem.tick();
            turtle.update()
        turtle.done()


BallApp().loop();
