# import turtle
# t = turtle.Pen()
# t.down()
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.backward(100)
# t.left(90)
# t.forward(50)
# t.up()
# t.left(90)
# t.forward(50)
# t.down()
# t.right(135)
# t.forward(70)
# t.up()
# t.backward(70)
# t.right(90)
# t.down()
# t.forward(70)  # roof is ready

#
# t.goto(0,0)
# t.pensize(5)
# t.pencolor("red")
# t.circle(100)

# t.home() # Move turtle to the origin – coordinates (0,0)

# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()


# import turtle

# # The screen has coordinates that go from -150 to 150 in the x (horizontal) and y
# # (vertical) directions.

# t = turtle.Pen()  # t - name of turtle
# t.shape("turtle")  # shape of turtle
# # t.color("green")  # turtle color
# t.speed(6) # turtle's speed from 1 to 100
# # t.pensize(5)
# t.width(5)
# t.begin_fill()
# t.circle(50)
# t.end_fill()

# t.color('red', 'yellow')
# # t.begin_fill()
# t.circle(50)
# # t.end_fill()
# t.up()
# t.goto(-150,0)  # setpos(x,y), setposition(x,y)
# t.down()
# t.fd(300)  # turtle.forward(300)
# t.bk(150)  # t.backward(150)
# t.rt(90)   # t.right(angle)
# t.fd(150)
# # t.bk(150)

# t.setx(0)  # Set the turtle’s first coordinate to x, leave second coordinate unchanged.
# t.sety(0)
# t.home() #Move turtle to the origin – coordinates (0,0)
# t.circle(120, 90)  # draw a semicircle дуга рад.120 угол 90
# t.left(90)
# t.fd(240)
# t.left(90)
# t.circle(120, 90)
# # turtle.dot(50, "red")


# for i in range(4):
#   turtle.fd(50); turtle.lt(80)
#   turtle.fd(50); turtle.lt(80)

# for i in range(8):
#   turtle.undo() # отмена действия

# шестиугольники по спирали
# x = 10
# for i in range(30):
#   turtle.fd(x); turtle.left(60)
#   x+=5




# import turtle
# t = turtle.Pen()  # t - name of turtle
# t.shape("turtle")  # shape of turtle
# t.width(5)
# t.color("green")  # turtle color
# t.up()

# t.down()
# t.begin_fill()
# t.circle(50)
# t.end_fill()
# t.up()
# t.left(90)
# t.fd(25)
# t.down()
# t.fillcolor("white")
# t.begin_fill()
# t.circle(30)
# t.end_fill()

#ring!! in (0,0) width 10
# import turtle
# t = turtle.Pen()  # t - name of turtle
# t.shape("turtle")  # shape of turtle  ['arrow', 'blank', 'circle', ..., 'turtle']
# t.color("green")
# t.up()
# t.sety(-50)
# t.down()
# t.begin_fill()
# t.circle(50)
# t.up()
# t.sety(-40)
# t.down()
# t.circle(40)
# t.end_fill()

# t.up()
# t.goto(-100, -50)
# # t.color("yellow")
# turtle.colormode(255)

# tup = (0, 255, 255)
# t.color(tup)

# t.down()
# t.begin_fill()
# t.circle(50)
# t.up()
# t.sety(-40)
# t.down()
# t.circle(40)
# t.end_fill()


import turtle

turtle.colormode(255)

t = turtle.Pen()  # t - name of turtle
# t.speed(100)
# t.goto(-150,-150)
# y=-150
# r, g, b = 0, 0, 0
# for i in range(255):
#   t.color(r,g,b )
#   t.fd(300)
#   r+=1
#   y+=1
#   t.goto(-150,y )
# for i in range(3, 10):
#   for j in range(i):
#     t.fd(50)
#     t.left(360//i)


# лабиринт
# dist = 2
# for i in range(200):
#   t.fd(dist)
#   t.rt(60)
#   dist+=2

from random import randint
t.pensize(5)
dist = 100
for i in range(36):
  r = randint(0,255)
  g= randint(0,255)
  b = randint(0,255)
  t.color(r,g,b)
  t.fd(dist); t.rt(90)
  t.fd(dist); t.rt(90)
  t.fd(dist); t.rt(90)
  t.fd(dist); t.rt(90)
  t.rt(10)