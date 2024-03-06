import pygame
import sys
from pygame.locals import *
from math import *
import time
import random
from config import *
from Bullet_Collection import *


def S_spray(self):
    self.S_temp_count_frequency_modifier += 1
    if self.S_temp_count_frequency_modifier % 6 == 0:
        self.S_temp_count += 1
        if self.S_temp_count % 200 == self.S_temp_count % 400:
            self.S_temp += 0.009
        else:
            self.S_temp -= 0.009
        self.S_bullet_angle += self.S_temp ** 2 - self.S_temp + 0.01
        self.shoot(angle=self.S_bullet_angle)
    elif self.S_temp_count_frequency_modifier % 6 == 1:
        self.shoot(angle=(self.S_bullet_angle + 1 * pi / 3))
    elif self.S_temp_count_frequency_modifier % 6 == 2:
        self.shoot(angle=(self.S_bullet_angle + 2 * pi / 3))
    elif self.S_temp_count_frequency_modifier % 6 == 3:
        self.shoot(angle=(self.S_bullet_angle + 3 * pi / 3))
    elif self.S_temp_count_frequency_modifier % 6 == 4:
        self.shoot(angle=(self.S_bullet_angle + 4 * pi / 3))
    elif self.S_temp_count_frequency_modifier % 6 == 5:
        self.shoot(angle=(self.S_bullet_angle + 5 * pi / 3))

def S_spray_2(self):
    if self.S_temp_count_frequency_modifier_2 > 2200:
        self.S_flag_2 = 0
    if self.S_temp_count_frequency_modifier_2 < 0:
        self.S_flag_2 = 1
    print(self.S_flag_2, self.S_temp_count_frequency_modifier_2)
    if self.S_flag_2:
        self.S_temp_count_frequency_modifier_2 += 1
    else:
        self.S_temp_count_frequency_modifier_2 -= 1
    self.S_temp_count_2 += 0.01
    if self.S_temp_count_frequency_modifier_2 < 500:
        if self.S_temp_count_frequency_modifier_2 % 4 == 0:
            self.S_bullet_angle_2 = self.S_temp_count_2  * sin(self.S_temp_count_2)
            self.shoot(angle=self.S_bullet_angle_2)
    elif self.S_temp_count_frequency_modifier_2 < 1000:
        if self.S_temp_count_frequency_modifier_2 % 4 == 0:
            self.S_bullet_angle_2 = self.S_temp_count_2  * sin(self.S_temp_count_2)
            self.shoot(angle=self.S_bullet_angle_2)
            self.S_bullet_angle_2 = (self.S_temp_count_2-5) * cos(self.S_temp_count_2-5)
            self.shoot(angle=self.S_bullet_angle_2)
    elif self.S_temp_count_frequency_modifier_2 < 1500:
        if self.S_temp_count_frequency_modifier_2 % 4 == 0:
            self.S_bullet_angle_2 = self.S_temp_count_2  * sin(self.S_temp_count_2)
            self.shoot(angle=self.S_bullet_angle_2)
            self.S_bullet_angle_2 = (self.S_temp_count_2-5) * cos(self.S_temp_count_2-5)
            self.shoot(angle=self.S_bullet_angle_2)
            self.S_bullet_angle_2 = (self.S_temp_count_2-10) * tan(self.S_temp_count_2-10)
            self.shoot(angle=self.S_bullet_angle_2)
    else:
        if self.S_temp_count_frequency_modifier_2 % 6 == 0:
            self.S_bullet_angle_2 = self.S_temp_count_2  * sin(self.S_temp_count_2)
            self.shoot(angle=self.S_bullet_angle_2)
            self.S_bullet_angle_2 = (self.S_temp_count_2-5) * cos(self.S_temp_count_2-5)
            self.shoot(angle=self.S_bullet_angle_2)
            self.S_bullet_angle_2 = (self.S_temp_count_2-10) * tan(self.S_temp_count_2-10)
            self.shoot(angle=self.S_bullet_angle_2)
            self.S_bullet_angle_2 = - self.S_temp_count_2 * sin(self.S_temp_count_2)
            self.shoot(angle=self.S_bullet_angle_2)
            self.S_bullet_angle_2 = - (self.S_temp_count_2-5) * cos(self.S_temp_count_2-5)
            self.shoot(angle=self.S_bullet_angle_2)
            self.S_bullet_angle_2 = - (self.S_temp_count_2-10) * tan(self.S_temp_count_2-10)
            self.shoot(angle=self.S_bullet_angle_2)


def S_split(self):
    self.S_temp_count_frequency_modifier_split += 1
    if self.S_temp_count_frequency_modifier_split % 15 == 0:
        boss_8_split_bullets.append(Boss_8_Split_Bullet(self.x + self.width / 2, self.y + self.height / 2, 5, WHITE, 7, random.uniform(0, 2*pi)))