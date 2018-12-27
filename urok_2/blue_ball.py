import pygame

size = width, height = 301, 301
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.circle(screen, (0, 0, 255), event.pos, 20)

    pygame.display.flip()
    clock.tick(50)

pygame.quit()