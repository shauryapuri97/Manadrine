import pygame, os
import menu
import data

def main():
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    pygame.mouse.set_visible(0)
    #pygame.display.set_icon(pygame.image.load(data.filepath(""))) #Add the game icon
    pygame.display.set_caption("Founder's Fire v2.0 - The Game")
    screen = pygame.display.set_mode((640, 480))
    menu.Menu(screen)
