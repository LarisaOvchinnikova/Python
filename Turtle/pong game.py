import turtle
# import os  #for insert sound for apple
import winsound   # for windows
wn = turtle.Screen()
wn.title("Pong by Larisa")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)


# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
#перемещение мяча:
ball.dx = 1
ball.dy = -1



# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))



#Function
def paddle_a_up():
  y = paddle_a.ycor() # coordinate y
  y += 20
  paddle_a.sety(y)  #перемещ в новую координату

def paddle_a_down():
  y = paddle_a.ycor() # coordinate y
  y -= 20
  paddle_a.sety(y)  #перемещ в новую координату

def paddle_b_up():
  y = paddle_b.ycor() # coordinate y
  y += 20
  paddle_b.sety(y)  #перемещ в новую координату

def paddle_b_down():
  y = paddle_b.ycor() # coordinate y
  y -= 20
  paddle_b.sety(y)  #перемещ в новую координату

# Keyboard binding
wn.listen()  # слушать, что вводится на клавиатуре
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


#Mail game loop
while True:
  wn.update()  #update screen

  # Move the ball
  ball.setx(ball.xcor() + ball.dx)
  ball.sety(ball.ycor() + ball.dy)

  # Border checking
  if ball.ycor() > 290:
    ball.sety(290)
    ball.dy *= -1 # reverse direction of the ball
    # os.system("afplay bounce.wav") # on mac , file should be in the same folder
    winsound.PlaySound("sound.wav", winsound.SND_ASYNC) # for windows

  if ball.ycor() < -290:
    ball.sety(-290)
    ball.dy *= -1 # reverse direction of the ball
    # os.system("afplay bounce.wav")
    winsound.PlaySound("sound.wav", winsound.SND_ASYNC)  # for windows

  if ball.xcor() > 390:
    ball.goto(0, 0)
    ball.dx *= -1 # reverse direction of the ball
    score_a += 1
    pen.clear()
    pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

  if ball.xcor() < -390:
    ball.goto(0, 0)
    ball.dx *= -1 # reverse direction of the ball
    score_b += 1
    pen.clear()
    pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

  # #Paddle and ball collisions
  if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40 ):
    ball.setx(340)
    ball.dx *= -1
    # os.system("afplay bounce.wav")
    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)  # for windows

  if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40 ):
    ball.setx(-340)
    ball.dx *= -1
    # os.system("afplay bounce.wav")
    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)  # for windows