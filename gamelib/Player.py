class Player:
    
    def __init__(self):
        self.spritesheet = simplegui.load_image('http://i.imgur.com/esDivR3.png')
        self.counter = 0
        self.time = 0
        self.pos = Vector((100, 100))

        
    def draw(self, canvas):
        
        imgCentre = (((2*self.counter + 1)%8)*272/8, (5)*288/8)
        canvas.draw_image(self.spritesheet, imgCentre, (272/4, 288/4), self.pos.getP(), (125, 125))
        self.time += 1
        if self.time % 5 == 0:
            self.counter += 1
        
    def keydown(self, key):
        
        v = Vector((0, 20))
        u = Vector((20, 0))
        
        if key == simplegui.KEY_MAP['down']:
            self.pos.add(v)
        
        if key == simplegui.KEY_MAP['up']:
            self.pos.sub(v)
        
        if key == simplegui.KEY_MAP['left']:
            self.pos.sub(u)
        
        if key == simplegui.KEY_MAP['right']:
            self.pos.add(u)
            background.bgSpeed = 4
            
    def keyup(self, key):
        
        if key == simplegui.KEY_MAP['right']:
            background.bgSpeed = 2
