from tkinter import *
from Tile import Tile
from Frog import Frog
from Car import Car
import RPi.GPIO as GPIO
from PIL import ImageTk, Image
from random import randint


def run():
    loop()
    spawnCars()
    canvas.mainloop()
    
def reset():
    x = TILESIZE * 4 - (frog.size/2)
    y = TILESIZE * 8 - (TILESIZE/2) - (frog.size/2)
    cx = canvas.coords(frog.obj)[0]
    cy = canvas.coords(frog.obj)[1]
    canvas.move(frog.obj, x - cx, y - cy)
    
def up(event):
    frog.up(canvas)

def down(event):
    frog.down(canvas)

def left(event):
    frog.left(canvas)
    
def right(event):
    frog.right(canvas)

def loop():
    if GPIO.input(21) == GPIO.HIGH:
        master.event_generate("<<Up>>")
    if GPIO.input(20) == GPIO.HIGH:
        master.event_generate("<<Left>>")
    if GPIO.input(26) == GPIO.HIGH:
        master.event_generate("<<Right>>")
    if GPIO.input(16) == GPIO.HIGH:
        master.event_generate("<<Down>>")
    for i in range(len(leftCars)):
        leftCars[i].update(canvas)
    for i in range(len(rightCars)):
        rightCars[i].update(canvas)
    canvas.after(33, loop)

def spawnCars():
    num = randint(1,100)
    if(num <= 35):
        rightCars.append(Car(canvas, True, TILESIZE))
    elif(num >= 65):
        leftCars.append(Car(canvas, False, TILESIZE))
    k = 0
    while k < len(rightCars):
        if rightCars[k].x > TILESIZE * 8:
            rightCars.remove(rightCars[k])
        else:
            if rightCars[k].collision(canvas,frog):
                reset()
            k += 1
    l = 0
    while l < len(leftCars):
        if leftCars[l].x < 0:
            leftCars.remove(leftCars[l])
        else:
            if leftCars[l].collision(canvas,frog):
                reset()
            l += 1
    
    canvas.after(500, spawnCars)
    
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(20,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(26,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

WIDTH = 960
HEIGHT = WIDTH
TILESIZE = WIDTH / 8

master = Tk()

master.bind("<<Up>>", up)
master.bind("<<Left>>", left)
master.bind("<<Right>>", right)
master.bind("<<Down>>", down)

canvas = Canvas(master, width=WIDTH, height=HEIGHT)
canvas.pack()

tiles = []
for i in range(8):
    tiles.append([])
    for j in range(8):
        tiles[i].append(Tile(i*TILESIZE, j*TILESIZE, TILESIZE, "#34a352", canvas))

for i in range(8):
    canvas.itemconfig(tiles[i][1].tile, fill="#4a4d4b", outline="#4a4d4b")
    canvas.itemconfig(tiles[i][3].tile, fill="#4a4d4b", outline="#4a4d4b")
    canvas.itemconfig(tiles[i][5].tile, fill="#4a4d4b", outline="#4a4d4b")

rightCars = []
leftCars = []

leftCars.append(Car(canvas, False, TILESIZE))
rightCars.append(Car(canvas, True, TILESIZE))
    
frog = Frog(TILESIZE, canvas)


run()