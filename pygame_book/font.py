import pygame
from pygame.locals import *
pygame.init()
my_font = pygame.font.SysFont("arial", 64)
name_surface = my_font.render("PYgaaaameee!", True, (0, 0, 0), (255, 255, 255))
screen = pygame.display.set_mode((640, 480), 0, 32)
screen.blit(name_surface, (0,0))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
            
    screen.blit(name_surface, (0,0))
    pygame.display.update()
