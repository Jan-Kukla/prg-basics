import turtle

def draw_square(length):
    window = turtle.Screen()
    #window.bgcolor("lightgreen")

    pen = turtle.Turtle()
    #pen.speed(5)

    side_length = length

    for i in range(4):
        pen.forward(side_length)
        pen.right(90)

def draw_trangle(length):
    window = turtle.Screen()
    #window.bgcolor("lightgreen")
    
    pen = turtle.Turtle()
    #pen.speed(5)
    
    side_length = length

    for i in range(3):
        pen.forward(side_length)
        pen.right(120)

    #pen.hideturtle()
    #window.mainloop()

def draw_rectangle(length_a, length_b):
    #window = turtle.Screen()
    #window.bgcolor("lightgreen")
    
    #pen = turtle.Turtle()
    #pen.speed(5)
    
    side_length_a = length_a
    side_length_b = length_b

    for i in range(2):
        pen.forward(side_length_a)
        pen.right(90)
        pen.forward(side_length_b)
        pen.right(90)

    #pen.hideturtle()
    #window.mainloop()