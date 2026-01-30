import turtle

drawing_board=turtle.Screen()
drawing_board.bgcolor("yellow")
drawing_board.title("Python Turtle")
turtle_instance=turtle.Turtle()
turtle_instance.color("black")
turtle.speed(0)

def turtle_forward():
    turtle_instance.forward(50)

def rotate_angle_right():
    turtle_instance.right(50)

def rotate_angle_left():
    turtle_instance.left(50)

def clear_screen():
    turtle_instance.clear()

def return_home():
    turtle_instance.home()

def turtle_pen_up():
    turtle_instance.penup()

def turtle_pen_down():
    turtle_instance.pendown()

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward,key="space")
drawing_board.onkey(fun=rotate_angle_left,key="Up")
drawing_board.onkey(fun=rotate_angle_right,key="Down")
drawing_board.onkey(fun=clear_screen,key="c")
drawing_board.onkey(fun=return_home,key="a")
drawing_board.onkey(fun=turtle_pen_down,key="w")
drawing_board.onkey(fun=turtle_pen_up,key="q")
turtle.mainloop()
