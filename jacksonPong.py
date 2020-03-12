import turtle as t
import time
import sys
import winsound
import random

class ball:
    def __init__(self, speed, color, dX, dY, shape, startX, startY):
        self.speed = speed
        self.color = color
        self.dX = dX
        self.dY = dY
        self.shape = shape
        self.startX = startX
        self.startY = startY

class paddle(Object.t):
    def __init__(self, speed, shape, color, stretch_wid, stretch_len, startX, startY):
        super().__init__(shape='circle', visible = true)
        self = t.Turtle()
        self.speed(self.speed)
        self.shape(self.shape)
        self.color(self.color)
        self.shapesize(stretch_wid=self.stretch_wid, stretch_len = self.stretch_len)
        self.penup()
        self.goto(self.startX, self.startY)


p1Score = 0
p2Score = 0
p = 0



window = t.Screen()
window.title("Pong by Hawken")
window.bgcolor("black")
window.setup(width = 800, height = 600)
window.tracer(0)

pA = paddle(0, "square", "white", 5, 1, -350, 0)
print(type(pA))
#paddle a


pB = paddle(0, "square", "white", 5, 1, 350, 0)

#paddle b
'''paddle_b = t.Turtle()
paddle_b.speed(pB.speed)
paddle_b.shape(pB.shape)
paddle_b.color(pB.color)
paddle_b.shapesize(stretch_wid= pB.stretch_wid, stretch_len = pB.stretch_len)
paddle_b.penup()
paddle_b.goto(pB.startX, pB.startY)'''

b = ball(10, "white", 4, -4, "square", 0, 0)

#ball
ball = t.Turtle()
ball.speed(b.speed)
ball.shape(b.shape)
ball.color(b.color)
ball.penup()
ball.goto(b.startX, b.startY)
ball.dx = b.dX
ball.dy = b.dY

'''
#function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)



def pause_game():
    global p
    p = 5

window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_down, "Down")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(pause_game, "space")


#Game Loop

while True:
    

        window.update()

        t.clear()

        t.color('white')
        style = ('Courier', 50, 'bold')
        t.write(str(p1Score) + "-" + str(p2Score), font=style, align='center')
        t.hideturtle()

        

        time.sleep(0.01)

        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        while p > 0:
            time.sleep(1)
            p -= 1
        #This is to keep the paddles in
        if paddle_b.ycor() > 250:
            paddle_b.sety(250)

        if paddle_b.ycor() < -250:
            paddle_b.sety(-250)

        if paddle_a.ycor() > 250:
            paddle_a.sety(250)

        if paddle_a.ycor() < -250:
            paddle_a.sety(-250)

        
        #This is for collision on the walls
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    
        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1

            p1Score += 1

            winsound.PlaySound("Boo.wav", winsound.SND_ASYNC)

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1

            p2Score += 1

            winsound.PlaySound("Boo.wav", winsound.SND_ASYNC)

        #This is paddle collision detetcion
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
            ball.setx(340)
            ball.dx *= -1
            ball.dy *= 1

            #if ball.ycor() > paddle_b.ycor() + 15 or ball.ycor() < paddle_b.ycor() - 15:
                #ball.dy = 0

            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
            ball.setx(-340)
            ball.dx *= -1
            ball.dy *= 1

            #if ball.ycor() > paddle_a.ycor() + 15 or ball.ycor() < paddle_a.ycor() - 15:
                #ball.dy = 0

            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        
    
'''
