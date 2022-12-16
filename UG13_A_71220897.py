import turtle

t = turtle.Screen()
s = turtle.Turtle()
s.hideturtle()
s.speed(speed=0)

#A
s.pensize(15)
s.color('red')
s.penup()
s.goto(-400,-70)
s.pendown()
s.left(70)
s.forward(200)
s.right(140)
s.forward(200)
s.penup()
s.backward(100)
s.pendown()
s.right(110)
s.forward(70)
s.penup()

#8
s.pensize(15)
s.color('yellow')
s.goto(-190,30)
s.pendown()
s.circle(50)
s.circle(-40)
s.penup()

#9
s.pensize(15)
s.color('lime')
s.goto(-75,25)
s.pendown()
s.circle(-40)
s.penup()
s.circle(-40,270)
s.pendown()
s.forward(90)
s.circle(-37,180)
s.penup()

#7
s.pensize(15)
s.color('cyan')
s.goto(0,100)
s.pendown()
s.right(90)
s.forward(95)
s.right(110)
s.forward(170)
s.penup()

#M
s.pensize(15)
s.color('magenta')
s.goto(140,-60)
s.pendown()
s.right(160)
s.forward(170)
s.right(130)
s.forward(90)
s.left(80)
s.forward(90)
s.right(130)
s.forward(170)


t.exitonclick()