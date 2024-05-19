class Tank:
    def __init__(self, x, y, speed, maxbullets, bullettype):
        self.width = 70
        self.height = 70
        self.x = x
        self.y = y
        self.speed = speed
        self.maxbullets = maxbullets
        self.bullettype = bullettype

    ### Setters ###
    def set_left(self, a):
        self.x = a
    def set_right(self, a):
        self.x = a - 70
    def set_top(self, a):
        self.y = a
    def set_bottom(self, a):
        self.y = a - self.height
    
    ### Getters ###
    def left(self):
        return self.x
    def right(self):
        return self.x + self.width
    def top(self):
        return self.y
    def bottom(self):
        return self.y + self.height

        
    def move(self, x, y):
        self.x += x
        self.y -= y