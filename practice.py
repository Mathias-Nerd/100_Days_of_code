import turtle
import random
import colorgram 

timmy = turtle.Turtle()
# timmy.shape("turtle")
turtle.colormode(255)

#Number 1
#Drawing a square
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)



#Number 2
#Lifting up and droping pen while moving
# for _ in range(5):
#     timmy.forward(20)
#     timmy.pu()
#     timmy.forward(20)
#     timmy.pd()




#Number 3
#draw from triangle to pentagon
# for i in range(3,11):
#     timmy.color(random.choice(color))
#     angle = ((i - 2) * 180) / i
#     for j in range(i):
#         timmy.forward(100)
#         timmy.right(180-angle)




#Number 4
#walking randomly

#Afunction that generates the tuple to be used for RGB number
def generate_colour():
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    colour_number = (r,g,b)
    return colour_number

# timmy.pensize(12)
# timmy.speed(10)
# direction = [0, 90, 180, 270]
# for i in range(200):
#     timmy.pencolor(generate_colour())
#     # timmy.speed(10)
#     timmy.right(random.choice(direction))
#     # timmy.speed(2)
#     timmy.forward(20)
    
#Number 5:Project
timmy.speed("fastest")
for i in range(36*2):
    timmy.color(generate_colour())
    timmy.circle(100)
    timmy.left(5)




screen = turtle.Screen()
screen.exitonclick()
