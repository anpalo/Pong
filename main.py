from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
import time
from screen_decorate import CenterLine
from scoreboard import Scoreboard


screen = Screen()
screen.title("Pong Puh Pong Pong Pong")
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.tracer(0)
esc_window = Screen()


def exit_program():
    esc_window.bye()


def close_window():
    close = Turtle()
    close.speed(0)
    close.color("red")
    close.penup()
    close.hideturtle()
    close.goto(0, 0)
    close.write("Press ESC again to exit", align="center", font = ("Courier", 24, "normal"))
    esc_window.listen()
    esc_window.onkeypress(exit_program, "Escape")


center_line = CenterLine(0)
ball = Ball()
right_paddle = Paddle(372, "white")
left_paddle = Paddle(-380, "white")
scoreboard = Scoreboard(0, 250, "white")
scoreboard.middle_card()
left_score = Scoreboard(-250, 250, "white")
right_score = Scoreboard(250, 250, "white")

screen.listen()
screen.onkey(right_paddle.move_up, 'Up')
screen.onkey(right_paddle.move_down, 'Down')
screen.onkey(left_paddle.move_up, 'w')
screen.onkey(left_paddle.move_down, 's')
screen.onkey(ball.reset, "r")
esc_window.listen()
esc_window.onkeypress(close_window, "Escape")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.057)
    ball.move()
    for paddle in right_paddle.new_paddle:
        if paddle.distance(ball) < 20:
            ball.setheading(180 - ball.heading())
            ball.move()
    for paddle in left_paddle.new_paddle:
        if paddle.distance(ball) < 20:
            ball.setheading(180 - ball.heading())
            ball.move()
    if ball.xcor() > 390:
        print("game is over")
        left_score.increase_score()
        ball.reset_ball()
    if ball.xcor() < -400:
        print("game is over")
        right_score.increase_score()
        ball.reset_ball()

# screen.exitonclick()
screen.mainloop()