#car = CarBlueprint()
# ^^      ^^  Class
# ^^ Object





# import module
# print(module.variable)





# from turtle import Turtle, Screen
# timmy = Turtle()
# #print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
# screen = Screen()
# print(screen.canvheight)
# print(screen.canvwidth)
# screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)