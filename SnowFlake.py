import turtle

def kochflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3
        kochflake(t, order-1, size)
        t.left(60)
        kochflake(t, order-1, size)
        t.right(120)
        kochflake(t, order-1, size)
        t.left(60)
        kochflake(t, order-1, size)

t = turtle.Turtle()
t.speed(0)
t.up()
t.goto(-150, 0)
t.down()

for _ in range(3):
    kochflake(t, 3, 300)
    t.right(120)

turtle.done()
