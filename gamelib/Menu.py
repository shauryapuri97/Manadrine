frame_width = 640
frame_height = 520

class Menu:
    
    def __init__(self):
        
        self.spritesheet = simplegui.load_image('http://i.imgur.com/esDivR3.png')
        self.counter = 0
        self.time = 0
        self.pos = Vector((frame_width/2, frame_height/3))


    def draw_handler(self, canvas):
        
        imgCentre = (((2*self.counter + 1)%8)*272/8, (1)*288/8)
        canvas.draw_image(self.spritesheet, imgCentre, (272/4, 288/4), self.pos.getP(), (125, 125))
        self.time += 1
        if self.time % 5 == 0:
            self.counter += 1

menu = Menu()
frame = simplegui.create_frame('Bish Bosh', frame_width, frame_height)
frame.set_draw_handler(menu.draw_handler)
frame.start()
