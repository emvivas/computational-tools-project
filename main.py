import pygame
from pygame.locals import *
from tkinter import messagebox

class Wall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("wall.jpeg").convert_alpha()
        self.image = pygame.transform.scale(self.image, (25, 25)) 
        self.rect = self.image.get_rect()

class Protagonist(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("bounce.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (17, 17)) 
        self.rect = self.image.get_rect()

class Trophy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("trophy.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (25, 25)) 
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH//2.2
        self.rect.y = HEIGHT//2

def construir_mapa(map):
    listaMuros = []
    x=0
    y=0
    for fila in map:
        for muro in fila:
            if muro == 1:
                listaMuros.append(pygame.Rect(x, y, 25, 25))
            x+=25
        x=0
        y+=25
    return listaMuros

def dibujar_muro(superficie, rectangulo):
    pygame.draw.rect(superficie, GREEN, rectangulo)

def dibujar_mapa(superficie, listaMuros):
    for muro in listaMuros:
        dibujar_muro(superficie, muro)

WIDTH = 650
HEIGHT = 650
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
particle = {
    "object" : pygame.Rect(600, 400, 20, 20), 
    "coordenates" : {'x':0, 'y':0},
    "direction": {'x':0, 'y':0}
}

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Laberinto")
clock = pygame.time.Clock()
listaWall = pygame.sprite.Group()
wall = Wall()
listaWall.add(wall)
listaProtagonist = pygame.sprite.Group()
protagonist = Protagonist()
listaProtagonist.add(protagonist)
       #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11, 12,13,14,15,16,17,18,19,20,21,22,23,24,25]
map =  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1], 
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1], 
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1], 
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1], 
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1], 
        [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1], 
        [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1], 
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1], 
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1], 
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1], 
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1], 
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1], 
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
listaMuros = construir_mapa(map)
listaTrophy = pygame.sprite.Group()
trophy = Trophy()
listaTrophy.add(trophy)

gameOver = False
while not gameOver:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                particle["direction"]['x']=-5
            elif event.key == pygame.K_RIGHT:
                particle["direction"]['x']=+5
            elif event.key == pygame.K_UP:
                particle["direction"]['y']=-5
            elif event.key == pygame.K_DOWN:
                particle["direction"]['y']=+5
        else:
            particle["direction"]['x']=0
            particle["direction"]['y']=0
    particle["coordenates"]['x'] += particle["direction"]['x']
    particle["coordenates"]['y'] += particle["direction"]['y']
    protagonist.rect.x = particle["coordenates"]['x']
    protagonist.rect.y = particle["coordenates"]['y']
    for muro in listaMuros:
        if protagonist.rect.colliderect(muro) or particle["coordenates"]['x'] < 0 or particle["coordenates"]['x'] > WIDTH or particle["coordenates"]['y'] < 0 or particle["coordenates"]['y'] > HEIGHT:
            particle["coordenates"]['x'] -= particle["direction"]['x']
            particle["coordenates"]['y'] -= particle["direction"]['y']

    for trofeo in listaTrophy:
        if protagonist.rect.colliderect(trofeo):
            gameOver=True
            messagebox.showinfo('¡Felicidades!','¡Has ganado!')
    window.fill(BLACK)
    x = 0
    y = 0
    for fila in map:
        for muro in fila:
            if muro == 1:
                wall.rect.x=x
                wall.rect.y=y
                listaWall.add(wall)
                listaWall.draw(window)
            x+=25
        x=0
        y+=25
    listaProtagonist.draw(window)
    listaTrophy.draw(window)
    #dibujar_mapa(window, listaMuros)
    pygame.display.flip()
pygame.quit()
