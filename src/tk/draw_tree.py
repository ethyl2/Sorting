import turtle
"""
Modify the thickness of the branches so that as the branchLen gets smaller, 
the line gets thinner.
"""


def tree(branchLen, t, size):
    t.pensize(size)
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15, t, size-1.25)
        t.left(40)
        tree(branchLen-15, t, size-1.25)
        t.right(20)
        t.backward(branchLen)


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(100, t, 10)
    myWin.exitonclick()


main()
