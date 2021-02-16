# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""
import pygame
from pygame.draw import *

pygame.init()

#
screen = pygame.display.set_mode((400, 400))

rect(screen, (80, 80, 80), (0, 0, 400, 400))

circle(screen, (250,250,0), (200, 200), 100)
rect(screen, (0, 0, 0), (150, 250, 90, 20))

circle(screen, (250,0,0), (150, 170), 20)
circle(screen, (250,0,0), (240, 170), 18)
circle(screen, (0,0,0), (150, 170), 10)
circle(screen, (0,0,0), (240,170), 10)

line(screen, (0,0,0), [100, 120], [180, 160], 15)
line(screen, (0,0,0), [300, 120], [200, 160], 15)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()