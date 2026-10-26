import figures
import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

pen = turtle.Turtle()
pen.speed(5)

#figures.draw_trangle(100)
figures.draw_rectangle(100,200)
pen.penup()
pen.goto(100, 100)
figures.draw_rectangle(200,100)
#figures.draw_trangle(100)
#figures.draw_trangle(100)
#figures.draw_square(100)
#figures.draw_square(100)
#pen.penup()
pen.hideturtle()
window.mainloop()

