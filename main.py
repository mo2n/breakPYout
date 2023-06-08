#carica le librerie pg, sys per chiuder le win, 
# random per la creazione del muro

import pygame
import sys
import random
from pygame.locals import *

#inizializzazione pygame
pygame.init()

#definizioni varibili globali per lo schermo
screen_altezza = 600 #width
screen_larghezza = 800 #height

bg = (234, 218, 184)

#colori da utilizzare nel progetto
block_red = (242, 85, 96)
block_green = (86, 174, 87)
block_blue = (69, 177, 232)
block_yellow = (255, 255, 0)

#inizializzazione schermo
screen = pygame.display.set_mode((screen_altezza, screen_larghezza))
pygame.display.set_caption("BreakPYout")# nome progetto window
clock = pygame.time.Clock()

#generatore ciclo
while True:
    clock.tick(60)
    #riempimento con colore del background
    screen.fill(bg)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

pygame.quit