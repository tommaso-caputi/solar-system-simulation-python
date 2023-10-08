import pygame
import planet

pygame.init()

SCREEN_SIZE = (1000, 720)
screen = pygame.display.set_mode((1000, 720))
clock = pygame.time.Clock()
running = True

pianeta = planet.Planet((255, 0, 0), 20, (100, 100))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")

    pygame.draw.circle(screen, "yellow", (SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2), 40)
    pygame.draw.circle(screen, pianeta.color, pianeta.pos, pianeta.size)

    pygame.display.flip()
    clock.tick(60)


pygame.quit()
