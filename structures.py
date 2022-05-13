from tkinter import *
import math

CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 1000


class Point():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z

    def setX(self, newX):
        self.x = newX

    def setY(self, newY):
        self.y = newY

    def setZ(self, newZ):
        self.z = newZ


class Line():
    def __init__(self, start, end, id):
        self.id = id
        self.colors = ["black", "red", "yellow", "green", "blue", "orange", "brown", "grey"]
        self.start = start
        self.end = end
        self.convertedStartX = None
        self.convertedStartY = None
        self.convertedEndX = None
        self.convertedEndY = None
        self.movement = 2
        self.observatorAngle = 90
        self.rotationAngle = math.radians(2)

    def draw(self, canvas):
        if self.isInView():
            canvas.create_line(self.convertedStartX, self.convertedStartY,
                               self.convertedEndX, self.convertedEndY, fill=self.colors[self.id])

    def isInView(self):
        tan = math.tan(math.radians(self.observatorAngle/2))
        if self.start.getZ() > 0 and self.end.getZ() > 0:
            self.convertedStartX = int(
                (CANVAS_WIDTH/2 * self.start.getX()) / (self.start.getZ() * tan)) + CANVAS_WIDTH/2
            self.convertedStartY = int(-(CANVAS_HEIGHT/2 * self.start.getY()) /
                                    (self.start.getZ() * tan)) + CANVAS_HEIGHT/2
            self.convertedEndX = int(
                (CANVAS_WIDTH/2 * self.end.getX()) / (self.end.getZ() * tan)) + CANVAS_WIDTH/2
            self.convertedEndY = int(-(CANVAS_HEIGHT/2 * self.end.getY()) /
                                    (self.end.getZ() * tan)) + CANVAS_HEIGHT/2
            return True
        else:
            return False

    def moveDown(self):
        self.start.setY(self.start.getY() - self.movement)
        self.end.setY(self.end.getY() - self.movement)

    def moveUp(self):
        self.start.setY(self.start.getY() + self.movement)
        self.end.setY(self.end.getY() + self.movement)

    def moveRight(self):
        self.start.setX(self.start.getX() + self.movement)
        self.end.setX(self.end.getX() + self.movement)

    def moveLeft(self):
        self.start.setX(self.start.getX() - self.movement)
        self.end.setX(self.end.getX() - self.movement)

    def moveForwards(self):
        self.start.setZ(self.start.getZ() - self.movement)
        self.end.setZ(self.end.getZ() - self.movement)

    def moveBackwards(self):
        self.start.setZ(self.start.getZ() + self.movement)
        self.end.setZ(self.end.getZ() + self.movement)

    def rotateLeftX(self):
        self.rotate('x', self.start, self.rotationAngle)
        self.rotate('x', self.end, self.rotationAngle)

    def rotateRightX(self):
        self.rotate('x', self.start, -self.rotationAngle)
        self.rotate('x', self.end, -self.rotationAngle)

    def rotateLeftY(self):
        self.rotate('y', self.start, self.rotationAngle)
        self.rotate('y', self.end, self.rotationAngle)

    def rotateRightY(self):
        self.rotate('y', self.start, -self.rotationAngle)
        self.rotate('y', self.end, -self.rotationAngle)

    def rotateLeftZ(self):
        self.rotate('z', self.start, self.rotationAngle)
        self.rotate('z', self.end, self.rotationAngle)

    def rotateRightZ(self):
        self.rotate('z', self.start, -self.rotationAngle)
        self.rotate('z', self.end, -self.rotationAngle)
    
    def rotate(self, option, point, rotation):
        secondCoord = None
        thirdCoord = None

        if option == 'x':
            secondCoord = point.getY()
            thirdCoord = point.getZ()
            point.setY(secondCoord * math.cos(rotation) - thirdCoord * math.sin(rotation))
            point.setZ(secondCoord * math.sin(rotation) + thirdCoord * math.cos(rotation))

        elif option == 'y':
            secondCoord = point.getX()
            thirdCoord = point.getZ()
            point.setX(secondCoord * math.cos(rotation) - thirdCoord * math.sin(rotation))
            point.setZ(secondCoord * math.sin(rotation) + thirdCoord * math.cos(rotation))

        elif option == 'z':
            secondCoord = point.getX()
            thirdCoord = point.getY()
            point.setX(secondCoord * math.cos(rotation) - thirdCoord * math.sin(rotation))
            point.setY(secondCoord * math.sin(rotation) + thirdCoord * math.cos(rotation))


    def zoomIn(self):
        if self.observatorAngle > 20: 
            self.observatorAngle -= 2

    def zoomOut(self):
        if self.observatorAngle < 160:
            self.observatorAngle += 2

class Drawer():
    def __init__(self, lines, canvas):
        self.canvas = canvas
        self.lines = lines
        self.draw()

    def draw(self):
        self.canvas.delete("all")
        for line in self.lines:
            line.draw(self.canvas)

    def moveDown(self):
        for line in self.lines:
            line.moveDown()

    def moveUp(self):
        for line in self.lines:
            line.moveUp()

    def moveLeft(self):
        for line in self.lines:
            line.moveLeft()

    def moveRight(self):
        for line in self.lines:
            line.moveRight()

    def moveForwards(self):
        for line in self.lines:
            line.moveForwards()

    def moveBackwards(self):
        for line in self.lines:
            line.moveBackwards()

    def rotateLeftX(self):
        for line in self.lines:
            line.rotateLeftX()
    
    def rotateRightX(self):
        for line in self.lines:
            line.rotateRightX()
    
    def rotateLeftY(self):
        for line in self.lines:
            line.rotateLeftY()
    
    def rotateRightY(self):
        for line in self.lines:
            line.rotateRightY()
    
    def rotateLeftZ(self):
        for line in self.lines:
            line.rotateLeftZ()
    
    def rotateRightZ(self):
        for line in self.lines:
            line.rotateRightZ()
    
    def zoomIn(self):
        for line in self.lines:
            line.zoomIn()
    
    def zoomOut(self):
        for line in self.lines:
            line.zoomOut()