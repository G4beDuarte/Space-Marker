import pygame
from tkinter import simpledialog
import math

pygame.init()

tamanho = (1000,563)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("SpaceMaker")
fundo = pygame.image.load("assets/fundo.jpg")
icone = pygame.image.load("assets/space.png")
fonte = pygame.font.SysFont("Arial", 18)
som = pygame.mixer.Sound("assets/Space_Machine_Power.mp3")
som.play(-1)
branco = (225,225,225)
preto = (0,0,0)


while True:
     for evento in pygame.event.get():
          if evento.type == pygame.QUIT:
               quit()

     tela.fill(branco)
     tela.blit(fundo,(0,0))

     textoOpcoes = fonte.render("Opções:", True, branco)
     textoSalvar = fonte.render("F10 - Salvar marcações", True, branco)
     textoCarregar = fonte.render("F11 - Carregar ultimas marcações", True, branco)
     textoExcluir = fonte.render("F12 - Excluir todas as marcações", True, branco)
     tela.blit(textoOpcoes, (10, 10))
     tela.blit(textoSalvar, (10, 40))
     tela.blit(textoCarregar, (10, 70))
     tela.blit(textoExcluir, (10, 100))

     pygame.display.update()
     clock.tick(60)

pygame.quit()