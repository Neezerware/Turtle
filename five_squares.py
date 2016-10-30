#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     07/10/2016
# Copyright:   (c) User 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import turtle
__import__("turtle").__traceable__=False

def create_canvas(cl, ttle):
    w=turtle.Screen()
    w.bgcolor(cl)
    w.title(ttle)
    return w

def create_tur(ccl, sz):
    t=turtle.Turtle()
    t.pensize(sz)
    t.color(ccl)
    return t

def create_square(sz):
    win=create_canvas("light green", "Draw squares")
    ft=create_tur("pink", 5)
    for k in range(5):
        ft.penup()
        ft.forward(sz*2)
        ft.pendown()
        for i in range(4):
            ft.forward(sz)
            ft.left(90)
    ft.penup()
    ft.forward(sz*2)
    ft.stamp()
    win.mainloop()


create_square(20)

