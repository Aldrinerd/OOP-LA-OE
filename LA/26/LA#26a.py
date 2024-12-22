from turtles import Leonardo, Michaelangelo, Donatello, Raphael
turtle1 = Leonardo("Leonardo","Leo")
turtle2 = Michaelangelo("Michaelangelo","Mikey")
turtle3 = Donatello("Donatello","Donny")
turtle4 = Raphael("Raphael","Raph")
for turtle in (turtle1,turtle2,turtle3,turtle4):
    print(turtle.name)
