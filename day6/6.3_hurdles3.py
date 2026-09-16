#100 Days of Code with Python
#Author: Mathias Nerd
#Hurdle 3
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        hurdle()
    else:
        move()
