class Tile:
    
    def __init__(self, x, y, size, color, canvas):
        self.x = x
        self.y = y
        self.tile = canvas.create_rectangle(x, y, x+size, y+size, fill=color, outline="#fff", width = 1)