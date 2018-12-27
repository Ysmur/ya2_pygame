import pygame
pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
# метод clock.tick() возвращает количество миллисекунд, прошедших с момента последнего вызова
clock = pygame.time.Clock()
RADIUS_PLUS = 10
pygame.time.set_timer(RADIUS_PLUS, 10)
radius = 0
flag = 0

running = True
while running:
    screen.fill((0, 0, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            flag = 1
            screen.fill((0, 0, 255))
            radius = 0
            circle = event.pos
            pygame.draw.circle(screen, (pygame.Color('yellow')), event.pos, radius)
        if event.type == RADIUS_PLUS and flag:
            radius += 1
            pygame.draw.circle(screen, (pygame.Color('yellow')), circle, radius)


    pygame.display.flip()
    clock.tick(100)
