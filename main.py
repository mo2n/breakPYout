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

#inizializzazione schermo
screen = pygame.display.set_mode((screen_altezza, screen_larghezza))
pygame.display.set_caption("BreakPyout")# nome progetto window
#font = pygame.font.SysFont('costantia', 30)# definizione font da usare nel progetto
clock = pygame.time.Clock()

#generatore ciclo
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

