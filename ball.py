import turtle
import random

class Vec2:
    def __init__(self, x, y):
        self.x, self.y = x, y;

class Ball:
    def __init__(self, color, pos: Vec2, vel: Vec2, radius: float):
        self.__color, self.__pos, self.__vel, self.__radius = color, pos, vel, radius;
    def tick(self, bounds):
        self.tickMovement(bounds);
        self.render();
    def tickMovement(self, bounds):
        self.__pos.x += self.__vel.x
        self.__pos.y += self.__vel.y
        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.__pos.x + self.__vel.x) > (bounds.x - self.__radius):
            self.__vel.x = -self.__vel.x
        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.__pos.y + self.__vel.y) > (bounds.y - self.__radius):
            self.__vel.y = -self.__vel.y
    def render(self):
        turtle.penup()
        turtle.color(self.__color)
        turtle.fillcolor(self.__color)
        turtle.goto(self.__pos.x, self.__pos.y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.__radius)
        turtle.end_fill()
class BallSystem:
    def __init__(self, bounds):
        self.__balls, self.__bounds = [], bounds;
    def addRandomBalls(self, numOfBalls):
        ball_radius = 0.05 * self.__bounds.x;
        for i in range(numOfBalls):
            self.__balls.append(Ball((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), Vec2(random.randint(-1*self.__bounds.x + ball_radius, self.__bounds.x - ball_radius), random.randint(-1*self.__bounds.y + ball_radius, self.__bounds.y - ball_radius)), Vec2(random.randint(1, 0.01*self.__bounds.x),random.randint(1, 0.01*self.__bounds.y)), ball_radius))
    def tick(self):
        for ball in self.__balls:
            ball.tick(self.__bounds);
