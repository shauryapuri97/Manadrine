import simplegui

class Background:
    
    def __init__(self):
        self.background_image = simplegui.load_image('http://i.imgur.com/PxXnhsW.png')
        self.y = 240
        self.x = 640
   
    def draw(self, canvas):
        canvas.draw_image(self.background_image, (640, 240), (1280, 480), (self.x, self.y), (1280, 480))
        
        if self.x <= 0:
            canvas.draw_image(self.background_image, (640, 240), (1280, 480), (self.x + 1280, self.y), (1280, 480))
        if self.x <= -640:
            self.x = 640
            
        self.x -= 2
         
background = Background()
frame = simplegui.create_frame("Test", 640, 480)
frame.set_draw_handler(background.draw)
frame.start()
