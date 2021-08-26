class Frog:
    def __init__(self, size, canvas):
        self.screen = size*8
        self.size = size/2
        self.speed = 5
        x = size * 4 - (self.size/2)
        y = size * 7.5 - (self.size/2)
        self.obj = canvas.create_rectangle(x, y, x+self.size, y+self.size, fill = "#38d161")
        
    def up(self, canvas):
        y = canvas.coords(self.obj)[1]
        if y - self.speed < 0:
            canvas.move(self.obj, 0 , -1 * y)
        else:
            canvas.move(self.obj, 0, -1*self.speed)
        
    def down(self, canvas):
        y = canvas.coords(self.obj)[3]
        if y + self.speed > self.screen:
            canvas.move(self.obj, 0 , self.screen-y)
        else:
            canvas.move(self.obj, 0, self.speed)
        
    def left(self, canvas):
        x = canvas.coords(self.obj)[0]
        if x - self.speed < 0:
            canvas.move(self.obj, -1*x, 0)
        else:
            canvas.move(self.obj, -1*self.speed, 0)
        
    def right(self, canvas):
        x = canvas.coords(self.obj)[2]
        if x + self.speed > self.screen:
            canvas.move(self.obj, self.screen-x, 0)
        else:
            canvas.move(self.obj, self.speed, 0)
