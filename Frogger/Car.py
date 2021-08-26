from tkinter import *
from PIL import ImageTk, Image
from random import choice
class Car:
    def __init__(self, canvas, topRoad, tileSize):
        self.speed = 20
        self.h= int(tileSize * .3)
        self.w = int(tileSize * .4)
        self.x = 0
        self.y = 0
        self.topRoad = topRoad
        if self.topRoad:
            self.x = -tileSize
            self.y = tileSize * 3.5 - (self.h/2)
        else:
            self.x = tileSize * 9
            list = [tileSize * 5.5 - (self.h/2), tileSize * 1.5 - (self.h/2)]
            self.y = choice(list)
        self.obj = canvas.create_rectangle(self.x, self.y, self.x + self.w, self.y + self.h, fill = "#2c6bd1")
        

    def update(self, canvas):
        if self.topRoad:
            canvas.move(self.obj, self.speed, 0)
            self.x += self.speed
        else:
            canvas.move(self.obj, -self.speed, 0)
            self.x -= self.speed
            
    def collision(self, canvas, frog):
        l1 = [self.x, self.y]
        r1 = [self.x + self.w, self.y + self.h]
        l2 = [canvas.coords(frog.obj)[0], canvas.coords(frog.obj)[1]]
        r2 = [canvas.coords(frog.obj)[2], canvas.coords(frog.obj)[3]]
        
        
        if (l1[0] == r1[0] or l1[1] == r1[1] or l2[0] == r2[0] or l2[1] == r2[1]):
            return False
        if (l1[0] >= r2[0] or l2[0] >= r1[0]):
            return False
        if(r1[1] <= l2[1] or r2[1] <= l1[1]):
            return False
        return True
        
        
    