from tkinter import *
import RPi.GPIO as GPIO
from time import sleep

def button(event):
    print("dat aint falco! Charlie Gray - 2021")

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

master = Tk()
master.bind("<<PhysicalButtonDown>>", button)

def loop():
    if GPIO.input(21) == GPIO.HIGH:
        master.event_generate("<<PhysicalButtonDown>>")
    master.after(10,loop)

master.after(10,loop)
master.mainloop()

#while True:
#    if GPIO.input()
