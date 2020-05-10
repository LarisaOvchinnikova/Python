from turtle import *
t = Turtle()
t.screen.setup(800, 800)
for i in range(20):
    t.fd(8)
    t.up()
    t.fd(8)
    t.down()
t.left(90)
t.fd(100)
t.left(90)
t.fd(200)
t.screen.exitonclick()
t.screen.mainloop()