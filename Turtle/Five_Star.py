import turtle

t = turtle.Turtle()
t.color("gold")
t.pensize(3)
t.speed(5)

for i in range(5):
    t.forward(100)
    t.left(120)

turtle.done()