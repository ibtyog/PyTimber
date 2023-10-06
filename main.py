from turtle import Turtle, Screen
from tree import Tree
from branch import Branch
from player import Player
from scoreboard import Scoreboard
import time
# screen setup
screen = Screen()
screen.setup(400,600)
screen.tracer(0)
screen.listen()
screen.title("turtleman")
# creating objects
tree = Tree()
branch = Branch()
timber = Player()
scoreboard = Scoreboard()
# assigning multiple class methods to one key
def left_arrow():
    timber.left_cut()
    branch.create_branch()
    scoreboard.add_score()
def right_arrow():
    timber.right_cut()
    branch.create_branch()
    scoreboard.add_score()
screen.onkey(left_arrow, "Left")
screen.onkey(right_arrow, "Right")
# last change => every 5 score games gets harder,
# last change is here to prevent looping if player stays still on same level (like 1,6,11, etc.)
last_change = 1

# main gameplay script
game_on = True
while game_on:
    screen.update()
    time.sleep(0.01)
# game cannot get harder than (chance of creating a branch 10 out of 15 - starting with 10 out of 50)
    if branch.difficulty > 15:
        # every 5 score gets harder (explained in last_change)
        if scoreboard.score % 5 == 1 and last_change != scoreboard.score:
            print("made it harder")
            last_change = scoreboard.score
            branch.difficulty -= 1
    # checks colliding with branch
    for branches in branch.branch_list:
        if timber.distance(branches) < 181:
            game_on = False
# post-game end screen
screen.clear()
scoreboard.game_over()
screen.exitonclick()
