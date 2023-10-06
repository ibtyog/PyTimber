from turtle import Turtle

# creating tree center
class Tree(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pensize(10)
        self.goto(0,-300)
        self.goto(0,300)


