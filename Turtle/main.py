import keywords
import turtle

def create_bricks():
    x, y = -300, 300
    bricks = []
    for _ in range(3):
        for i in range(3):
            brick = turtle.Turtle()
            brick.hideturtle()
            brick.shape("brick.gif")
            brick.up()
            brick.setx(x)
            brick.sety(y)
            brick.showturtle()
            x += 300
            bricks.append(brick)
        x = -300
        y -= 80
    return bricks


def goleft():
    x = rocket.xcor()
    if x >= -(turtle.window_width() / 2 - 105):
        rocket.setx(x - 25)

def goright():
    x = rocket.xcor()
    if x <= (turtle.window_width() / 2 - 105):
        rocket.setx(x + 25)


s = turtle.Screen()
ball = turtle.Turtle()
rocket = turtle.Turtle()
width = 1072
height = 1070

s.setup(width + 4, height + 8)  # fudge factors due to window borders & title bar

s.addshape("rocket.gif")
rocket.shape("rocket.gif")
s.addshape("brick.gif")
ball.shape("circle")
ball.color("green")
rocket.resizemode("auto")

rocket.up()
ball.up()
ball.speed(3)
rocket.goto(0, -300)


x, y = 0, 0
xdir, ydir = 10, 10
xlimit, ylimit = turtle.window_width() / 2, turtle.window_height() / 2

bricks = create_bricks()



while True:
    s.listen()
    s.onkey(goleft, "Left")
    s.onkey(goright, "Right")
    x += xdir
    y += ydir
    if ball.ycor() <= -turtle.window_height() / 2 + 10:
        del ball
        ball = turtle.Turtle()
        ball.up()
        ball.shape("circle")
        ball.color("green")
        ball.setx(0)
        ball.sety(0)
        x, y = 0, 0
        ydir = -ydir

    if rocket.xcor() - 100 < ball.xcor() < rocket.xcor() + 100 and ball.ycor() < rocket.ycor() + 31:
        y = (rocket.ycor() + 50)
        ydir = -ydir

    if not -xlimit < x < xlimit:
        xdir = -xdir
    if not -ylimit < y < ylimit:
        ydir = -ydir

    for brick in bricks:
        if brick.xcor() - 100 < ball.xcor() < brick.xcor() + 100 and \
                brick.ycor() - 60 < ball.ycor() < brick.ycor() + 60 and brick.isvisible():
            brick.hideturtle()
            del brick
            ydir = -ydir

    ball.goto(x, y)
    s.update()
