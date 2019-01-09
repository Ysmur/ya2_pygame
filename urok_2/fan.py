import pygame
pygame.init()
size = width, height = 201, 201
screen = pygame.display.set_mode(size)
# метод clock.tick() возвращает количество миллисекунд, прошедших с момента последнего вызова
clock = pygame.time.Clock()


def draw():
    pygame.draw.circle(screen, (255, 255, 255), (100, 100), 10)
    pygame.draw
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw()
    pygame.display.flip()

    clock.tick(100)