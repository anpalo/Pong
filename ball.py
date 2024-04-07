from turtle import Turtle
import random
import time

heading = [random.randint(10, 45), random.randint(135, 170), random.randint(190, 225), random.randint(315, 350)]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("greenyellow")
        self.shape("circle")
        self.shapesize(1)
        self.setheading(random.choice(heading))
        self.speed("slow")

    def move(self):
        self.forward(15)
        if self.ycor() > 280 or self.ycor() < -270:
            self.setheading(-self.heading())

    def reset_ball(self):
        time.sleep(2.0)
        self.goto(0, 0)




