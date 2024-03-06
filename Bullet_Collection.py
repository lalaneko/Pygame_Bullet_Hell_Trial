import pygame
import sys
from pygame.locals import *
from math import *
import time
import random
from config import *

class Bullet:
    def __init__(self, x, y, speed, color, radius, angle):
        # self.symbol = bullet_symbol
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.radius = radius
        self.angle = angle

    def update(self):
        self.y += self.speed * cos(self.angle)
        self.x += self.speed * sin(self.angle)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def check_collision(self, target):
        # Calculate the distance between the center of the bullet and the center of the player
        distance_x = self.x - (target.x + target.width / 2)
        distance_y = self.y - (target.y + target.height / 2)
        distance = sqrt(distance_x ** 2 + distance_y ** 2)

        # Check if the distance is less than the sum of the bullet's radius and half of the player's width/height
        if distance < (self.radius + max(target.width, target.height) / 2):
            return True
        else:
            return False



class Boss_Bullet(Bullet):
    def update(self):
        self.y += self.speed * cos(self.angle)
        self.x += self.speed * sin(self.angle)

class Boss_8_Split_Bullet(Bullet):
    def split(self):
        for i in range(1,11):
            boss_bullets.append(Boss_Bullet(self.x * 0.99, self.y * 0.99, 4, WHITE, 5, self.angle + pi/5 * i))
