from turtle import Turtle
import random

BRANCH_LENGTH = 200
branch_headings_list = [0,180]
MOVE_DISTANCE = 40

class Branch():
    def __init__(self):
        self.branch_list = []
        self.move_distance = MOVE_DISTANCE
        self.difficulty = 50

    # creating object branch and appending it to branch_list[]
    def create_branch(self):
        random_chance = random.randint(0,self.difficulty)
        if random_chance == 1 or random_chance == 2 or random_chance == 3 or random_chance == 4 or random_chance == 5 or random_chance == 6 or random_chance == 7 or random_chance == 8 or random_chance == 9 or random_chance == 10:
            new_branch = Turtle()
            new_branch.hideturtle()
            new_branch.pensize(5)
            new_branch.goto(0, 330)
            new_branch.setheading(random.choice(branch_headings_list))
            new_branch.forward(BRANCH_LENGTH)
            self.branch_list.append(new_branch)
        self.move_branch()
    # loops through branch_list[] and moves it MOVE_DISTANCE lower
    def move_branch(self):
        for branches in self.branch_list:
            new_y = branches.ycor()
            new_y -= MOVE_DISTANCE
            branches.goto(0,new_y)
            branches.clear()
            branches.forward(BRANCH_LENGTH)


