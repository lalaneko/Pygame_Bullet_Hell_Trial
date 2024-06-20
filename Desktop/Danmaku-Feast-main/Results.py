

import sys
import pygame
from pygame.locals import *
from config import *


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)  # Change to topleft alignment
    surface.blit(textobj, textrect)


def game(screen, result):
    print("Results")
    screen_width = 600

    font_title = pygame.font.SysFont(None, 48)
    font_options = pygame.font.SysFont(None, 36)

    msg = "You won" if result == 1 else "You lost"

    while True:
        screen.fill((0, 0, 0))
        draw_text(msg, font_title, (255, 255, 255), screen, screen_width//2 - font_options.size(msg)[0] // 1.5, 70)

        back_width, back_height = font_options.size("Back")
        back_pos = (screen_width//2 - back_width//1.5, 170)
        back_rect = pygame.Rect(back_pos[0], back_pos[1], back_width, back_height)

        mouse_pos = pygame.mouse.get_pos()

        if back_rect.collidepoint(mouse_pos):
            draw_text("Back", font_title, (255, 0, 0), screen, screen_width//2 - back_width // 1.5, back_pos[1])
        else:
            draw_text("Back", font_title, (255, 255, 255), screen, back_pos[0], back_pos[1])


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and back_rect.collidepoint(mouse_pos):
                return 
             
        pygame.display.set_caption("Results")
        pygame.display.update()


