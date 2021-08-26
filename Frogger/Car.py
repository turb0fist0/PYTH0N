from tkinter import *
from PIL import ImageTk, Image
class Car:
    def __init__(self, canvas, topRoad, tileSize):
        self.speed = 5
        h= int(tileSize * .3)
        w = int(tileSize * .4)
        self.x = 0
        y = 0
        if topRoad:
            x = -tileSize
            y = tileSize * 3.5 - (h/2)
        self.obj = canvas.create_rectangle(self.x, y, self.x + w, y + h, fill = "#2c6bd1")
    def update(self, canvas):
        canvas.move(self.obj, self.speed, 0)
        self.x += self.speed
        
        
    