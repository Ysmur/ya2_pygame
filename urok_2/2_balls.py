import pygame
pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
# метод clock.tick() возвращает количество миллисекунд, прошедших с момента последнего вызова
clock = pygame.time.Clock()
flag = 0
balls = []
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        screen2 = pygame.Surface(screen.get_size())
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            flag = 1
            pos = event.pos
            speed_0 = 1
            speed_1 = -1
            pygame.draw.circle(screen, (pygame.Color('white')), event.pos, 20)
    if flag:
        screen2.fill((0, 0, 0))
        if pos[0] >= width or pos[0] <= 0:
            speed_0 = -speed_0
        if pos[1] >= height or pos[1] <= 0:
            speed_1 = -speed_1
        pos = pos[0] + speed_0, pos[1] + speed_1
        pygame.draw.circle(screen2, (255, 0, 0), pos, 20)
    screen.blit(screen2, (0, 0))
    clock.tick(100)
    pygame.display.flip()

