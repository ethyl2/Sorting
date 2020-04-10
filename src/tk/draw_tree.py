import turtle
import random

"""
Modify the thickness of the branches so that as the branchLen gets smaller, 
the line gets thinner.

Modify the color of the branches so that as the branchLen gets very short it is colored like a leaf.

Modify the angle used in turning the turtle so that at each branch point the angle is 
selected at random in some range. 
For example choose the angle between 15 and 45 degrees. Play around to see what looks good.

Modify the branchLen recursively so that instead of always subtracting 
the same amount you subtract a random amount in some range.

"""
tree_colors = ['#3F602B', '#397D02',
               '#698B22', '#4CBB17', '#83F52C', '#C8F526', '#D4ED91', '#DFFFA5']


def tree(branchLen, t, size, color_index):
    t.pensize(size)
    t.pencolor(tree_colors[color_index])
    if branchLen > 5:
        my_angle = random.randrange(15, 46)
        # print(my_angle)
        my_sub = random.randrange(14, 16)
        t.forward(branchLen)
        t.right(my_angle)
        tree(branchLen-my_sub, t, size-1.25, color_index+1)
        t.left(my_angle * 2)
        tree(branchLen-my_sub, t, size-1.25, color_index+1)
        t.right(my_angle)
        color_index -= 1
        t.backward(branchLen)


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(100, t, 10, 0)
    myWin.exitonclick()


main()
