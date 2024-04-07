from turtle import Turtle

Y_POS = []
for nums in range(-300, 260, 40):
    Y_POS.append(nums)


class CenterLine:
    def __init__(self, x_pos):
        self.new_line = []
        self.x_pos = x_pos
        self.create_line()

    def create_line(self):
        for y in Y_POS:
            dash = Turtle()
            dash.hideturtle()
            dash.penup()
            dash.shapesize(1, .5)
            dash.color("gray10")
            dash.shape("square")
            dash.goto(self.x_pos, y)
            dash.showturtle()
