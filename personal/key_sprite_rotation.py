import pygame
from pygame.locals import *
from sys import exit
import os

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

class Ship(object):
    def __init__(self):
        self.main_image = pygame.image.load(os.path.join("..", "assets", "ship.jpg")).convert()
        self.image = self.main_image
        self.rect = self.image.get_rect()
        self.rect.center = (320, 240)
        self.dir = 0

    def update(self):
        old_center = self.rect.center
        self.image = pygame.transform.rotate(self.main_image, self.dir)
        self.rect = self.image.get_rect()
        self.rect.center = old_center

    def render(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def turn_left(self):
        self.dir += 45
        if self.dir > 360:
            self.dir = 45

    def turn_right(self):
        self.dir -= 45
        if self.dir < 0:
            self.dir = 315


ship = Ship()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_LEFT]:
        ship.turn_left()
    if pressed_keys[K_RIGHT]:
        ship.turn_right()

    ship.update()
    ship.render(screen)
    pygame.display.update()
