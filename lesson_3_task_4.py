import trace
from turtle import *

my_turtle = Turtle()
my_turtle.speed(0)
my_turtle.screen.setup(1200, 800)

def draw_rect1(t):
    t.right(23)
    t.forward(10)
    t.right(23)
    t.forward(10)
    t.right(23)
    t.forward(10)
    t.left(23)
    t.forward(10)
    t.right(23)
    t.forward(10)
    t.right(23)
    t.forward(10)
    t.backward(10)
    t.left(23)
    t.backward(10)
    t.left(23)
    t.backward(10)
    t.left(171)
    t.circle(30)
    t.left(90)
    t.up()
    t.forward(20)
    t.circle(2)
    t.left(40)
    t.up()
    t.forward(20)
    t.down()
    t.circle(2)
    t.right(80)
    t.up()
    t.forward(20)
    t.down()
    t.circle(2)
    t.right(70)
    t.up()
    t.forward(20)
    t.down()
    t.circle(2)
    t.right(70)
    t.up()
    t.forward(20)
    t.down()
    t.circle(2)
    t.right(40)
    t.up()
    t.forward(20)
    t.down()
    t.circle(2)
    t.right(60)
    t.up()
    t.forward(20)
    t.down()
    t.circle(2)
    t.right(130)
    t.up()
    t.forward(30)
    t.down()
    t.circle(2)
    t.left(105)
    t.up()
    t.forward(35)
    t.down()
    t.circle(2)
    t.left(110)
    t.up()
    t.forward(30)
    t.down()
    t.circle(2)
    t.ht()
draw_rect1(my_turtle)


# рисует квадраты в цикле
#for x in range(0, 360):
    #draw_rect(my_turtle)
    #my_turtle.right(1)

# необходимо, чтобы окно не закрывалось само, а только по клику
my_turtle.screen.exitonclick()
my_turtle.screen.mainloop()