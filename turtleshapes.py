import turtle

t = turtle.Turtle()
t.color('#00D9F7')  # Cyan
t.width(3)

# Draw Hexagon
for i in range(6):
    t.forward(100)
    t.left(60)

t = turtle.Turtle()
t.color('#FF0055')  # Neon Red
t.bgcolor('#1a1a1a')

# Draw Rectangle
t.begin_fill()
for i in range(2):
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.left(90)
t.end_fill()

t = turtle.Turtle()
t.color('#00ff41')  # Neon Green
t.width(2)

# Draw Triangle
t.begin_fill()
for i in range(3):
    t.forward(150)
    t.left(120)
t.end_fill()