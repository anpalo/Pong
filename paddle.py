from turtle import Turtle

Y_POSITIONS = [70, 50, 30, 10, -10, -30, -50, -70]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle():
    def __init__(self, pos_x, color):
        self.new_paddle = []
        self.create_paddle(pos_x, color)
        self.head = self.new_paddle[0]
        self.tail = self.new_paddle[-1]

    def create_paddle(self, x_pos, color):
        for y_pos in Y_POSITIONS:
            new_segment = Turtle()
            new_segment.hideturtle()
            new_segment.penup()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.goto(x_pos, y_pos)
            new_segment.color(color)
            new_segment.showturtle()
            self.new_paddle.append(new_segment)

    def move_up(self):
        self.head.setheading(UP)
        if self.head.ycor() < 280:
            for seg_num in range(len(self.new_paddle)-1, 0, -1):
                new_y = self.new_paddle[seg_num - 1].ycor()
                self.new_paddle[seg_num].goto(self.new_paddle[seg_num].xcor(), new_y)
            self.head.forward(MOVE_DISTANCE)

    def move_down(self):
        self.tail.setheading(270)
        if self.tail.ycor() > -275:
            for seg_num in range(0, len(self.new_paddle)-1):
                new_y = self.new_paddle[seg_num +1].ycor()
                self.new_paddle[seg_num].goto(self.new_paddle[seg_num].xcor(), new_y)
            self.tail.forward(MOVE_DISTANCE)

