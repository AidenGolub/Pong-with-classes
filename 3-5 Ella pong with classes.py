#initial setup
import turtle
import time
import os
import winsound


window=turtle.Screen()
window.title("Pong by Ella")
window.bgcolor("gray")
window.setup(width=800, height=600)
window.tracer(0)

#Score
score_a=0
score_b=0



#Paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
class P:
	def __init__(self, speed, shape, color, shapesize, penup, goto):
		P=turtle.Turtle()
		self.speed=speed
		self.shape=shape
		self.color=color
		self.shapesize=shapesize
		self.penup=penup
		self.goto=goto
paddle_a=P(0, "square", "blue", (stretch_wid=5, stretch_len=1), (), (-350, 0))
paddle_b=P(0, "square", "blue", (stretch_wid=5, stretch_len=1), (), (350, 0))

#Paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

class B(turtle.Turtle):
	def __init__(self, spd, shp, clr, gtx, gty, deltax, deltay):
#		super().__init__(speed=spd, shape=shp, color=clr, goto=gt, dx=deltax, dy=deltay)
		super().__init__()
		self.turtle=turtle.Turtle()
		self.turtle.speed=spd
		self.turtle.color=clr
		self.turtle.goto(gtx, gty)
		self.penup()

ball=B(0, "circle", "red", 0, 0, 2, -2)



# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


#Function
def paddle_a_up():
	y=paddle_a.ycor()
	y+=20
	paddle_a.sety(y)

	
def paddle_a_down():
	y=paddle_a.ycor()
	y-=20
	paddle_a.sety(y)
	
def paddle_b_up():
	y=paddle_b.ycor()
	y+=20
	paddle_b.sety(y)

def paddle_b_down():
	y=paddle_b.ycor()
	y-=20
	paddle_b.sety(y)

def paddle_b_bottom ():
	paddle_b.ycor-40

def paddle_b_top ():
	paddle_b.ycor+40

def paddle_a_bottom ():
	paddle_a.ycor-40
	
def paddle_a_top ():
	paddle_a.ycor+40
	
def pause():
	time.sleep(5)

#Keyboard Binding
window.listen()
window.onkeypress(paddle_a_up,"w")
window.onkeypress(paddle_a_down,"s")
window.onkeypress(paddle_b_up,"Up")
window.onkeypress(paddle_b_down,"Down")
window.onkeypress(pause," ")

#Main game loop
while True:
	window.update()
	
	time.sleep(0.01)
	#Move the ball
	ball.setx(ball.xcor()+ball.dx)
	ball.sety(ball.ycor()+ball.dy)
	
	#Border checking
	if paddle_a.ycor()>290:
		paddle_a.sety(290)
		
	if paddle_b.ycor()>290:
		paddle_b.sety(290)
		
	if paddle_a.ycor()<-290:
		paddle_a.sety(-290)
		
	if paddle_b.ycor()<-290:
		paddle_b.sety(-290)
		
	if ball.ycor()>290:
		ball.sety(290)
		ball.dy *= -1
		winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
		
	if ball.ycor()<-290:
		ball.sety(-290)
		ball.dy *= -1
		winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
		
	if ball.xcor()>390:
		ball.goto(0, 0)
		ball.dx*=-1
		score_a+=1
		pen.clear()
		pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
		winsound.PlaySound("twitch.wav", winsound.SND_ASYNC)
		
	if ball.xcor()<-390:
		ball.goto(0, 0)
		ball.dx*=-1
		score_b+=1
		pen.clear()
		pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
		winsound.PlaySound("twitch.wav", winsound.SND_ASYNC)
		
	#paddle and ball collisions
	if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+50 and ball.ycor()>paddle_b.ycor() -50):
		ball.setx(340)
		ball.dx*=-1
		winsound.PlaySound("jump.wav", winsound.SND_ASYNC)
		
	if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor()+50 and ball.ycor()>paddle_a.ycor() -50):
		ball.setx(-340)
		ball.dx*=-1
		winsound.PlaySound("jump.wav", winsound.SND_ASYNC)
		



