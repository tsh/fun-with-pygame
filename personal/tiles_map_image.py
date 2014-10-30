import pygame
from pygame.locals import *
from sys import exit
import os
import math
from vector2 import Vector2

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

class Ship(object):
    def __init__(self):
        self.main_image = pygame.image.load(os.path.join("..", "assets", "ship.jpg")).convert()
        self.image = self.main_image  # we need copy for rotating sprite
        self.rect = self.image.get_rect()
        self.rect.center = (320, 240)
        self.dir = 0
        self.sprite_pos = Vector2(200, 150)

    def update(self, dt, rdir, mdir):
        rotated_sprite = pygame.transform.rotate(self.main_image, self.dir)
        w, h = rotated_sprite.get_size()
        sprite_draw_pos = Vector2(self.sprite_pos.x-w/2, self.sprite_pos.y-h/2)
        screen.blit(rotated_sprite, sprite_draw_pos)

        self.dir += rdir * 45 * dt

        dx = math.sin(self.dir*math.pi/180)
        dy = math.cos(self.dir*math.pi/180)
        v = Vector2(dx, dy)
        v *= mdir
        self.sprite_pos+= v * 50 * dt

tile_map = [[1,1,1,1,1,1,1,1],
       [1,0,0,0,0,0,0,1],
       [1,0,0,0,1,0,0,1],
       [1,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,1],
       [1,1,1,1,1,1,1,1]]

map_height = len(tile_map)
map_width = len(tile_map[0])
star = pygame.image.load(os.path.join("..", "assets", "green_star.png")).convert()
tile_width = star.get_rect().width
tile_height = star.get_rect().height

def render_map():
    for row in range(map_height):
        for column in range(map_width):
            if tile_map[row][column] == 1:
                x = tile_width * column
                y = tile_height * row
                screen.blit(star, (x,y))

ship = Ship()
clock = pygame.time.Clock()

while True:
    time_passed = clock.tick() / 1000.0

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    pressed_keys = pygame.key.get_pressed()
    rdir = 0.
    mdir = 0.
    if pressed_keys[K_LEFT]:
        rdir += 1
    if pressed_keys[K_RIGHT]:
        rdir -= 1
    if pressed_keys[K_UP]:
        mdir -= 1
    if pressed_keys[K_DOWN]:
        mdir += 1

    render_map()
    ship.update(time_passed, rdir, mdir)
    pygame.display.update()
