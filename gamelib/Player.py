class Player:
    
    def __init__(self):
        self.spritesheet = simplegui.load_image('http://i.imgur.com/esDivR3.png')
        self.counter = 0
        self.time = 0
        self.x = 100
        self.y = 100

        
    def draw(self, canvas):
        
        imgCentre = (((2*self.counter + 1)%8)*272/8, (5)*288/8)
        canvas.draw_image(self.spritesheet, imgCentre, (272/4, 288/4), (self.x, self.y), (125, 125))
        self.time += 1
        if self.time % 5 == 0:
            self.counter += 1
