import simplegui
import math

class Vector:

    def __init__(self, p=(0, 0)):
        self.x = p[0]
        self.y = p[1]

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def getP(self):
        return (self.x, self.y)

    def copy(self):
        x = self.x
        y = self.y
        return (x, y)

    def mult(self, k):
        self.x = self.x * k
        self.y = self.y * k

    def div(self, k):
        self.x = self.x / k
        self.y = self.y / k

    def normalise(self):
        return self.div(self.length())

    def get_normalised(self):
        v = Vector(self.copy())
        v.div(v.length())
        return v

    def add(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y

    def sub(self, other):
        self.x = self.x - other.x
        self.y = self.y - other.y

    def negate(self):
        self.x = -self.x
        self.y = -self.y

    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y)

    def length(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    def length_squared(self):
        return math.pow(self.x, 2) + math.pow(self.y, 2)

    def reflect(self, normal):
        n = normal.copy()
        n.mult(2 * self.dot(normal))
        self.sub(n)
        return self

    def angle(self, other):
        dot = self.dot(other)
        length_product = self.length() * other.length()
        return math.degrees(math.acos(dot / length_product))

frame_width = 640
frame_height = 520

class Game:
    
    isEasy = True
    isMedium = False
    isHard = False
    
    def __init__(self):
        self.message = 'This is the game area'
    def draw_handler(self, canvas):
        
        global isEasy, isMedium, isHard
        
        print (self.message)
        if Game.isMedium==True:
            print('OK OK')
            
class Menu:
    
    def __init__(self):
        
        self.spritesheet = simplegui.load_image('http://i.imgur.com/esDivR3.png')
        self.play_button = simplegui.load_image('http://i.imgur.com/YoufMUE.png')
        self.playpressed_button = simplegui.load_image('http://i.imgur.com/XOMPi6Z.png')
        self.instructions_button = simplegui.load_image('http://i.imgur.com/Okm3Pl8.png')
        self.instructionspressed_button = simplegui.load_image('http://i.imgur.com/D9TKm5I.png')
        self.difficulty_button = simplegui.load_image('http://i.imgur.com/FTKT9RY.png')
        self.difficultypressed_button = simplegui.load_image('http://i.imgur.com/yTPYdkm.png')
        self.exit_button = simplegui.load_image('http://i.imgur.com/iBNcHVz.png')
        self.exitpressed_button = simplegui.load_image('http://i.imgur.com/sruD3sH.png')
        self.back_button = simplegui.load_image('http://i.imgur.com/KeiRzKu.png')
        self.backpressed_button = simplegui.load_image('http://i.imgur.com/oerVbsu.png')
        self.counter = 0
        self.time = 0
        self.pos = Vector((frame_width/2, frame_height/3))
        self.index = 0


    def draw_handler(self, canvas):
        
        imgCentre = (((2*self.counter + 1)%8)*272/8, (1)*288/8)
        canvas.draw_image(self.spritesheet, imgCentre, (272/4, 288/4), self.pos.getP(), (125, 125))
        canvas.draw_image(self.play_button, (200/2,50/2), (200, 50), (frame_width/2, frame_height/1.8), (200, 50))
        canvas.draw_image(self.instructions_button, (200/2,50/2), (200, 50), (frame_width/2, frame_height/1.5), (200, 50))
        canvas.draw_image(self.difficulty_button, (200/2,50/2), (200, 50), (frame_width/2, frame_height/1.28), (200, 50))
        canvas.draw_image(self.exit_button, (200/2,50/2), (200, 50), (frame_width/2, frame_height/1.12), (200, 50))
        self.time += 1
        if self.time % 5 == 0:
            self.counter += 1
        if self.index==0:
            canvas.draw_image(self.playpressed_button, (200/2,50/2), (200, 50), (frame_width/2, frame_height/1.8), (200, 50))
        elif self.index==1:
            canvas.draw_image(self.instructionspressed_button, (200/2,50/2), (200, 50), (frame_width/2, frame_height/1.5), (200, 50))
        elif self.index==2:
            canvas.draw_image(self.difficultypressed_button, (200/2,50/2), (200, 50), (frame_width/2, frame_height/1.28), (200, 50))
        elif self.index ==3:
            canvas.draw_image(self.exitpressed_button, (200/2,50/2), (200, 50), (frame_width/2, frame_height/1.12), (200, 50))
            
        #Add mouse drag and change of canvas when an option is selected
    
    def keydown(self, key):
        
        if key == simplegui.KEY_MAP['down']:
            
            if self.index==3:
                self.index=0
            else:
                self.index+=1
        
        if key == simplegui.KEY_MAP['up']:
            
            if self.index==0:
                self.index+=3
            else: 
                self.index-=1
        
        if key == 13:
            
            if self.index==0:
                frame.set_draw_handler(game.draw_handler)
            elif self.index ==1:
                frame.set_draw_handler(screen.draw_handler)
                frame.set_keydown_handler(screen.keydown)
            elif self.index ==2:
                frame.set_draw_handler(screen_diff.draw_handler)
                frame.set_keydown_handler(screen_diff.keydown)
            elif self.index==3:
                exit(0)
            
class Screen:
    
    def __init__(self):
        
        self.spritesheet = simplegui.load_image('http://i.imgur.com/esDivR3.png')
        self.back_button = simplegui.load_image('http://i.imgur.com/KeiRzKu.png')
        self.backpressed_button = simplegui.load_image('http://i.imgur.com/oerVbsu.png')
        self.counter = 0
        self.time = 0
        self.pos = Vector((frame_width/2, frame_height/3))


    def draw_handler(self, canvas):
        
        imgCentre = (((2*self.counter + 1)%8)*272/8, (1)*288/8)
        canvas.draw_image(self.spritesheet, imgCentre, (272/4, 288/4), self.pos.getP(), (125, 125))
        canvas.draw_image(self.backpressed_button, (200/2,50/2), (200, 50), (frame_width/2, frame_height/1.08), (200/1.2, 50/1.2))
        self.time += 1
        if self.time % 5 == 0:
            self.counter += 1
    
    def keydown(self, key):
        
        if key == 13:
            
            frame.set_draw_handler(menu.draw_handler)
            frame.set_keydown_handler(menu.keydown)
                
        #Add mouse drag and change of canvas when an option is selected

class Screen_Diff:
    
    def __init__(self):
        
        self.spritesheet = simplegui.load_image('http://i.imgur.com/esDivR3.png')
        self.play_button = simplegui.load_image('http://i.imgur.com/YoufMUE.png')
        self.playpressed_button = simplegui.load_image('http://i.imgur.com/XOMPi6Z.png')
        self.instructions_button = simplegui.load_image('http://i.imgur.com/Okm3Pl8.png')
        self.instructionspressed_button = simplegui.load_image('http://i.imgur.com/D9TKm5I.png')
        self.difficulty_button = simplegui.load_image('http://i.imgur.com/FTKT9RY.png')
        self.difficultypressed_button = simplegui.load_image('http://i.imgur.com/yTPYdkm.png')
        self.back_button = simplegui.load_image('http://i.imgur.com/KeiRzKu.png')
        self.backpressed_button = simplegui.load_image('http://i.imgur.com/oerVbsu.png')
        self.counter = 0
        self.time = 0
        self.pos = Vector((frame_width/2, frame_height/3))
        self.index = 0


    def draw_handler(self, canvas):
        
        imgCentre = (((2*self.counter + 1)%8)*272/8, (1)*288/8)
        canvas.draw_image(self.spritesheet, imgCentre, (272/4, 288/4), self.pos.getP(), (125, 125))
        canvas.draw_image(self.play_button, (200/2,50/2), (200, 50), (frame_width/2, frame_height/1.8), (200, 50))
        canvas.draw_image(self.instructions_button, (200/2,50/2), (200, 50), (frame_width/2, frame_height/1.5), (200, 50))
        canvas.draw_image(self.difficulty_button, (200/2,50/2), (200, 50), (frame_width/2, frame_height/1.28), (200, 50))
        canvas.draw_image(self.back_button, (200/2,50/2), (200, 50), (frame_width/2, frame_height/1.08), (200/1.2, 50/1.2))
        
        self.time += 1
        if self.time % 5 == 0:
            self.counter += 1
            if Game.isEasy == True:
                print ('The game is set to Easy')
            elif Game.isMedium == True:
                print ('The game is set to Medium')
            elif Game.isHard == True:
                print('The game is set to Hard')	
        if self.index==0:
            canvas.draw_image(self.playpressed_button, (200/2,50/2), (200, 50), (frame_width/2, frame_height/1.8), (200, 50))
        elif self.index==1:
            canvas.draw_image(self.instructionspressed_button, (200/2,50/2), (200, 50), (frame_width/2, frame_height/1.5), (200, 50))
        elif self.index==2:
            canvas.draw_image(self.difficultypressed_button, (200/2,50/2), (200, 50), (frame_width/2, frame_height/1.28), (200, 50))
        elif self.index==3:
            canvas.draw_image(self.backpressed_button, (200/2,50/2), (200, 50), (frame_width/2, frame_height/1.08), (200/1.2, 50/1.2))
        
        
    
    def keydown(self, key):
        
        if key == simplegui.KEY_MAP['down']:
            
            if self.index==3:
                self.index=0
            else:
                self.index+=1
        
        if key == simplegui.KEY_MAP['up']:
            
            if self.index==0:
                self.index+=3
            else: 
                self.index-=1
                
        if key == 13:
            
            if self.index==0:
                Game.isEasy = True
                Game.isMedium = False
                Game.isHard = False
                
            elif self.index==1:
                Game.isEasy = False
                Game.isMedium = True
                Game.isHard = False
                
            elif self.index==2:
                Game.isEasy = False
                Game.isMedium = False
                Game.isHard = True
                
            elif self.index==3:
                frame.set_draw_handler(menu.draw_handler)
                frame.set_keydown_handler(menu.keydown)
                
        #Add mouse drag and change of canvas when an option is selected
        

menu = Menu()
screen = Screen()
screen_diff = Screen_Diff()
game = Game()
frame = simplegui.create_frame('Bish Bosh', frame_width, frame_height)
frame.set_draw_handler(menu.draw_handler)
frame.set_keydown_handler(menu.keydown)
frame.start()
