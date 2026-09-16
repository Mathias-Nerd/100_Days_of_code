#100 Days of Code with Python
#Author: Mathias Nerd
#Hurdles 1
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
i = 6
while i > 0:
    hurdle()
    i -= 1
