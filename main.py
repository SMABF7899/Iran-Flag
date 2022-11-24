from turtle import *

run_speed = 5
def Alaho_Akbar(num1, num2):
    color("white")
    speed(run_speed + 10)
    up()
    setpos(- num1 + 540, 0 - num2)
    down()
    begin_fill()
    forward(1 * 5)
    right(90)
    forward(5 * 5)
    right(90)
    forward(5 * 5)
    right(90)
    forward(2 * 5)
    left(90)
    forward(3 * 5)
    left(90)
    forward(1 * 5)
    left(90)
    forward(2 * 5)
    right(90)
    forward(1 * 5)
    right(90)
    forward(3 * 5)
    right(90)
    forward(3 * 5)
    right(90)
    forward(4 * 5)
    left(90)
    forward(2 * 5)
    right(90)
    forward(1 * 5)
    right(90)
    forward(4 * 5)
    left(90)
    forward(1 * 5)
    left(90)
    forward(4 * 5)
    right(90)
    forward(1 * 5)
    right(90)
    forward(4 * 5)
    left(90)
    forward(1 * 5)
    left(90)
    forward(4 * 5)
    end_fill()
    up()
    setpos(-5 * 5 - num1 + 540, 0 - num2)
    down()
    begin_fill()
    left(90)
    forward(13 * 5)
    left(90)
    forward(1 * 5)
    left(90)
    forward(13 * 5)
    left(90)
    forward(1 * 5)
    end_fill()
    up()
    setpos(-9 * 5 - num1 + 540, -2 * 5 - num2)
    down()
    begin_fill()
    left(180)
    forward(3 * 5)
    right(90)
    forward(5 * 5)
    right(90)
    forward(2 * 5)
    left(90)
    forward(3 * 5)
    left(90)
    forward(2 * 5)
    right(90)
    forward(1 * 5)
    right(90)
    forward(3 * 5)
    right(90)
    forward(5 * 5)
    right(90)
    forward(2 * 5)
    left(90)
    forward(3 * 5)
    left(90)
    forward(1 * 5)
    left(90)
    forward(2 * 5)
    right(90)
    forward(1 * 5)
    right(90)
    forward(3 * 5)
    end_fill()
    up()
    setpos(-15 * 5 - num1 + 540, -5 * 5 - num2)
    down()
    begin_fill()
    left(90)
    forward(1 * 5)
    left(90)
    forward(1 * 5)
    left(90)
    forward(1 * 5)
    left(90)
    forward(1 * 5)
    end_fill()


def Alef_Up():
    pen(pensize=4)
    forward(50)
    left(90)
    forward(10)
    right(180)
    forward(10)
    left(90)
    forward(50)
    left(90)
    forward(10)
    right(180)
    forward(10)
    left(90)


def Alef_Down():
    forward(50)
    right(90)
    forward(10)
    right(180)
    forward(10)
    right(90)
    forward(50)
    right(90)
    forward(10)
    right(180)
    forward(10)
    right(90)


drawing_area = Screen()
drawing_area.setup(width=1500, height=1500)
hideturtle()
speed(run_speed)

color("green")
begin_fill()
up()
setpos(553, 120)
down()
left(90)
forward(230)
left(90)
forward(1111)
left(90)
forward(230)
left(90)
forward(1111)
end_fill()

color("red")
begin_fill()
up()
setpos(553, -345)
down()
left(90)
forward(230)
left(90)
forward(1111)
left(90)
forward(230)
left(90)
forward(1111)
end_fill()

for i in range(11):
    Alaho_Akbar(i * 100, -150)
for i in range(11):
    Alaho_Akbar(i * 100, 120)

up()
setpos(547.5, 121)
down()
color("green")
right(180)
for i in range(11):
    Alef_Up()

up()
setpos(547.5, -117)
down()
color("red")
for i in range(11):
    Alef_Down()

pen(pensize=7)
color("green")
up()
setpos(550, 121)
down()
left(90)
forward(10)
up()
setpos(-555, 121)
down()
forward(10)

up()
setpos(550, -117)
down()
color("red")
right(180)
forward(10)
up()
setpos(-555, -117)
down()
forward(10)
drawing_area.addshape("iran.gif")
Turtle().shape("iran.gif")
exitonclick()
