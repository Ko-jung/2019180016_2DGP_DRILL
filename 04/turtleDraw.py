import turtle

turtle.shape("turtle")
turtle.speed(10)

i = 0
turtle.penup()
turtle.goto(-300,300)
turtle.pendown()
while i < 2:
    turtle.fd(500);  turtle.right(90)
    turtle.fd(100);  turtle.right(90)
    turtle.fd(500);  turtle.left(90)
    turtle.fd(100);  turtle.left(90)
    i+=1

turtle.fd(500);  turtle.right(90)
turtle.fd(100);  turtle.right(90)

i = 0
turtle.fd(500);  turtle.right(90)

while i < 2:
    turtle.fd(500); turtle.right(90)
    turtle.fd(100);  turtle.right(90)
    turtle.fd(500);  turtle.left(90)
    turtle.fd(100);  turtle.left(90)
    i+=1

turtle.fd(500); turtle.right(90)
turtle.fd(100);  turtle.right(90)
turtle.fd(500)

turtle.exitonclick()
