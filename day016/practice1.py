# from turtle import  Turtle,Screen


# tido = Turtle()
# print(tido)
# tido.shape("turtle")
# tido.color("cyan")
# tido.forward(100)

# my_screen = Screen() 
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
# print(table)
table.add_column("Pokemon Name", ["Pikachu", "Squire", "Charmander"])
table.add_column("Pokemon Name", ["Electric", "Water", "Fire"])
print(table)
