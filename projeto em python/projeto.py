import turtle

wn = turtle.Screen()
wn.title("jogo do pong")
wn.bgcolor("grey")
wn.setup(width=800, height=600)
wn.tracer(0)

#player A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#player B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# boll
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.20
ball.dy = 0.20

# function

#cima
def paddle_a_up():
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)

#baixo
def paddle_a_donw():
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)



def paddle_b_up():
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)

#baixo
def paddle_b_donw():
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)


# keyboard

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_donw, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_donw, "Down")



# meu jogo de loop
while True:
    wn.update()


    # movimentação da bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)