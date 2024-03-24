from turtle import *


# we want to paint a house

 #step 1: draw a spuare    

width(7)
color("blue")
begin_fill()
begin_fill()
forward(200)
left(90)
forward(200)      
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(70)
left(90)
end_fill()
#end of spuare

#drawing a door

color("red")
begin_fill()
forward(100)
right(90)
forward(50)
right(90)
forward(100)
end_fill()
#end of door

penup()
goto(200, 200)

pendown()

color("yellow")
begin_fill()
right(150)
forward(200)
left(120)
forward(200) 
end_fill()

penup()
goto(120, 165)
pendown()


begin_fill()
left(30)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
end_fill()
forward(50)
penup()
goto(70, 165)
pendown()


begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()




exitonclick()


