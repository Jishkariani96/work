from turtle import *

color ("purple")
width(5)
speed(7)

#starting cube
forward (200)
left (90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
#cube done

#start making a door

left (90)
forward(70)
color("black")
begin_fill()
left(90)
forward(120)
right(90)
forward(70)
right(90)
forward(120)
end_fill ()
#door done, now start making roof
penup()
goto(200, 200)
pendown()
color('red')
begin_fill()
left (240)
forward (120)
left(60)
forward(115)
end_fill()
#roof done

#start windows
color("yellow")

penup()
goto (25,25)
pendown()
right (120)
forward(125)
right(90)
forward(25)
right(90)
forward(125)
right(90)
forward(25)

penup()
goto (155,25)
pendown()
right (90)
forward(125)
right(90)
forward(26)
right(90)
forward(125)
right(90)
forward(26)
#done!


exintonclick()
