import pygame
pygame.init()
size = width, height = 301, 301
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
x2 = y2 = 0
x1 = y1 = 0


def draw(x1, y1, x2, y2):
    pygame.draw.rect(screen, pygame.Color('black'), (x1, y1, 100, 100), 0)
    pygame.draw.rect(screen, pygame.Color('green'), (x2, y2, 100, 100), 0)
    x2 = y2 = 0

# основной цикл
running = True
while running:

    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 0 < x < 100 and 0 < y < 100:
                x1, y1 = x, y
        if event.type == pygame.MOUSEBUTTONUP:
            x2, y2 = event.pos
    draw(x1, y1, x2, y2)
    pygame.display.flip()

    clock.tick(50)
pygame.quit()
