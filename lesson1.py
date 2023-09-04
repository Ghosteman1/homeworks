from turtle import *
#start drawing a house

speed (8)
width (3)
color ("blue")
penup()
goto (0, 0)
pendown ()
forward (140)
left (90)
forward (140)
left (90)
forward (140)
left (90)
forward (140)
left(90)
forward (50)
left(90)

#door
color ("yellow")
begin_fill()
forward (70)
right (90)
forward (40)
right(90)
forward (70)
end_fill()

#windows
penup()
goto(140, 115)
pendown()
width(1)
color ("blue")
right (90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)


#windows
penup()
goto (0, 115)
pendown()
forward(40)
right(90)
forward(40)
right(90)
forward(40)

#roof
penup()
goto (140, 140)
pendown()
width(3)
color("red")
begin_fill()
right(55)
forward(120)
left(108)
forward(120)
end_fill()

#roof
color ("red")
begin_fill()
right(53)
forward(120)
right(120)
forward(109)
right(60)
forward(138)
end_fill()

#House
penup()
goto (-120, 140)
pendown()
color ("blue")
right(90)
forward(140)
left(90)
forward(120)

#door
penup()
goto(-40, 0)
pendown()
color("yellow")
begin_fill()
left(90)
forward(70)
left(90)
forward(40)
left(90)
forward (70)
end_fill()

penup()
goto (-120, 140)
pendown()
color("blue")
left(90)
forward(125)






exitonclick ()