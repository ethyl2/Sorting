import turtle

myTurtle = turtle.Turtle()
myTurtle.pencolor('yellowgreen')
myTurtle.shape('turtle')
myTurtle.pensize(5)
myWin = turtle.Screen()


def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle, lineLen-5)


drawSpiral(myTurtle, 150)
myWin.exitonclick()
