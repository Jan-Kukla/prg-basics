import figures

#window = turtle.Screen()
#window.bgcolor("lightgreen")
#pen = turtle.Turtle()
#pen.speed(5)

ksztalt = figures.draw_rectangle(20, 40)

figures.pen.penup()
figures.pen.goto(40,0)
figures.pen.pendown()

ksztalt2 = figures.draw_rectangle(20, 40)

figures.pen.penup()
figures.pen.goto(80,0)
figures.pen.pendown()

ksztalt3 = figures.draw_square(20)

figures.pen.penup()
figures.pen.goto(120,0)
figures.pen.pendown()

ksztalt3 = figures.draw_square(20)

figures.pen.penup()
figures.pen.goto(160,0)
figures.pen.pendown()

ksztalt4 = figures.draw_trangle(20)

figures.pen.penup()
figures.pen.goto(200,0)
figures.pen.pendown()

ksztalt4 = figures.draw_trangle(20)

figures.pen.hideturtle()
figures.window.mainloop()

