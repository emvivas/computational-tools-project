import pygame

pygame.init()
size = w, h = 800, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True

while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill("white")


    pygame.display.flip()

    clock.tick(60)

pygame.quit()