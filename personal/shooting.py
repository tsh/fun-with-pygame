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
        self.dir = 0
        self.sprite_pos = Vector2(250, 250)

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

    def shoot(self):
        bullet = Bullet(self.sprite_pos.x, self.sprite_pos.y, self.dir)
        bullets.append(bullet)


class Target(object):
    def __init__(self):
        self.image = pygame.image.load(os.path.join("..", "assets", "ship.jpg")).convert()
        self.sprite_pos = Vector2(250, 50)

    def update(self, surface):
        surface.blit(self.image, self.sprite_pos)



class Bullet(object):
    def __init__(self, x, y, angle):
        self.main_image = pygame.image.load(os.path.join("..", "assets", "green_star.png")).convert()
        self.x = x
        self.y = y
        self.speed = 110
        self.angle = angle

    def update(self, surface, dt):
        dx = -math.sin(self.angle*(math.pi / 180.0)) *self.speed*dt
        dy = -math.cos(self.angle*(math.pi / 180.0)) *self.speed*dt
        self.x += dx
        self.y += dy
        surface.blit(self.main_image,(self.x, self.y))
        if self.x > 500 or self.y > 500 or self.x <0 or self.y <0:
            bullets.remove(self)

ship = Ship()
clock = pygame.time.Clock()
bullets = []
target = Target()

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
    if pressed_keys[K_SPACE]:
        ship.shoot()

    ship.update(time_passed, rdir, mdir)
    target.update(screen)
    for bullet in bullets:
        bullet.update(screen, time_passed)
    pygame.display.update()
    screen.fill((0, 0, 0))
