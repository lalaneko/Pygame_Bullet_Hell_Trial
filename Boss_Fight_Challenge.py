import pygame
import sys
from pygame.locals import *
from math import *
import time
import random
from Danmaku import *
from Bullet_Collection import *
from Sprites import *
from config import *
# 
# # 游戏窗口尺寸
# screen_width = 600
# screen_height = 800
#
# # 定义颜色
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# ENEMY_COLOR = (128, 64, 200)
# BOSS_COLOR = (176, 120, 50)
#

# 初始化Pygame
pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bullet Hell Game")

# 创建玩家对象
player = Player(screen_width // 2 - 10, screen_height - 40, 5, 100)  # TODO

# 创建Boss对象
boss = Boss(screen_width // 2 - 20, screen_height // 2 - 270, 2, 1000)
boss_marker = Boss_Marker(boss)

# 游戏主循环
clock = pygame.time.Clock()

game_over = False


while not game_over:
    screen.fill(BLACK)

    # 存储需要移除的子弹
    bullets_to_remove = []

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                player.shooting = True

        if event.type == KEYUP:
            if event.key == K_SPACE:
                player.shooting = False

    if player.shooting:
        player.shoot()

    if not game_over:
        player.update()
        player.draw(screen)

        for bullet in bullets:
            boss.health -= 0.01
            bullet.update()
            bullet.draw(screen)

            # 检查子弹是否击中Boss
            if bullet.check_collision(boss):
                boss.health -= 10
                if boss.health <= 0:
                    print('Won')
                    game_over = True
                if bullet not in bullets_to_remove:
                    bullets_to_remove.append(bullet)

            # 检查子弹是否超出屏幕
            if bullet.y < 0 or bullet.y > screen_height or bullet.x < 0 or bullet.x > screen_width:
                if bullet not in bullets_to_remove:
                    bullets_to_remove.append(bullet)

        # 移除需要移除的子弹
        for bullet in bullets_to_remove:
            bullets.remove(bullet)


        for boss_bullet in boss_bullets:
            boss_bullet.update()
            boss_bullet.draw(screen)

            # 检查Boss子弹是否击中玩家
            if boss_bullet.check_collision(player):
                player.health -= 10
                boss_bullets.remove(boss_bullet)

            # 检查Boss子弹是否超出屏幕
            if boss_bullet.y < 0 or boss_bullet.y > screen_height:
                boss_bullets.remove(boss_bullet)

        for boss_8_split_bullet in boss_8_split_bullets:
            boss_8_split_bullet.update()
            boss_8_split_bullet.draw(screen)

            # 检查Boss子弹是否击中玩家
            if boss_8_split_bullet.check_collision(player):
                player.health -= 20
                boss_8_split_bullets.remove(boss_8_split_bullet)

            # 检查Boss子弹是否超出屏幕
            if boss_8_split_bullet.y < 0 or boss_8_split_bullet.y > screen_height or boss_8_split_bullet.x < 0 or boss_8_split_bullet.x > screen_width:
                boss_8_split_bullet.split()
                boss_8_split_bullets.remove(boss_8_split_bullet)

        for boss_slow_down_bullet in boss_slow_down_bullets:
            boss_slow_down_bullet.update()
            boss_slow_down_bullet.draw(screen)

            if boss_slow_down_bullet.check_collision(player):
                player.health -= 10
                boss_slow_down_bullets.remove(boss_slow_down_bullet)
            # 检查Boss子弹是否超出屏幕
            if boss_slow_down_bullet.y < 0 or boss_slow_down_bullet.y > screen_height:
                boss_slow_down_bullets.remove(boss_slow_down_bullet)

        boss.update()
        boss.draw(screen)

        boss_marker.update()
        boss_marker.draw(screen)

        # 检查Boss是否与玩家碰撞
        if player.x < boss.x + boss.width and player.x + player.width > boss.x and player.y < boss.y + boss.height and player.y + player.height > boss.y:
            player.health -= 20
            if boss.health <= 0:
                print('Won')
                game_over = True
            print('Lost')
            game_over = True

        # 检查玩家生命值
        if player.health <= 0:
            print('Lost')
            game_over = True

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
