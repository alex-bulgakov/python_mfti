import turtle as turtle


def print_square(size):
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)


def print_square_spiral(steps, length, offset):
    for i in range(steps):
        turtle.forward(l)
        turtle.left(90)
        length += offset


def print_ngon(n, size):
    for i in range(n):
        turtle.forward(size)
        turtle.left(360/n)


def draw_color_circle(color, size):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()


def set_position(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def draw_star(vertices):
    turtle.color('red', 'yellow')
    turtle.begin_fill()
    while True:
        turtle.forward(200)
        turtle.right(180 - 360/(vertices*2))
        if abs(turtle.posx()) < 1:
            break
    turtle.end_fill()
    turtle.done()


# turtle.speed(10)
# turtle.pen(shown=False)
# setPosition(0, -100)
# drawColorCircle("yellow", 200)
#
# setPosition(100, 120)
# drawColorCircle("blue", 30)
# setPosition(-100, 120)
# drawColorCircle("blue", 30)
#
# setPosition(0, 100)
# turtle.pensize(20)
# turtle.left(-90)
# turtle.forward(50)
#
# setPosition(-100, 50)
# turtle.pencolor("red")
# turtle.circle(100, 180)
#
# sleep(5)


#
# rad1 = 50
# rad2 = 10
# turtle.left(90)
# for i in range (20):
#     turtle.circle(-rad1, 180)
#     turtle.circle(-rad2, 180)

# rad = 50
# turtle.left(90)
# turtle.speed(10)
# for i in range (20):
#     turtle.circle(rad)
#     turtle.circle(rad*(-1))
#     rad += 10


# for i in range(10):
#     rad = 100
#     if i % 2 == 0:
#         rad *= -1
#     turtle.circle(rad)
#     turtle.left(360/10)
#
# sleep(2)


# x = 0
# y = 0
# for i in range(3, 13):
#     printNGon(i, 100 + i * 10)
#     turtle.penup()
#     turtle.goto(x, y)
#     turtle.pendown()
#     # x -= 100
#     y -= 20
#
# sleep(2)

# turtle.speed(10)
# printSquareSpiral(20, 0, 0)
# sleep(2)

# n = 365
# turtle.speed(1)
# # turtle.shape('turtle')
# for i in range(n):
#     turtle.forward((1/(2*math.pi))*i)
#     turtle.left(40)




# x = 0
# y = 0
# for i in range (10, 1000, 10):
#     printSquare(i)
#     turtle.penup()
#     turtle.goto(x, y)
#     turtle.pendown()
#     x -= 5
#     y -= 5
