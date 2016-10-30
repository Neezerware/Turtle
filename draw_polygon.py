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

def create_tur(clr, sz):
    t=turtle.Turtle()
    t.color(clr)
    t.pensize(5)
    return t

def draw_polygon(sz):
    win=create_canvas("light green","Draw Polygon" )
    tess=create_tur("pink", 5)
    for i in range(8):
        tess.forward(sz)
        tess.left(45)

draw_polygon(80)