import pygame
from pygame.locals import *
from tkinter import messagebox

WIDTH = 1200
HEIGHT = 800
   #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
map =  [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1], 
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], 
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1], 
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1], 
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1], 
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], 
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1], 
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1], 
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1], 
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1], 
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1], 
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1], 
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], 
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
TILE_X = WIDTH/len(map[0])
TILE_Y = HEIGHT/len(map)
class Wall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("wall.jpeg").convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILE_X, TILE_Y)) 
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
        self.image = pygame.transform.scale(self.image, (TILE_X * .9, TILE_Y)) 
        self.rect = self.image.get_rect()
        self.rect.x = TILE_X*21.05
        self.rect.y = TILE_Y*20

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, speed_x, speed_y):
        super().__init__()
        self.rect = pygame.Rect(x, y, w, h)
        self.x_accul = 0
        self.y_accul = 0
        self.speed_x = speed_x
        self.speed_y = speed_y


def construir_mapa(map):
    listaMuros = []
    x=0
    y=0
    for fila in map:
        for muro in fila:
            if muro == 1:
                listaMuros.append(pygame.Rect(x, y, TILE_X, TILE_Y))
            x+=TILE_X
        x=0
        y+=TILE_Y
    return listaMuros

def dibujar_muro(superficie, rectangulo):
    pygame.draw.rect(superficie, "green", rectangulo)

def dibujar_mapa(superficie, listaMuros):
    for muro in listaMuros:
        dibujar_muro(superficie, muro)

particle = {
    "object" : pygame.Rect(600, 400, 20, 20), 
    "coordinates" : {'x':TILE_X*13.25, 'y':0},
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
listaMuros = construir_mapa(map)
listaTrophy = pygame.sprite.Group()
trophy = Trophy()
listaTrophy.add(trophy)

obstaculos = [
    (TILE_X * 3.375, TILE_Y * 4.125, TILE_X//4, TILE_Y*.75, 0, 2),
    (TILE_X * 6.375, TILE_Y * 6.125, TILE_X//4, TILE_Y*.75, 0, -2),
    (TILE_X * 9.375, TILE_Y * 4.125, TILE_X//4, TILE_Y*.75, 0, 2),
    (TILE_X * 19.375, TILE_Y * 2.125, TILE_X//4, TILE_Y*.75, 0, 2),
    (TILE_X * 22.375, TILE_Y * 4.125, TILE_X//4, TILE_Y*.75, 0, -2),
    (TILE_X * 25.375, TILE_Y * 2.125, TILE_X//4, TILE_Y*.75, 0, 2),
    (TILE_X * 28.375, TILE_Y * 4.125, TILE_X//4, TILE_Y*.75, 0, -2),
    (TILE_X * 2.375, TILE_Y * 14.125, TILE_X//4, TILE_Y*.75, 0, -2),
    (TILE_X * 6.375, TILE_Y * 12.125, TILE_X//4, TILE_Y*.75, 0, 2),
    (TILE_X * 12.375, TILE_Y * 18.5, TILE_X//4, TILE_Y*1.75, 0, -1)
    ]

obstacles = []
for obstaculo in obstaculos:
    obstacles.append(Obstacle(*obstaculo))

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
    particle["coordinates"]['x'] += particle["direction"]['x']
    particle["coordinates"]['y'] += particle["direction"]['y']
    protagonist.rect.x = particle["coordinates"]['x']
    protagonist.rect.y = particle["coordinates"]['y']
    for muro in listaMuros:
        if protagonist.rect.colliderect(muro) or particle["coordinates"]['x'] < 0 or particle["coordinates"]['x'] > WIDTH or particle["coordinates"]['y'] < 0 or particle["coordinates"]['y'] > HEIGHT:
            particle["coordinates"]['x'] -= particle["direction"]['x']
            particle["coordinates"]['y'] -= particle["direction"]['y']
    for trofeo in listaTrophy:
        if protagonist.rect.colliderect(trofeo):
            gameOver=True
            messagebox.showinfo('¡Felicidades!','¡Has ganado!')
    for obstacle in obstacles:
        obstacle.rect.x += obstacle.speed_x
        obstacle.rect.y += obstacle.speed_y
        obstacle.x_accul += obstacle.speed_x
        obstacle.y_accul += obstacle.speed_y
        if abs(obstacle.x_accul) > 2*TILE_X:
            obstacle.speed_x *= -1
            obstacle.x_accul = 0
        if abs(obstacle.y_accul) > 2*TILE_Y:
            obstacle.speed_y *= -1
            obstacle.y_accul = 0

        if obstacle.rect.y < 0 or obstacle.rect.y > HEIGHT:
            obstacle.speed_y *= -1
        if obstacle.rect.x < 0 or obstacle.rect.x > WIDTH:
            obstacle.speed_x *= -1
        if protagonist.rect.colliderect(obstacle):
            gameOver=True
            messagebox.showinfo('Game over','¡Inténtalo de nuevo!')

    window.fill("black")
    x = 0
    y = 0
    for fila in map:
        for muro in fila:
            if muro == 1:
                wall.rect.x=x
                wall.rect.y=y
                listaWall.add(wall)
                listaWall.draw(window)
            x+=TILE_X
        x=0
        y+=TILE_Y
    listaProtagonist.draw(window)
    listaTrophy.draw(window)

    for obstacle in obstacles:
        pygame.draw.rect(window, "red", obstacle)

    #dibujar_mapa(window, listaMuros)
    pygame.display.flip()
pygame.quit()
