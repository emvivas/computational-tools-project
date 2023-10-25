import pygame
from pygame.locals import *
import sys

pygame.init()
size = w, h = 800, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

player = pygame.Rect(0, 0, 20, 20)
player.center = screen.get_rect().center
speed = 5

running = True
while running:
    clock.tick(60)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    player.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * speed
    player.x = max(-5, min(player.x, w - 15))
    player.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * speed
    player.y = max(-5, min(player.y, h - 15))

    print(player.x, player.y)

    player.centerx = player.centerx % screen.get_width()
    player.centery = player.centery % screen.get_height()

    screen.fill("white")
    pygame.draw.circle(screen, "blue", player.center, 5)
    pygame.display.flip()

pygame.quit()