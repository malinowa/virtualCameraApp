from tkinter import *
from structures import *
from freader import FileReader

CANVAS_WIDTH=1000
CANVAS_HEIGHT=1000

root = Tk()
canvas = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

freader = FileReader('figures2.txt')
lines = freader.getLines()

drawer = Drawer(lines=lines, canvas=canvas)

def moveDown(event):
    drawer.moveDown()
    drawer.draw()

def moveUp(event):
    drawer.moveUp()
    drawer.draw()

def moveLeft(event):
    drawer.moveLeft()
    drawer.draw()

def moveRight(event):
    drawer.moveRight()
    drawer.draw()

def moveForwards(event):
    drawer.moveForwards()
    drawer.draw()

def moveBackwards(event):
    drawer.moveBackwards()
    drawer.draw()

def rotateLeftX(event):
    drawer.rotateLeftX()
    drawer.draw()

def rotateRightX(event):
    drawer.rotateRightX()
    drawer.draw()

def rotateLeftY(event):
    drawer.rotateLeftY()
    drawer.draw()

def rotateRightY(event):
    drawer.rotateRightY()
    drawer.draw()

def rotateLeftZ(event):
    drawer.rotateLeftZ()
    drawer.draw()

def rotateRightZ(event):
    drawer.rotateRightZ()
    drawer.draw()

def zoomIn(event):
    drawer.zoomIn()
    drawer.draw()

def zoomOut(event):
    drawer.zoomOut()
    drawer.draw()

root.bind('<Down>', moveDown)
root.bind('<Up>', moveUp)
root.bind('<Left>', moveLeft)
root.bind('<Right>', moveRight)
root.bind('<s>', moveForwards)
root.bind('<w>', moveBackwards)

root.bind('<a>', rotateLeftY)
root.bind('<d>', rotateRightY)
root.bind('<r>', rotateLeftX)
root.bind('<f>', rotateRightX)
root.bind('<z>', rotateLeftZ)
root.bind('<c>', rotateRightZ)

root.bind('<t>', zoomIn)
root.bind('<g>', zoomOut)


root.mainloop()
