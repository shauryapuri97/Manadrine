import pygame, sys
from pygame.locals import *
from data import *


def cutscene(screen, text):
    black= pygame.Surface((640, 480))  # Create a scene/surface/BG for cut scene
    black.fill((0, 0, 0))  # Fill the scene with black BG
    font = pygame.font.Font(filepath("fonts/font.ttf"), 16)  # Add font to the scene
    alpha = 255
    intro = True
    outro = False
    fontHeight = font.get_height() + 3  # Constant fontHeight to determine the height of the image
    textLen = len(text)  # Constant textLen used to determine the height of the image
    height = textLen * fontHeight  # Calculated height for the image
    image = pygame.Surface((640, height))  # image surface object created
    y = 0
    for line in text:
        ren = font.render(line, 1, (255, 255, 255))
        image.blit(ren,
                   (320 - ren.get_width() / 2, y * fontHeight)) # font is rendered over the surface object at (x,y)
        y += 1
    while 1:
        pygame.time.wait(10)
        for e in pygame.event.get():  # To check for key press / action events in the scene
            if e.type == QUIT:
                sys.exit()
            if e.type == K_c:
                sys.exit()
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    return
                if e.key in (K_SPACE, K_RETURN):  #If enter is pressed then
                    intro = False  #Switch the scene to outro i.e. fade out
                    outro = True
        if intro:
            if alpha > 0:
                alpha -= 5
        if outro:
            if alpha < 255:
                alpha += 5
            else:
                return
        black.set_alpha(alpha)  # Alpha is used to add the fade effect, so it fades in/out text into the black bg/image
        screen.fill((0, 0, 0))
        screen.blit(image, (0, 240 - image.get_height() / 2))
        screen.blit(black, (0, 0))
        ren = font.render("Press Enter to continue", 1, (255, 255, 255))
        screen.blit(ren, (320 - ren.get_width() / 2, 460))
        pygame.display.flip()
