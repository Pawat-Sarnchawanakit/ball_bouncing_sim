import turtle
import ball

num_balls = int(input("Number of balls to simulate: "))
turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()
canvas_width = turtle.screensize()[0]
canvas_height = turtle.screensize()[1]
turtle.colormode(255)
ballSystem = ball.BallSystem(ball.Vec2(canvas_width, canvas_height))
ballSystem.addRandomBalls(num_balls);
while (True):
    turtle.clear()
    ballSystem.tick();
    turtle.update()
turtle.done()
