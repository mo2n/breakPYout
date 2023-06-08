#carica le librerie pg, sys per chiuder le win, 
# random per la creazione del muro

import pygame
import sys
import random
from pygame.locals import *

#inizializzazione pygame
pygame.init()

#definizioni varibili globali per lo schermo
screen_altezza = 800 #width
screen_larghezza = 800 #height

#colore background
bg = (234, 218, 184)

#definizione dei blocchi/brik
cols = 8 #colonne
rows = 8 #righe

#colori da utilizzare nel progetto
block_red = (242, 85, 96)
block_green = (86, 174, 87)
block_blue = (69, 177, 232)
block_yellow = (255, 255, 0)

class muro(): #wall
    def __init__(self):
        self.larghezza = screen_larghezza // cols
        self.altezza = 50

    def creazione_muro(self):
        self.blocchi = []
        #definisci una lista vuota per ogni blocco individuale
        blocco_individuale = []
        for row in range(rows):
            blocco_row = []
            #crea una iterazione per ogni colonna
            for col in range(cols):
                blocco_x = col * self.larghezza
                blocco_y = row * self.altezza
                rect = pygame.Rect(blocco_x, blocco_y, self.larghezza, self.altezza)
                 #assegna l'intensita della forza x colpire i blocchi
                if row < 2:
                    forza = 4
                elif row < 4:
                    forza = 3
                elif row < 6:
                    forza = 2
                elif row < 8:
                    forza = 1

                blocco_individuale = [rect, forza]
                #append blocco individuale ai blocchi nelle righe
                blocco_row.append(blocco_individuale)
            self.blocchi.append(blocco_row)

    def disegna_muro(self):
            for row in self.blocchi:
                #assegna i colori in base alla loro forza/resistenza ai colpi
                for blocco in row:
                    if blocco[1] == 4:
                        block_col = block_blue
                    elif blocco[1] == 3:
                        block_col = block_green
                    elif blocco[1] == 2:
                        block_col = block_yellow
                    elif blocco[1] == 1:
                        block_col = block_red
                    
                    pygame.draw.rect(screen, block_col, blocco[0])
                    pygame.draw.rect(screen, bg, (blocco[0]), 2)


muro = muro()
muro.creazione_muro()



#inizializzazione schermo
screen = pygame.display.set_mode((screen_altezza, screen_larghezza))
pygame.display.set_caption("BreakPYout")# nome progetto window
clock = pygame.time.Clock()

#generatore ciclo
while True:
    clock.tick(60)
    #riempimento con colore del background
    screen.fill(bg)

    #disegna muro
    muro.disegna_muro()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

pygame.quit