import turtle
 
class Window:
     
    def __init__(self, width, height, bgc, title):
        
        self.width = width
        self.height = height
        self.bgc = bgc
        self.title = title
        self.window = turtle.Screen()
        self.window.bgcolor(bgc)
        self.window.title(title)
        self.window.setup(width=self.width, height=self.height)
         
class Paddle:
     
    def __init__(self, color, posx, posy, shape="square", width=5, len=1):
     
        self.shape = shape
        self.color = color
        self.posx = posx
        self.posy = posy
        self.width = width
        self.len = len
         
        self.paddle = turtle.Turtle()       
        self.paddle.speed(0)
        self.paddle.shape(self.shape)
        self.paddle.color(self.color)
        self.paddle.shapesize(stretch_wid=self.width,stretch_len=self.len)
        self.paddle.penup()
        self.paddle.goto(self.posx, self.posy)
         
    def paddle_up(self):
         
        y = self.paddle.ycor()
        if y < 245:
            y += 30
            self.paddle.sety(y)
     
    def paddle_down(self):
         
        y = self.paddle.ycor()
        if y > -245:
            y -= 30
            self.paddle.sety(y)
             
class Ball:
     
    def __init__(self, color, vx=4, vy=4, shape="square", posx=0, posy=0):
         
        self.shape = shape
        self.color = color
        self.vx = vx
        self.vy = vy
        self.posx = posx
        self.posy = posy    
         
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape(self.shape)
        self.ball.color(self.color)
        self.ball.penup()
        self.ball.goto(self.posx, self.posy)
 
class Score:
         
    score_1 = 0
    score_2 = 0
     
    def __init__(self, color, posx, posy, shape="square"):
        self.color = color
        self.posx = posx
        self.posy = posy
        self.shape = shape
         
        self.score = turtle.Turtle()
        self.score.speed(0)
        self.score.shape(self.shape)
        self.score.color(self.color)
        self.score.penup()
        self.score.goto(self.posx, self.posy)
        self.score.hideturtle()
        self.score.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))        
 
         
win = Window(800, 600, "white", "Pong")
paddle_1 = Paddle("cyan", -350, 0)
paddle_2 = Paddle("cyan", 350, 0)
b = Ball("orange", vx=6,vy=6)
s = Score("orange", 0, 260)
 
win.window.listen()
win.window.onkeypress(paddle_1.paddle_up, "w")
win.window.onkeypress(paddle_1.paddle_down, "s")
win.window.onkeypress(paddle_2.paddle_up, "Up")
win.window.onkeypress(paddle_2.paddle_down, "Down")
 
while True:
 
    win.window.update()
     
    b.ball.setx(b.ball.xcor() + b.vx)
    b.ball.sety(b.ball.ycor() + b.vy)
     
    if b.ball.ycor() > 250:
        b.vy *= -1
     
    if b.ball.ycor() < -280:
        b.vy *= -1
         
    if b.ball.xcor() > 400:
        s.score_1 += 1
        s.score.clear()
        s.score.write("Player 1: {}  Player 2: {}".format(s.score_1, s.score_2), align="center", font=("Courier", 24, "normal"))
        b.ball.goto(0, 0)
        b.vx *= -1
         
    elif b.ball.xcor() < -400:
        s.score_2 += 1
        s.score.clear()
        s.score.write("Player 1: {}  Player 2: {}".format(s.score_1, s.score_2), align="center", font=("Courier", 24, "normal"))
        b.ball.goto(0, 0)
        b.vx *= -1
     
     
    if b.ball.xcor() < -330 and b.ball.ycor() < paddle_1.paddle.ycor() + 50 and b.ball.ycor() > paddle_1.paddle.ycor() - 50:
        b.vx *= -1
     
    elif b.ball.xcor() > 330 and b.ball.ycor() < paddle_2.paddle.ycor() + 50 and b.ball.ycor() > paddle_2.paddle.ycor() - 50:
        b.vx *= -1
     
