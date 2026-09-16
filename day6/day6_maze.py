#100 Days of Code with Python
#Author: Mathias Nerd
#Maze
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
#To avoid infinite loop
while front_is_clear():
    move()
turn_left()

#The main logic
#1. if right is clear to right
#2. otherwise if front is clear go front
#3. otherwise turn left
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
    

