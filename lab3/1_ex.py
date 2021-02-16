#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 17:30:55 2021

@author: iskander
"""

import pygame
from pygame.draw import *
l = 500
height=700 # hieght
height2=430
pygame.init()

screen = pygame.display.set_mode((l, height))
#phon
rect(screen, (250, 250, 250), (0, 0, l, height))
rect(screen, (210, 210, 220), (0, 0, l, 430))
rect(screen, (40, 60, 60), (0, 435, l, 700))
#columns
rect(screen, (190, 220, 210), (0, 10, l/5, height2))
rect(screen, (210, 160, 250), (160, 30, l/5, height2))
rect(screen, (210, 200, 250), (80, 80, l/5, height2))
rect(screen, (140, 240, 140), (390, 20, l/5, height2))
rect(screen, (140, 140, 140), (330, 80, l/5, height2))
#cloud
ellipse(screen, (190, 220, 210), (290, 100, 280, 100))
ellipse(screen, (255, 220, 210), (150, 650, 450, 100))


pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()