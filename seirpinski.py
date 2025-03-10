import turtle

def draw_triangle(points, color, t):
    t.fillcolor(color)
    t.up()
    t.goto(points[0])
    t.down()
    t.begin_fill()
    t.goto(points[1])
    t.goto(points[2])
    t.goto(points[0])
    t.end_fill()

def midpoint(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points, depth, t):
    colors = ['red', 'blue', 'orange', 'green', 'white', 'black']
    draw_triangle(points, colors[depth], t)
    if depth > 0:
        m0 = midpoint(points[0], points[1])
        m1 = midpoint(points[1], points[2])
        m2 = midpoint(points[2], points[0])
        sierpinski([points[0], m0, m2], depth-1, t)
        sierpinski([points[1], m0, m1], depth-1, t)
        sierpinski([points[2], m1, m2], depth-1, t)
      
t = turtle.Turtle()
t.speed(0)
points = [(-200, -100), (0, 200), (200, -100)]
sierpinski(points, 1, t)  # Depth set to 1
turtle.done()
