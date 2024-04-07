from turtle import Turtle

ALIGNMENT = "center"
SCORE_FONT = ("courier", 40, "normal")
CENTER_FONT = ("courier",20 , "normal")
class Scoreboard(Turtle):
    def __init__(self, x_pos, y_pos, color):
        super().__init__()
        self.penup()
        self.color(color)
        self.goto(x_pos, y_pos)
        self.score = 0
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.score}", align=ALIGNMENT, font=SCORE_FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def middle_card(self):
        self.clear()
        self.write("Scoreboard", align=ALIGNMENT, font=SCORE_FONT)




