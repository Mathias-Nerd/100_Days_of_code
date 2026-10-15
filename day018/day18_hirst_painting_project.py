#Mathias-Nerd
#Hirst painting project
import colorgram
import turtle
import random

turtle.colormode(255)

colour = [(item.rgb.r,item.rgb.g, item.rgb.b) for item in colorgram.extract('image.jpg', 30)]
print(colour)
tim = turtle.Turtle()
# tim.penup()
# print(tim.position())

# tim.forward(100)

# print(tim.position())f

tim.speed(5)
tim.penup()
tim.setpos(-300, -300)
tim.hideturtle()


# if -300 <= x <= 300 and -300 <= y <= 300:
while -300 <= tim.ycor() <= 300:
    tim.setx(-300)
    while -300 <= tim.xcor() <= 300:
        tim.color(random.choice(colour))
        # tim.pendown()
        tim.dot(20)
        # tim.penup()
        tim.forward(50)
    tim.sety(tim.ycor() + 50)
    
    
    








screen = turtle.Screen()
screen.exitonclick()