import pygame
from tkinter import simpledialog
import math

pygame.init()

tamanho = (1000,563)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("SpaceMaker")
branco = (225,225,225)

while True:
     for evento in pygame.event.get():
          if evento.type == pygame.QUIT:
               quit()

     tela.fill(branco)
     pygame.display.update()
     clock.tick(60)
     
pygame.quit()