from turtle import Turtle
Y_POS = -270
LEFT = -20
RIGHT = 20
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto(20, Y_POS)

# cutting tree from specific side
    def left_cut(self):
        self.goto(LEFT, Y_POS)
    def right_cut(self):
        self.goto(RIGHT,Y_POS)