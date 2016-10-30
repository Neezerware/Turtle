#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     09/10/2016
# Copyright:   (c) User 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import turtle
win=turtle.Screen()
win.bgcolor("light green")
win.title("Bar Chart")
win.screensize(1000,1000)
def draw_bar(t,height):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(' '+ str(height))
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(height)
    t.end_fill()
    t.left(90)
    t.penup()
    t.forward(30)
    t.pendown()


alex=turtle.Turtle()
alex.color("blue", "red")
xs = [48, 117, 200, 240, 160, 260, 220]

for x in xs:
    if x>=200:
        alex.color("blue","red")
    elif x>=100 and x<200:
        alex.color("blue","yellow")
    elif x<100:
        alex.color("blue", "green")
    draw_bar(alex,x)
win.mainloop()