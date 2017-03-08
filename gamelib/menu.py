#! /usr/bin/env python

import pygame
from pygame.locals import *

from cutscenes import *
from data import *


def RunGame(screen):
    #Game(screen) #Add the game bit here
    play_music() #Add name of music file here, 0.75


def Help(screen):  # Show help screen if the user chooses controls option in the menu
    cutscene(screen, ["CONTROLS:",
                      # Calls cutscene which cuts teh menu scene and changes screen to cutscene to display controls to the player
                      "",
                      "Move: Arrow Keys",
                      "Jump: Space",
                      "Return: Escape key (ESC)",
                      "Music off: = S key",
                      "Music on: = M key",
                      "Pause: P key",
                      "Press hold the Space key to extend your air time"])


class menuStyle:
    def __init__(self, *options):

        self.options = options  #Assign all the options given in menu, called with menuStyle
        self.x = 0
        self.y = 0
        self.font = pygame.font.Font(None, 32)
        self.option = 0
        self.width = 1
        self.color = [0, 0, 0]
        self.hcolor = [255, 0, 0]
        self.height = len(self.options) * self.font.get_height()
        for o in self.options:
            text = o[0]
            ren = self.font.render(text, 2, (0, 0, 0))  #Get width of the text for every option
            if ren.get_width() > self.width:
                self.width = ren.get_width()

    def draw(self, surface):
        i = 0
        for o in self.options:
            if i == self.option:
                clr = self.hcolor  #Change highlight color of the option if user is at that option using the variable i
            else:
                clr = self.color  #Else the color of other position options remains the same
            text = o[0]
            ren = self.font.render(text, 2, clr)
            if ren.get_width() > self.width:
                self.width = ren.get_width()
            surface.blit(ren,
                         ((self.x + self.width / 2) - ren.get_width() / 2, self.y + i * (self.font.get_height() + 4)))  #Render and position the fonts on the surface
            i += 1

    def update(self, events):
        for e in events:  #Check for events
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_DOWN:  #If down key then
                    self.option += 1  #Increase the position of the option by 1
                if e.key == pygame.K_UP: #If up key then
                    self.option -= 1  #Decrease the position of the option by 1
                if e.key == pygame.K_RETURN:  #If enter button is pressed i.e. chosen
                    self.options[self.option][1]()  #Set this option as chosen
        if self.option > len(self.options) - 1:
            self.option = 0  #Move the option back to the first option if the player tries to reach beyond the last given option
        if self.option < 0:
            self.option = len(self.options) - 1  #Move the option back to the top i.e. the last option in the list if the player tries to reach above the first option

    #METHODS

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def set_font(self, font):
        self.font = font

    def set_highlight_color(self, color):
        self.hcolor = color

    def set_normal_color(self, color):
        self.color = color

    def center_at(self, x, y):
        self.x = x - (self.width / 2)
        self.y = y - (self.height / 2)

class Menu(object):
    def __init__(self, screen):
        self.screen = screen  # Set screen
        self.menu = menuStyle(["NEW GAME", lambda: RunGame(screen)], ["CONTROLS", lambda: Help(screen)],
                              ["QUIT GAME", sys.exit])  # Set menu options by calling menuStyle
        self.menu.set_highlight_color((255, 0, 0))
        self.menu.set_normal_color((255, 255, 255))
        self.menu.center_at(300, 400)
        self.menu.set_font(pygame.font.Font(filepath("fonts/font.ttf"), 16))  # Set font for menu text
        self.bg = load_image("menu.png")  # Load menu bg image
        self.font = pygame.font.Font(filepath("fonts/font.ttf"), 16)
        self.font2 = pygame.font.Font(filepath("fonts/Roboto-Regular.ttf"), 45)
        self.clock = pygame.time.Clock()
        events = pygame.event.get()  # Create event
        self.menu.update(events)
        self.menu.draw(self.screen)
        self.main_loop()  # Main loop for menu is called

    def main_loop(self):
        while 1:
            self.clock.tick(30)
            events = pygame.event.get()  # Get any events in the loop
            self.menu.update(events)
            for e in events:
                if e.type == QUIT:
                    pygame.quit()
                    return
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    pygame.quit()
                    return

            self.screen.blit(self.bg, (0, 0))

            ren = self.font2.render("Team", 1, (255, 255, 255))
            self.screen.blit(ren, (320 - ren.get_width() / 2, 180))

            ren = self.font2.render("Mandarine", 1, (255, 255, 255))
            self.screen.blit(ren, (320 - ren.get_width() / 2, 235))

            ren = self.font2.render("Founder's Fire v2.0", 1, (255, 255, 255))
            self.screen.blit(ren, (320 - ren.get_width() / 2, 80))

            self.menu.draw(self.screen)
            pygame.display.flip()
